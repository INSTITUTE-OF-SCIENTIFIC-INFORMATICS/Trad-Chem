#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Anu Gamage
LLM Integration Example for TradChem
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tradchem

def main():
    """Example usage of TradChem with LLM integration"""
    
    # Basic query example
    result = tradchem.llm_query("immunity", context_limit=2)
    print(f"Found {result['total_found']} medicines for immunity")
    
    for medicine in result['context_data']:
        print(f"- {medicine['product_name']}")
        print(f"  Benefits: {', '.join(medicine['benefits'])}")

if __name__ == "__main__":
    main() 