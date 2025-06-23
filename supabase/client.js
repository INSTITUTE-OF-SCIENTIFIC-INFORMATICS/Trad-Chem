import { createClient } from '@supabase/supabase-js'

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || 'https://your-project.supabase.co'
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || 'your-anon-key'

export const supabase = createClient(supabaseUrl, supabaseAnonKey)

// Database table names
export const TABLES = {
  USERS: 'users',
  MEDICINES: 'medicines',
  BENEFITS: 'benefits',
  DISEASES: 'diseases',
  INGREDIENTS: 'ingredients',
  MEDICINE_SYSTEMS: 'medicine_systems',
  CATEGORIES: 'categories',
  CHAT_SESSIONS: 'chat_sessions',
  CHAT_MESSAGES: 'chat_messages',
  USER_FAVORITES: 'user_favorites',
  SEARCH_HISTORY: 'search_history'
}

// Schema names
export const SCHEMAS = {
  PUBLIC: 'public',
  TRADCHEM: 'tradchem'
}

// Helper functions for database operations
export const dbHelpers = {
  // Medicine operations
  async getMedicines(limit = 100, offset = 0) {
    const { data, error } = await supabase
      .from(`${SCHEMAS.TRADCHEM}.${TABLES.MEDICINES}`)
      .select(`
        *,
        traditional_system:medicine_systems(name),
        category:categories(name),
        benefits:medicine_benefits(benefit:benefits(name, description)),
        diseases:medicine_diseases(disease:diseases(name, description)),
        ingredients:medicine_ingredients(ingredient:ingredients(name, smiles_notation, molecular_weight))
      `)
      .range(offset, offset + limit - 1)
      .order('created_at', { ascending: false })

    return { data, error }
  },

  async searchMedicines(query, searchType = 'name', limit = 20) {
    let queryBuilder = supabase
      .from(`${SCHEMAS.TRADCHEM}.${TABLES.MEDICINES}`)
      .select(`
        *,
        traditional_system:medicine_systems(name),
        category:categories(name),
        benefits:medicine_benefits(benefit:benefits(name, description)),
        diseases:medicine_diseases(disease:diseases(name, description)),
        ingredients:medicine_ingredients(ingredient:ingredients(name, smiles_notation, molecular_weight))
      `)

    switch (searchType) {
      case 'name':
        queryBuilder = queryBuilder.or(`product_name.ilike.%${query}%,scientific_name.ilike.%${query}%`)
        break
      case 'benefit':
        queryBuilder = queryBuilder.or(`benefits.benefit.name.ilike.%${query}%`)
        break
      case 'disease':
        queryBuilder = queryBuilder.or(`diseases.disease.name.ilike.%${query}%`)
        break
      case 'ingredient':
        queryBuilder = queryBuilder.or(`ingredients.ingredient.name.ilike.%${query}%`)
        break
      default:
        queryBuilder = queryBuilder.or(`product_name.ilike.%${query}%,scientific_name.ilike.%${query}%,description.ilike.%${query}%`)
    }

    const { data, error } = await queryBuilder
      .limit(limit)
      .order('created_at', { ascending: false })

    return { data, error }
  },

  async getMedicineById(id) {
    const { data, error } = await supabase
      .from(`${SCHEMAS.TRADCHEM}.${TABLES.MEDICINES}`)
      .select(`
        *,
        traditional_system:medicine_systems(name),
        category:categories(name),
        benefits:medicine_benefits(benefit:benefits(name, description)),
        diseases:medicine_diseases(disease:diseases(name, description)),
        ingredients:medicine_ingredients(ingredient:ingredients(name, smiles_notation, molecular_weight))
      `)
      .eq('id', id)
      .single()

    return { data, error }
  },

  // Chat operations
  async createChatSession(userId, sessionName = null) {
    const { data, error } = await supabase
      .from(`${SCHEMAS.TRADCHEM}.${TABLES.CHAT_SESSIONS}`)
      .insert({
        user_id: userId,
        session_name: sessionName || `Chat ${new Date().toLocaleString()}`
      })
      .select()
      .single()

    return { data, error }
  },

  async getChatSessions(userId) {
    const { data, error } = await supabase
      .from(`${SCHEMAS.TRADCHEM}.${TABLES.CHAT_SESSIONS}`)
      .select('*')
      .eq('user_id', userId)
      .order('updated_at', { ascending: false })

    return { data, error }
  },

  async getChatMessages(sessionId) {
    const { data, error } = await supabase
      .from(`${SCHEMAS.TRADCHEM}.${TABLES.CHAT_MESSAGES}`)
      .select('*')
      .eq('session_id', sessionId)
      .order('created_at', { ascending: true })

    return { data, error }
  },

  async addChatMessage(sessionId, userId, message, response = null, messageType = 'user', confidenceScore = null, sources = [], medicineReferences = []) {
    const { data, error } = await supabase
      .from(`${SCHEMAS.TRADCHEM}.${TABLES.CHAT_MESSAGES}`)
      .insert({
        session_id: sessionId,
        user_id: userId,
        message,
        response,
        message_type: messageType,
        confidence_score: confidenceScore,
        sources,
        medicine_references: medicineReferences
      })
      .select()
      .single()

    return { data, error }
  },

  // User favorites
  async addToFavorites(userId, medicineId) {
    const { data, error } = await supabase
      .from(`${SCHEMAS.TRADCHEM}.${TABLES.USER_FAVORITES}`)
      .insert({
        user_id: userId,
        medicine_id: medicineId
      })
      .select()
      .single()

    return { data, error }
  },

  async removeFromFavorites(userId, medicineId) {
    const { error } = await supabase
      .from(`${SCHEMAS.TRADCHEM}.${TABLES.USER_FAVORITES}`)
      .delete()
      .eq('user_id', userId)
      .eq('medicine_id', medicineId)

    return { error }
  },

  async getFavorites(userId) {
    const { data, error } = await supabase
      .from(`${SCHEMAS.TRADCHEM}.${TABLES.USER_FAVORITES}`)
      .select(`
        *,
        medicine:medicines(
          *,
          traditional_system:medicine_systems(name),
          category:categories(name)
        )
      `)
      .eq('user_id', userId)
      .order('created_at', { ascending: false })

    return { data, error }
  },

  // Search history
  async addSearchHistory(userId, query, searchType, resultsCount) {
    const { data, error } = await supabase
      .from(`${SCHEMAS.TRADCHEM}.${TABLES.SEARCH_HISTORY}`)
      .insert({
        user_id: userId,
        query,
        search_type: searchType,
        results_count: resultsCount
      })
      .select()
      .single()

    return { data, error }
  },

  async getSearchHistory(userId, limit = 20) {
    const { data, error } = await supabase
      .from(`${SCHEMAS.TRADCHEM}.${TABLES.SEARCH_HISTORY}`)
      .select('*')
      .eq('user_id', userId)
      .order('created_at', { ascending: false })
      .limit(limit)

    return { data, error }
  },

  // Statistics
  async getStatistics() {
    const [
      { count: totalMedicines },
      { count: totalBenefits },
      { count: totalDiseases },
      { count: totalIngredients },
      { count: totalSystems }
    ] = await Promise.all([
      supabase.from(`${SCHEMAS.TRADCHEM}.${TABLES.MEDICINES}`).select('*', { count: 'exact', head: true }),
      supabase.from(`${SCHEMAS.TRADCHEM}.${TABLES.BENEFITS}`).select('*', { count: 'exact', head: true }),
      supabase.from(`${SCHEMAS.TRADCHEM}.${TABLES.DISEASES}`).select('*', { count: 'exact', head: true }),
      supabase.from(`${SCHEMAS.TRADCHEM}.${TABLES.INGREDIENTS}`).select('*', { count: 'exact', head: true }),
      supabase.from(`${SCHEMAS.TRADCHEM}.${TABLES.MEDICINE_SYSTEMS}`).select('*', { count: 'exact', head: true })
    ])

    return {
      total_medicines: totalMedicines || 0,
      total_benefits: totalBenefits || 0,
      total_diseases: totalDiseases || 0,
      total_ingredients: totalIngredients || 0,
      total_systems: totalSystems || 0,
      last_updated: new Date().toISOString()
    }
  }
}

// Authentication helpers
export const authHelpers = {
  async signUp(email, password, fullName = null) {
    const { data, error } = await supabase.auth.signUp({
      email,
      password,
      options: {
        data: {
          full_name: fullName
        }
      }
    })
    return { data, error }
  },

  async signIn(email, password) {
    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password
    })
    return { data, error }
  },

  async signOut() {
    const { error } = await supabase.auth.signOut()
    return { error }
  },

  async getCurrentUser() {
    const { data: { user }, error } = await supabase.auth.getUser()
    return { user, error }
  },

  async getCurrentSession() {
    const { data: { session }, error } = await supabase.auth.getSession()
    return { session, error }
  }
}

// Real-time subscriptions
export const realtimeHelpers = {
  subscribeToChatMessages(sessionId, callback) {
    return supabase
      .channel(`chat_messages_${sessionId}`)
      .on('postgres_changes', {
        event: 'INSERT',
        schema: SCHEMAS.TRADCHEM,
        table: TABLES.CHAT_MESSAGES,
        filter: `session_id=eq.${sessionId}`
      }, callback)
      .subscribe()
  },

  subscribeToUserFavorites(userId, callback) {
    return supabase
      .channel(`user_favorites_${userId}`)
      .on('postgres_changes', {
        event: '*',
        schema: SCHEMAS.TRADCHEM,
        table: TABLES.USER_FAVORITES,
        filter: `user_id=eq.${userId}`
      }, callback)
      .subscribe()
  }
}

export default supabase 