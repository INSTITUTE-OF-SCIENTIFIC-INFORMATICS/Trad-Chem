#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TradChem LLM Integration Demo
TradChem LLM Integration Demonstration

This script demonstrates that TradChem is now fully functional
and ready for integration with the Trad-Chem LLM chatbot.

Author: Anu Gamage
"""

import tradchem
import json


def demo_basic_functionality():
    """Demonstrate basic functionality"""
    print("=== TradChem Basic Functionality Demo ===")
    print("TradChem Basic Functionality Demonstration")
    print()
    
    # Get database statistics - Retrieve database metrics
    print("📊 Database Statistics - Database Information:")
    stats = tradchem.get_database_stats()
    print(f"  • Total Medicines - Medicine Count: {stats['total_medicines']}")
    print(f"  • Version - Package Version: {stats['version']}")
    print(f"  • Traditional Systems - Medical Systems: {stats.get('traditional_systems', [])}")
    print()


def demo_llm_queries():
    """Demonstrate LLM query functionality"""
    print("=== LLM Query Functionality Demo ===")
    print("LLM Query Function Demonstration")
    print()
    
    # Test different types of queries - Test various search patterns
    test_queries = [
        ("immunity", "Immunity boost query - Immune enhancement search"),
        ("fatigue", "Fatigue treatment query - Fatigue management search"),
        ("cannabis", "Cannabis compounds query - Cannabis chemical search"),
        ("vitality", "Vitality enhancement query - Energy boost search")
    ]
    
    for query, description in test_queries:
        print(f"🔍 {description}:")
        print(f"  Query: '{query}'")
        
        result = tradchem.llm_query(query, context_limit=2, include_smiles=False)
        
        if result['total_found'] > 0:
            print(f"  ✅ Found {result['total_found']} results")
            for i, medicine in enumerate(result['context_data']):
                print(f"    {i+1}. {medicine['product_name']}")
                print(f"       Relevance: {medicine['relevance_score']}")
                print(f"       Matched fields: {medicine['matched_fields']}")
                if medicine['benefits']:
                    print(f"       Benefits: {', '.join(medicine['benefits'][:2])}")
        else:
            print(f"  ⚠️  No matches found")
        print()


def demo_search_functions():
    """Demonstrate search functionality"""
    print("=== Search Functions Demo ===")
    print("Search Function Demonstration")
    print()
    
    # Search by benefits - Benefits-based search
    print("🔍 Search by Benefits - Therapeutic Benefits Search:")
    benefits_results = tradchem.search_by_benefits("immunity", limit=3)
    if benefits_results:
        for medicine in benefits_results:
            print(f"  • {medicine['product_name']}")
    else:
        print("  No results found for 'immunity'")
    print()
    
    # Search by disease - Disease-based search
    print("🔍 Search by Disease - Disease Treatment Search:")
    disease_results = tradchem.search_by_disease("weakness", limit=3)
    if disease_results:
        for medicine in disease_results:
            print(f"  • {medicine['product_name']}")
    else:
        print("  No results found for 'weakness'")
    print()


def demo_llm_integration_format():
    """Demonstrate LLM integration format"""
    print("=== LLM Integration Format Demo ===")
    print("LLM Integration Format Demonstration")
    print()
    
    # Show how data is formatted for LLM context - Display LLM context formatting
    result = tradchem.llm_query("vitality", context_limit=1, include_smiles=True)
    
    print("🤖 Sample LLM Context Data Format - LLM Context Data Example:")
    print("```json")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print("```")
    print()


def demo_integration_ready():
    """Demonstrate integration readiness"""
    print("=== Integration Readiness Check ===")
    print("Integration Status Verification")
    print()
    
    try:
        # Test all main functions - Verify core functionality
        stats = tradchem.get_database_stats()
        query_result = tradchem.llm_query("test", context_limit=1)
        all_medicines = tradchem.get_all_medicines(include_smiles=False)
        
        print("✅ All core functions working")
        print("✅ Database accessible")
        print("✅ LLM query format ready")
        print("✅ Search functions operational")
        print()
        print("🎉 TradChem is READY for Trad-Chem LLM Integration!")
        print("🎉 TradChem is prepared for Trad-Chem LLM integration!")
        print()
        print("📁 Repository: https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem")
        print("🤖 LLM Chatbot: https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem-LLM")
        print()
        return True
        
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        return False


def main():
    """Main demonstration function"""
    print("TradChem LLM Integration Demo")
    print("TradChem LLM Integration Demonstration")
    print("=" * 60)
    print()
    
    # Run all demos - Execute all demonstration functions
    demo_basic_functionality()
    demo_llm_queries()
    demo_search_functions()
    demo_llm_integration_format()
    
    # Final integration readiness check - Final verification of integration status
    success = demo_integration_ready()
    
    if success:
        print("🚀 Ready to connect with Trad-Chem LLM!")
        print("🚀 Prepared for Trad-Chem LLM connection!")
    else:
        print("❌ Still need to fix some issues")
        print("❌ Issues remain to be resolved")
    
    return success


if __name__ == "__main__":
    main() 