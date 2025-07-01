#!/usr/bin/env python3
"""
TradChem LLM Integration Example

This example shows how to integrate TradChem database with the Trad-Chem LLM chatbot.
Repository: https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem-LLM

Author: SaltyHeart
"""

import json
from tradchem import llm_query, get_database_stats, search_by_benefits, search_by_disease


def main_integration_example():
    """Main integration example showing core functionality."""
    
    print("🌿 TradChem Database LLM Integration Example")
    print("=" * 50)
    
    # 1. Get database statistics
    print("\n📊 Database Statistics:")
    stats = get_database_stats()
    print(f"   Total medicines: {stats['total_medicines']}")
    print(f"   Traditional systems: {', '.join(stats['traditional_systems'][:5])}")
    print(f"   Geographic regions: {', '.join(stats['geographic_regions'][:5])}")
    
    # 2. LLM query examples
    print("\n🤖 LLM Query Examples:")
    
    queries = [
        "What plants help with inflammation?",
        "Turmeric benefits",
        "Ayurvedic herbs for diabetes",
        "Anti-inflammatory traditional medicine"
    ]
    
    for query in queries:
        print(f"\n📝 Query: {query}")
        response = llm_query(query, context_limit=3)
        print(f"   Found: {response['total_found']} relevant medicines")
        
        for i, medicine in enumerate(response['context_data'], 1):
            print(f"   {i}. {medicine['product_name']}")
            if medicine['benefits']:
                print(f"      Benefits: {', '.join(medicine['benefits'][:3])}")
    
    # 3. Specific search examples
    print("\n🔍 Specific Search Examples:")
    
    # Search by benefits
    inflammation_meds = search_by_benefits("inflammation", limit=3)
    print(f"\n   Anti-inflammatory medicines: {len(inflammation_meds)} found")
    for med in inflammation_meds[:2]:
        print(f"   - {med.get('product_name', 'Unknown')}")
    
    # Search by disease
    diabetes_meds = search_by_disease("diabetes", limit=3)
    print(f"\n   Diabetes medicines: {len(diabetes_meds)} found")
    for med in diabetes_meds[:2]:
        print(f"   - {med.get('product_name', 'Unknown')}")


def gemini_integration_example():
    """Gemini Flash integration example."""
    
    print("\n🚀 Gemini Flash Integration Example")
    print("-" * 40)
    
    user_query = "What are the best traditional herbs for reducing inflammation?"
    
    # Get TradChem context
    context_data = llm_query(user_query, context_limit=3, include_smiles=False)
    
    # Format for Gemini prompt
    context_text = f"Traditional Medicine Database Context:\n"
    context_text += f"Database contains {context_data['database_context']['total_medicines']} medicines\n"
    context_text += f"Found {context_data['total_found']} relevant results:\n\n"
    
    for i, medicine in enumerate(context_data['context_data'], 1):
        context_text += f"{i}. {medicine['product_name']}\n"
        if medicine['traditional_system']:
            context_text += f"   System: {medicine['traditional_system']}\n"
        if medicine['benefits']:
            context_text += f"   Benefits: {', '.join(medicine['benefits'][:3])}\n"
        if medicine['diseases']:
            context_text += f"   Treats: {', '.join(medicine['diseases'][:3])}\n"
        context_text += "\n"
    
    gemini_prompt = f"""
You are a traditional medicine expert with access to a comprehensive database.

User Question: {user_query}

{context_text}

Please provide a detailed response based on the traditional medicine data above.
Include specific plant names, their benefits, and traditional usage when available.
"""
    
    print("📋 Generated Gemini Prompt:")
    print(gemini_prompt)
    
    # Return structured data for LLM use
    return {
        "user_query": user_query,
        "context_data": context_data,
        "gemini_prompt": gemini_prompt
    }


def chatbot_api_example():
    """Chatbot API integration example."""
    
    print("\n💬 Chatbot API Integration Example")
    print("-" * 40)
    
    def process_chatbot_query(user_message: str):
        """Process chatbot query using TradChem database."""
        
        # Use TradChem to get relevant information
        response = llm_query(user_message, context_limit=5)
        
        # Format as chatbot response
        if response['total_found'] > 0:
            chatbot_response = {
                "status": "success",
                "query": user_message,
                "traditional_medicine_data": response['context_data'],
                "database_info": response['database_context'],
                "suggestion": f"Found {response['total_found']} traditional medicines related to your query."
            }
        else:
            chatbot_response = {
                "status": "no_results",
                "query": user_message,
                "suggestion": "No traditional medicines found for this query. Try using different keywords."
            }
        
        return chatbot_response
    
    # Test queries
    test_queries = [
        "I need something for joint pain",
        "What can help with digestion?",
        "Traditional medicine for stress relief"
    ]
    
    for query in test_queries:
        print(f"\n🗨️  User: {query}")
        response = process_chatbot_query(query)
        print(f"   Status: {response['status']}")
        print(f"   Suggestion: {response['suggestion']}")
        
        if response['status'] == 'success' and response['traditional_medicine_data']:
            medicine = response['traditional_medicine_data'][0]
            print(f"   Top result: {medicine['product_name']}")


def export_for_llm():
    """Export data for LLM training."""
    
    print("\n📤 Exporting Data for LLM Training")
    print("-" * 40)
    
    # Get all data
    from tradchem import get_all_medicines
    
    all_medicines = get_all_medicines(include_smiles=False)
    
    # Create training data format
    training_data = []
    
    for medicine in all_medicines[:10]:  # Example first 10
        training_entry = {
            "medicine_name": medicine.get('product_name', ''),
            "traditional_system": medicine.get('traditional_system', ''),
            "benefits": medicine.get('benefits', []),
            "diseases": medicine.get('diseases', []),
            "geographic_origin": medicine.get('geographic_origin', ''),
            "sample_queries": [
                f"What are the benefits of {medicine.get('product_name', '')}?",
                f"How is {medicine.get('product_name', '')} used in traditional medicine?",
                f"What diseases does {medicine.get('product_name', '')} treat?"
            ]
        }
        training_data.append(training_entry)
    
    # Save as JSON
    with open('tradchem_llm_training_data.json', 'w', encoding='utf-8') as f:
        json.dump(training_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Exported {len(training_data)} training examples to 'tradchem_llm_training_data.json'")
    print("   This file can be used to train or fine-tune the LLM chatbot")


if __name__ == "__main__":
    # Run all examples
    main_integration_example()
    gemini_integration_example()
    chatbot_api_example()
    export_for_llm()
    
    print("\n🎉 Integration examples completed!")
    print("\n📚 Next Steps:")
    print("   1. Copy these functions to your Trad-Chem LLM chatbot")
    print("   2. Use llm_query() as the main integration point")
    print("   3. Customize the responses for your specific needs")
    print("   4. See: https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem-LLM") 