#!/usr/bin/env python3
"""
TradChem LLM Integration Example

Simple example showing how to use TradChem database with LLM chatbots.
Author: SaltyHeart
"""

from tradchem import llm_query, get_database_stats, search_by_benefits


def main():
    """Main example demonstrating LLM integration functions."""
    
    print("TradChem Database - LLM Integration Example")
    print("=" * 50)
    
    # 1. Get database overview
    print("\n1. Database Overview:")
    stats = get_database_stats()
    print(f"   Total medicines: {stats['total_medicines']}")
    print(f"   Version: {stats['version']}")
    
    # 2. Simple LLM query
    print("\n2. LLM Query Example:")
    query = "turmeric anti-inflammatory"
    response = llm_query(query, context_limit=3)
    
    print(f"   Query: '{query}'")
    print(f"   Results found: {response['total_found']}")
    
    for i, medicine in enumerate(response['context_data'], 1):
        print(f"   {i}. {medicine['product_name']}")
        if medicine.get('benefits'):
            print(f"      Benefits: {', '.join(medicine['benefits'][:2])}")
    
    # 3. Search by benefits
    print("\n3. Search by Benefits:")
    anti_inflammatory = search_by_benefits("inflammation", limit=3)
    print(f"   Found {len(anti_inflammatory)} anti-inflammatory medicines")
    
    for med in anti_inflammatory[:2]:
        print(f"   - {med.get('product_name', 'Unknown')}")
    
    print("\n✅ Example completed!")
    print("   Use these functions in your Trad-Chem LLM chatbot.")


if __name__ == "__main__":
    main() 