#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TradChem Integration Example
Example integration with Gemini Flash LLM for traditional medicine queries

Author: Anu Gamage
"""

import tradchem
import json

def demonstrate_llm_integration():
    """Demonstrate how to integrate TradChem with LLM"""
    
    print("TradChem LLM Integration Example")
    print("=" * 40)
    
    # Example 1: Search for immunity boosters
    print("\n1. Searching for immunity boosters...")
    immunity_results = tradchem.llm_query("immunity boost", context_limit=3)
    
    print(f"Found {immunity_results['total_found']} relevant medicines:")
    for medicine in immunity_results['context_data']:
        print(f"  - {medicine['product_name']}")
        print(f"    Benefits: {', '.join(medicine['benefits'][:2])}")
        print(f"    Relevance Score: {medicine['relevance_score']}")
    
    # Example 2: Search by disease
    print("\n2. Searching for fatigue treatments...")
    fatigue_results = tradchem.search_by_disease("fatigue")
    
    for medicine in fatigue_results[:2]:
        print(f"  - {medicine['product_name']}")
        if 'traditional_system' in medicine:
            print(f"    System: {medicine['traditional_system']}")
    
    # Example 3: Get database statistics
    print("\n3. Database Statistics:")
    stats = tradchem.get_database_stats()
    print(f"  Total Medicines: {stats['total_medicines']}")
    print(f"  Traditional Systems: {stats['traditional_systems']}")
    
    # Example 4: Format for LLM context
    print("\n4. Sample LLM Context (JSON format):")
    context_data = tradchem.llm_query("energy", context_limit=1, include_smiles=False)
    print(json.dumps(context_data, indent=2))

def gemini_integration_example():
    """Example of how this could be used with Gemini Flash"""
    
    print("\n" + "=" * 50)
    print("Example Gemini Flash Integration")
    print("=" * 50)
    
    # Simulate user query
    user_query = "What traditional medicines can help with low energy?"
    
    # Get relevant context from TradChem
    context = tradchem.llm_query("energy vitality", context_limit=3, include_smiles=False)
    
    # Format context for LLM prompt
    context_text = ""
    for medicine in context['context_data']:
        context_text += f"Medicine: {medicine['product_name']}\n"
        context_text += f"Benefits: {', '.join(medicine['benefits'])}\n"
        context_text += f"System: {medicine.get('traditional_system', 'Unknown')}\n\n"
    
    # Example prompt construction
    prompt = f"""
Based on the following traditional medicine database information:

{context_text}

User Question: {user_query}

Please provide a helpful response about traditional medicines for low energy, 
including specific recommendations from the database.
"""
    
    print("Generated prompt for Gemini Flash:")
    print("-" * 30)
    print(prompt)
    print("-" * 30)

if __name__ == "__main__":
    demonstrate_llm_integration()
    gemini_integration_example() 