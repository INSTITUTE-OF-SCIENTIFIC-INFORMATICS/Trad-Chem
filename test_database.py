#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TradChem Database Test Script
Database functionality testing and validation

Author: Anu Gamage
"""

def main():
    """Test basic database functionality"""
    try:
        import tradchem
        
        # Test database loading
        print("Testing TradChem database...")
        
        # Get statistics
        stats = tradchem.get_database_stats()
        print(f"Database loaded successfully!")
        print(f"Total medicines: {stats['total_medicines']}")
        print(f"Version: {stats['version']}")
        
        # Test query functionality
        result = tradchem.llm_query("immunity", context_limit=2)
        print(f"Query test successful - Found {result['total_found']} results")
        
        print("All tests passed!")
        return True
        
    except Exception as e:
        print(f"Test failed: {e}")
        return False

if __name__ == "__main__":
    main() 