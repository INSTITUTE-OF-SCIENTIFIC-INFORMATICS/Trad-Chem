#!/usr/bin/env python3
"""
Simple test script for TradChem database and LLM integration

This script validates that the core functionality works correctly.
Run this after making changes to ensure everything still works.

Author: SaltyHeart
"""

def test_basic_imports():
    """Test if the main functions can be imported"""
    try:
        from tradchem import (
            llm_query, 
            get_database_stats, 
            search_by_benefits, 
            search_by_disease,
            search_by_system,
            TradChem
        )
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False


def test_database_loading():
    """Test if the database loads correctly"""
    try:
        from tradchem import TradChem
        tc = TradChem()
        
        if len(tc.data) > 0:
            print(f"✅ Database loaded with {len(tc.data)} medicines")
            return True
        else:
            print("❌ Database is empty")
            return False
            
    except Exception as e:
        print(f"❌ Database loading failed: {e}")
        return False


def test_llm_query():
    """Test the main LLM query function"""
    try:
        from tradchem import llm_query
        
        response = llm_query("turmeric", context_limit=3)
        
        required_keys = ['query', 'total_found', 'context_data', 'database_context']
        if all(key in response for key in required_keys):
            print(f"✅ LLM query works - found {response['total_found']} results")
            return True
        else:
            print("❌ LLM query response missing required keys")
            return False
            
    except Exception as e:
        print(f"❌ LLM query failed: {e}")
        return False


def test_database_stats():
    """Test database statistics function"""
    try:
        from tradchem import get_database_stats
        
        stats = get_database_stats()
        
        if stats['total_medicines'] > 0:
            print(f"✅ Database stats work - {stats['total_medicines']} medicines")
            return True
        else:
            print("❌ Database stats show 0 medicines")
            return False
            
    except Exception as e:
        print(f"❌ Database stats failed: {e}")
        return False


def test_search_functions():
    """Test the search functions"""
    try:
        from tradchem import search_by_benefits, search_by_disease, search_by_system
        
        # Test benefit search
        benefit_results = search_by_benefits("inflammation", limit=5)
        
        # Test disease search
        disease_results = search_by_disease("arthritis", limit=5)
        
        # Test system search
        system_results = search_by_system("ayurveda", limit=5)
        
        print(f"✅ Search functions work:")
        print(f"   - Benefits: {len(benefit_results)} results")
        print(f"   - Diseases: {len(disease_results)} results") 
        print(f"   - Systems: {len(system_results)} results")
        return True
        
    except Exception as e:
        print(f"❌ Search functions failed: {e}")
        return False


def run_all_tests():
    """Run all tests and report results"""
    
    print("🧪 TradChem Database Test Suite")
    print("=" * 40)
    
    tests = [
        ("Basic Imports", test_basic_imports),
        ("Database Loading", test_database_loading),
        ("LLM Query Function", test_llm_query),
        ("Database Statistics", test_database_stats),
        ("Search Functions", test_search_functions)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing {test_name}...")
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ Test {test_name} crashed: {e}")
            failed += 1
    
    print(f"\n📊 Test Results")
    print("=" * 20)
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"📈 Success Rate: {passed/(passed+failed)*100:.1f}%")
    
    if failed == 0:
        print("\n🎉 All tests passed! TradChem database is ready for LLM integration!")
        print("\n📚 Next steps:")
        print("   1. Use llm_query() in your Trad-Chem LLM chatbot")
        print("   2. See INTEGRATION_EXAMPLE.py for usage examples")
        print("   3. Visit: https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem-LLM")
    else:
        print(f"\n⚠️  {failed} test(s) failed. Please fix the issues above.")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1) 