import { serve } from "https://deno.land/std@0.168.0/http/server.ts"
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}

serve(async (req) => {
  // Handle CORS preflight requests
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
  }

  try {
    // Create Supabase client
    const supabaseClient = createClient(
      Deno.env.get('SUPABASE_URL') ?? '',
      Deno.env.get('SUPABASE_ANON_KEY') ?? '',
      {
        global: {
          headers: { Authorization: req.headers.get('Authorization')! },
        },
      }
    )

    // Get request body
    const { message, sessionId, context } = await req.json()

    // Get user from auth
    const { data: { user }, error: authError } = await supabaseClient.auth.getUser()
    if (authError || !user) {
      return new Response(
        JSON.stringify({ error: 'Unauthorized' }),
        { status: 401, headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
      )
    }

    // Search for relevant medicines in the database
    const { data: medicines, error: searchError } = await supabaseClient
      .from('tradchem.medicines')
      .select(`
        *,
        traditional_system:medicine_systems(name),
        category:categories(name),
        benefits:medicine_benefits(benefit:benefits(name, description)),
        diseases:medicine_diseases(disease:diseases(name, description)),
        ingredients:medicine_ingredients(ingredient:ingredients(name, smiles_notation, molecular_weight))
      `)
      .or(`product_name.ilike.%${message}%,scientific_name.ilike.%${message}%,description.ilike.%${message}%`)
      .limit(5)

    if (searchError) {
      console.error('Search error:', searchError)
    }

    // Build context from database results
    let dbContext = ''
    if (medicines && medicines.length > 0) {
      dbContext = 'Relevant traditional medicines from our database:\n\n'
      medicines.forEach((medicine, index) => {
        dbContext += `${index + 1}. ${medicine.product_name}`
        if (medicine.scientific_name) {
          dbContext += ` (${medicine.scientific_name})`
        }
        dbContext += `\n`
        if (medicine.description) {
          dbContext += `Description: ${medicine.description}\n`
        }
        if (medicine.traditional_system?.name) {
          dbContext += `Traditional System: ${medicine.traditional_system.name}\n`
        }
        if (medicine.benefits && medicine.benefits.length > 0) {
          dbContext += `Benefits: ${medicine.benefits.map(b => b.benefit.name).join(', ')}\n`
        }
        if (medicine.diseases && medicine.diseases.length > 0) {
          dbContext += `Diseases: ${medicine.diseases.map(d => d.disease.name).join(', ')}\n`
        }
        if (medicine.ingredients && medicine.ingredients.length > 0) {
          dbContext += `Ingredients: ${medicine.ingredients.map(i => i.ingredient.name).join(', ')}\n`
        }
        dbContext += '\n'
      })
    }

    // Generate AI response using OpenAI (if available) or fallback
    let aiResponse = ''
    let confidenceScore = 0.8
    let sources = []
    let medicineReferences = medicines?.map(m => m.id) || []

    // Try to use OpenAI if API key is available
    const openaiApiKey = Deno.env.get('OPENAI_API_KEY')
    if (openaiApiKey) {
      try {
        const openaiResponse = await fetch('https://api.openai.com/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${openaiApiKey}`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            model: 'gpt-3.5-turbo',
            messages: [
              {
                role: 'system',
                content: `You are TradChem LLM, an expert assistant specializing in traditional medicine and chemical compounds. 
                You have access to a comprehensive database of traditional medicines, their benefits, chemical compositions, and SMILES notations.
                Always provide accurate, evidence-based information and cite sources when possible.
                If you're not sure about something, say so rather than making up information.
                Focus on traditional medicine knowledge and be helpful to users seeking information about traditional remedies.`
              },
              {
                role: 'user',
                content: `Context about traditional medicines: ${dbContext}\n\nUser question: ${message}`
              }
            ],
            max_tokens: 1000,
            temperature: 0.7,
          }),
        })

        const openaiData = await openaiResponse.json()
        if (openaiData.choices && openaiData.choices[0]) {
          aiResponse = openaiData.choices[0].message.content
          confidenceScore = 0.9
        }
      } catch (error) {
        console.error('OpenAI error:', error)
      }
    }

    // Fallback response if OpenAI is not available or fails
    if (!aiResponse) {
      aiResponse = generateFallbackResponse(message, medicines)
      confidenceScore = 0.6
    }

    // Extract sources from medicines
    if (medicines && medicines.length > 0) {
      sources = medicines
        .map(m => m.source)
        .filter(s => s)
        .slice(0, 3) // Limit to 3 sources
    }

    // Save chat message to database
    if (sessionId) {
      await supabaseClient
        .from('tradchem.chat_messages')
        .insert({
          session_id: sessionId,
          user_id: user.id,
          message,
          response: aiResponse,
          message_type: 'user',
          confidence_score: null,
          sources: [],
          medicine_references: []
        })

      await supabaseClient
        .from('tradchem.chat_messages')
        .insert({
          session_id: sessionId,
          user_id: user.id,
          message: '',
          response: aiResponse,
          message_type: 'assistant',
          confidence_score: confidenceScore,
          sources,
          medicine_references: medicineReferences
        })
    }

    // Return response
    return new Response(
      JSON.stringify({
        response: aiResponse,
        confidence: confidenceScore,
        sources,
        medicine_references: medicineReferences,
        timestamp: new Date().toISOString()
      }),
      { 
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        status: 200 
      }
    )

  } catch (error) {
    console.error('Error:', error)
    return new Response(
      JSON.stringify({ error: 'Internal server error' }),
      { 
        status: 500, 
        headers: { ...corsHeaders, 'Content-Type': 'application/json' } 
      }
    )
  }
})

// Fallback response generator
function generateFallbackResponse(message: string, medicines: any[]): string {
  const lowerMessage = message.toLowerCase()
  
  if (medicines && medicines.length > 0) {
    const medicine = medicines[0]
    return `Based on our database, I found information about ${medicine.product_name}. 
    
${medicine.description || 'This traditional medicine has been used in various traditional medicine systems.'}

${medicine.benefits && medicine.benefits.length > 0 ? 
  `Benefits: ${medicine.benefits.map(b => b.benefit.name).join(', ')}` : ''}

${medicine.diseases && medicine.diseases.length > 0 ? 
  `Traditionally used for: ${medicine.diseases.map(d => d.disease.name).join(', ')}` : ''}

${medicine.traditional_system?.name ? 
  `Traditional System: ${medicine.traditional_system.name}` : ''}

Please note that this information is for educational purposes only and should not replace professional medical advice.`
  }

  if (lowerMessage.includes('turmeric') || lowerMessage.includes('curcumin')) {
    return `Turmeric (Curcuma longa) is a well-known traditional medicine used in Ayurvedic medicine. 
    
Key benefits:
- Anti-inflammatory properties
- Antioxidant effects
- Digestive support
- Immune system enhancement

Active compound: Curcumin (SMILES: CC1=CC(=C(C=C1)O)C(=O)O)

Traditional uses include treating inflammation, arthritis, and digestive issues. Always consult with healthcare professionals before use.`
  }

  if (lowerMessage.includes('ashwagandha') || lowerMessage.includes('withania')) {
    return `Ashwagandha (Withania somnifera) is an important adaptogenic herb in Ayurvedic medicine.
    
Key benefits:
- Stress reduction
- Energy enhancement
- Immune support
- Adaptogenic effects

Traditional uses include managing stress, anxiety, and fatigue. It's considered a powerful adaptogen that helps the body adapt to various stressors.`
  }

  if (lowerMessage.includes('smiles') || lowerMessage.includes('chemical')) {
    return `SMILES (Simplified Molecular Input Line Entry System) is a notation for representing chemical structures.
    
In our database, each traditional medicine ingredient has associated SMILES notations for its active compounds. This allows for:
- Chemical analysis
- Molecular property calculations
- Drug discovery applications
- Structure-activity relationship studies

For example, curcumin's SMILES notation is: CC1=CC(=C(C=C1)O)C(=O)O`
  }

  return `I'm TradChem LLM, your assistant for traditional medicine information. 

I can help you with:
- Information about specific traditional medicines
- Chemical compositions and SMILES notations
- Benefits and therapeutic uses
- Searching the traditional medicine database
- Understanding molecular properties

Please ask me about any traditional medicine or chemical compound you're interested in!`
} 