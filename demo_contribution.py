#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TradChem Data Contribution Demo Script
Demonstrates how to add traditional medicine data to the TradChem database

Author: SaltyHeart
"""

import json
import csv
from pathlib import Path
from tradchem.tradchem import TradChem
from tradchem.utils.smiles_utils import validate_smiles

def demo_csv_contribution():
    """Demonstrate CSV format data contribution"""
    print("🌿 Demonstrating CSV Format Data Contribution")
    print("=" * 50)
    
    # Create sample data
    sample_data = [
        {
            "product_name": "Turmeric Extract",
            "benefits": "Anti-inflammatory; Antioxidant; Digestive support; Immune enhancement",
            "diseases": "Inflammation; Arthritis; Digestive issues; Weak immune system",
            "ingredients": "Turmeric; Curcumin; Demethoxycurcumin",
            "smiles": "CC1=CC(=C(C=C1)O)C(=O)O; CC1=CC(=C(C=C1)O)C(=O)O; CC1=CC(=C(C=C1)O)C(=O)O",
            "source": "Traditional Ayurvedic literature, DOI: 10.1000/curcumin_study",
            "traditional_system": "Ayurvedic Medicine",
            "description": "Turmeric has been used in Ayurvedic medicine for thousands of years, with anti-inflammatory and digestive support properties."
        },
        {
            "product_name": "Ginseng Root Extract",
            "benefits": "Energy boost; Immune enhancement; Anti-aging; Adaptogen",
            "diseases": "Fatigue; Weak immune system; Aging; Stress",
            "ingredients": "Ginseng; Ginsenosides; Rb1; Rg1",
            "smiles": "CC1=CC(=C(C=C1)O)C(=O)O; CC1=CC(=C(C=C1)O)C(=O)O; CC1=CC(=C(C=C1)O)C(=O)O; CC1=CC(=C(C=C1)O)C(=O)O",
            "source": "Shennong Ben Cao Jing, DOI: 10.1000/ginseng_study",
            "traditional_system": "Traditional Chinese Medicine",
            "description": "Ginseng is one of the most revered herbs in Traditional Chinese Medicine, considered a powerful adaptogen."
        }
    ]
    
    # Write to CSV file
    csv_file = "contributions/demo_contribution.csv"
    Path("contributions").mkdir(exist_ok=True)
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=sample_data[0].keys())
        writer.writeheader()
        writer.writerows(sample_data)
    
    print(f"✅ Created sample CSV file: {csv_file}")
    print("📋 CSV format is suitable for batch data contribution")
    print()

def demo_json_contribution():
    """Demonstrate JSON format data contribution"""
    print("🌿 Demonstrating JSON Format Data Contribution")
    print("=" * 50)
    
    # Create sample JSON data
    sample_json = {
        "medicines": [
            {
                "product_name": "Ashwagandha (Withania somnifera)",
                "benefits": [
                    "Stress reduction",
                    "Energy boost",
                    "Immune enhancement",
                    "Adaptogenic effects"
                ],
                "diseases": [
                    "Stress",
                    "Anxiety",
                    "Fatigue",
                    "Weak immune system"
                ],
                "chemical_composition": {
                    "ingredients": {
                        "Ashwagandha": {
                            "primary_smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
                            "molecular_weight": 470.6,
                            "bioavailability": "Low"
                        },
                        "Withanolide": {
                            "primary_smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
                            "molecular_weight": 470.6,
                            "bioavailability": "Low"
                        }
                    }
                },
                "source": "Charaka Samhita, DOI: 10.1000/ashwagandha_study",
                "traditional_system": "Ayurvedic Medicine",
                "description": "Ashwagandha is an adaptogenic herb that helps the body adapt to stress.",
                "dosage_info": "300-600mg daily, usually taken with milk",
                "contraindications": "May affect thyroid function, use with caution during pregnancy",
                "geographic_origin": "India",
                "harvesting_season": "Winter (December-February)"
            }
        ],
        "metadata": {
            "contributor": "Demo Contributor",
            "contribution_date": "2024-01-01",
            "data_version": "1.0",
            "quality_check": "Completed",
            "sources_verified": True,
            "smiles_validated": True
        }
    }
    
    # Write to JSON file
    json_file = "contributions/demo_contribution.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(sample_json, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Created sample JSON file: {json_file}")
    print("📋 JSON format is suitable for structured data contribution")
    print()

def demo_smiles_validation():
    """Demonstrate SMILES validation"""
    print("🧪 Demonstrating SMILES Validation")
    print("=" * 50)
    
    # Test SMILES
    test_smiles = [
        "CC1=CC(=C(C=C1)O)C(=O)O",  # Curcumin
        "CC(C)(C)CC1=CC(=C(C=C1)O)C(=O)O",  # Gingerol
        "CN1C=NC2=C1C(=O)N(C(=O)N2C)C",  # Caffeine
        "INVALID_SMILES"  # Invalid SMILES
    ]
    
    for smiles in test_smiles:
        try:
            is_valid = validate_smiles(smiles)
            status = "✅ Valid" if is_valid else "❌ Invalid"
            print(f"SMILES: {smiles}")
            print(f"Status: {status}")
            print()
        except Exception as e:
            print(f"SMILES: {smiles}")
            print(f"Error: {e}")
            print()

def demo_database_integration():
    """Demonstrate database integration"""
    print("🗄️ Demonstrating Database Integration")
    print("=" * 50)
    
    try:
        # Initialize TradChem database
        tc = TradChem()
        
        # Add sample medicine
        medicine_data = {
            "product_name": "Demo Medicine",
            "benefits": ["Demo benefit 1", "Demo benefit 2"],
            "diseases": ["Demo disease 1", "Demo disease 2"],
            "chemical_composition": {
                "ingredients": {
                    "Demo ingredient": {
                        "primary_smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
                        "molecular_weight": 300.0
                    }
                }
            },
            "source": "Demo source",
            "traditional_system": "Demo medical system"
        }
        
        # Add to database
        result = tc.add_medicine(medicine_data)
        print(f"✅ Medicine addition result: {result}")
        
        # Search medicine
        search_result = tc.search_medicines("Demo Medicine")
        print(f"🔍 Search results: {len(search_result)} matches")
        
        # Get statistics
        stats = tc.get_statistics()
        print(f"📊 Database statistics: {stats}")
        
    except Exception as e:
        print(f"❌ Database operation error: {e}")

def demo_contribution_workflow():
    """Demonstrate complete contribution workflow"""
    print("🔄 Demonstrating Complete Contribution Workflow")
    print("=" * 50)
    
    print("1. 📋 Prepare data")
    print("   - Research traditional medicine information")
    print("   - Collect reliable reference sources")
    print("   - Validate SMILES molecular structures")
    print()
    
    print("2. 📝 Choose contribution method")
    print("   - Web interface: Simplest method")
    print("   - CSV template: Suitable for batch data")
    print("   - JSON format: Developer-friendly")
    print("   - GitHub Issues: Quick contribution")
    print()
    
    print("3. ✅ Data validation")
    print("   - Validate SMILES format")
    print("   - Check data completeness")
    print("   - Confirm source reliability")
    print()
    
    print("4. 📤 Submit contribution")
    print("   - Create Pull Request")
    print("   - Fill in detailed description")
    print("   - Wait for community review")
    print()
    
    print("5. 🎉 Contribution completed")
    print("   - Data integrated into database")
    print("   - Receive contributor recognition")
    print("   - Help preserve traditional medicine knowledge")
    print()

def main():
    """Main function"""
    print("🌿 TradChem Data Contribution Demo")
    print("=" * 60)
    print("This demo shows how to contribute traditional medicine data to the TradChem database")
    print("Author: SaltyHeart")
    print()
    
    # Run various demos
    demo_csv_contribution()
    demo_json_contribution()
    demo_smiles_validation()
    demo_database_integration()
    demo_contribution_workflow()
    
    print("🎯 Contribution Guide Summary")
    print("=" * 50)
    print("📊 Data contribution methods:")
    print("   - Web interface: Visit the app to add data")
    print("   - CSV template: Download template and fill in data")
    print("   - JSON format: Structured data format")
    print("   - GitHub Issues: Use Issue template")
    print()
    print("📋 Data quality requirements:")
    print("   - Accurate and verifiable information")
    print("   - Correct SMILES molecular structures")
    print("   - Reliable and cited sources")
    print("   - Complete and comprehensive data")
    print()
    print("🔬 SMILES validation:")
    print("   - Use validated molecular structures")
    print("   - Include molecular weight when possible")
    print("   - Provide bioavailability information")
    print()
    print("📚 Traditional medicine systems supported:")
    print("   - Ayurvedic Medicine")
    print("   - Traditional Chinese Medicine")
    print("   - Unani Medicine")
    print("   - African Traditional Medicine")
    print("   - Indigenous Medicine")
    print()
    print("🌿 Thank you for contributing to traditional medicine knowledge preservation!")
    print("Your contributions help protect and share valuable traditional medicine wisdom.")

if __name__ == "__main__":
    main() 