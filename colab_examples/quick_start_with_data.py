#!/usr/bin/env python3
"""
TradChem Quick Start with Sample Data

This script creates sample traditional medicine data and demonstrates
how to use TradChem for analysis.
"""

import json
import pandas as pd
import os
from tradchem import TradChem

def create_sample_data():
    """Create sample traditional medicine data."""
    
    # Sample data
    sample_medicines = [
        {
            "product_name": "Turmeric Extract",
            "scientific_name": "Curcuma longa",
            "description": "Traditional anti-inflammatory herb",
            "traditional_system": "Ayurveda",
            "geographic_origin": "India",
            "benefits": ["Anti-inflammatory", "Antioxidant", "Digestive aid"],
            "diseases": ["Arthritis", "Digestive disorders"],
            "chemical_composition": {
                "ingredients": {
                    "Curcumin": {
                        "smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
                        "molecular_weight": 368.38,
                        "formula": "C21H20O6"
                    }
                }
            }
        },
        {
            "product_name": "Ashwagandha Root",
            "scientific_name": "Withania somnifera",
            "description": "Adaptogenic herb for stress relief",
            "traditional_system": "Ayurveda",
            "geographic_origin": "India",
            "benefits": ["Stress relief", "Energy boost", "Immune support"],
            "diseases": ["Anxiety", "Fatigue", "Stress"],
            "chemical_composition": {
                "ingredients": {
                    "Withanolides": {
                        "smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
                        "molecular_weight": 470.6,
                        "formula": "C28H38O6"
                    }
                }
            }
        },
        {
            "product_name": "Ginger Root",
            "scientific_name": "Zingiber officinale",
            "description": "Traditional digestive aid",
            "traditional_system": "TCM",
            "geographic_origin": "China",
            "benefits": ["Digestive aid", "Anti-nausea", "Anti-inflammatory"],
            "diseases": ["Nausea", "Digestive disorders", "Motion sickness"],
            "chemical_composition": {
                "ingredients": {
                    "Gingerol": {
                        "smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
                        "molecular_weight": 294.4,
                        "formula": "C17H26O4"
                    }
                }
            }
        },
        {
            "product_name": "Ginseng Root",
            "scientific_name": "Panax ginseng",
            "description": "Energy and vitality herb",
            "traditional_system": "TCM",
            "geographic_origin": "China",
            "benefits": ["Energy boost", "Immune support", "Stress relief"],
            "diseases": ["Fatigue", "Low energy", "Stress"],
            "chemical_composition": {
                "ingredients": {
                    "Ginsenosides": {
                        "smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
                        "molecular_weight": 800.0,
                        "formula": "C42H72O14"
                    }
                }
            }
        },
        {
            "product_name": "Echinacea Purpurea",
            "scientific_name": "Echinacea purpurea",
            "description": "Immune system support",
            "traditional_system": "Western Herbalism",
            "geographic_origin": "North America",
            "benefits": ["Immune support", "Cold prevention", "Anti-inflammatory"],
            "diseases": ["Colds", "Flu", "Immune weakness"],
            "chemical_composition": {
                "ingredients": {
                    "Echinacoside": {
                        "smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
                        "molecular_weight": 786.7,
                        "formula": "C35H46O20"
                    }
                }
            }
        }
    ]
    
    # Create CSV file
    csv_data = []
    for medicine in sample_medicines:
        csv_row = {
            'product_name': medicine['product_name'],
            'scientific_name': medicine['scientific_name'],
            'description': medicine['description'],
            'traditional_system': medicine['traditional_system'],
            'geographic_origin': medicine['geographic_origin'],
            'benefits': ', '.join(medicine['benefits']),
            'diseases': ', '.join(medicine['diseases']),
            'chemical_composition': json.dumps(medicine['chemical_composition'])
        }
        csv_data.append(csv_row)
    
    # Save CSV file
    df = pd.DataFrame(csv_data)
    df.to_csv('medicines.csv', index=False)
    print("✅ Created medicines.csv")
    
    # Save JSON file
    with open('medicines.json', 'w', encoding='utf-8') as f:
        json.dump(sample_medicines, f, indent=2, ensure_ascii=False)
    print("✅ Created medicines.json")
    
    return sample_medicines

def demonstrate_tradchem():
    """Demonstrate TradChem functionality with sample data."""
    
    print("\n🌿 TradChem Demonstration")
    print("=" * 40)
    
    # Initialize TradChem
    tc = TradChem()
    print("✅ TradChem initialized")
    
    # Load data
    try:
        medicines = tc.load_data('medicines.csv')
        print(f"✅ Loaded {len(medicines)} medicines from CSV")
    except FileNotFoundError:
        print("❌ medicines.csv not found, creating sample data...")
        medicines = create_sample_data()
        medicines = tc.load_data('medicines.csv')
        print(f"✅ Loaded {len(medicines)} medicines from CSV")
    
    # Validate data
    print("\n📊 Data Validation:")
    validation = tc.validate_data(medicines)
    print(f"  Total medicines: {validation['total_medicines']}")
    print(f"  Valid medicines: {validation['valid_medicines']}")
    print(f"  Invalid medicines: {validation['invalid_medicines']}")
    print(f"  Data quality score: {validation['data_quality_score']:.2%}")
    
    # Search medicines
    print("\n🔍 Search Functionality:")
    results = tc.search_medicines("turmeric", limit=3)
    print(f"  Found {len(results)} results for 'turmeric'")
    for medicine in results:
        print(f"    - {medicine['product_name']}")
    
    # Chemical analysis
    print("\n🧪 Chemical Analysis:")
    chemical_analysis = tc.analyze_chemical_structures(medicines)
    print(f"  Total compounds: {chemical_analysis['total_compounds']}")
    print(f"  Valid SMILES: {chemical_analysis['valid_smiles']}")
    print(f"  Invalid SMILES: {chemical_analysis['invalid_smiles']}")
    print(f"  Average molecular weight: {chemical_analysis['avg_molecular_weight']:.2f}")
    print(f"  Unique formulas: {chemical_analysis['unique_formulas']}")
    
    # Statistical analysis
    print("\n📈 Statistical Analysis:")
    stats = tc.statistical_analysis(medicines)
    print(f"  Total medicines: {stats['total_medicines']}")
    print(f"  Unique systems: {stats['unique_systems']}")
    print(f"  Unique regions: {stats['unique_regions']}")
    print(f"  Average benefits per medicine: {stats['avg_benefits_per_medicine']:.2f}")
    print(f"  Compounds with SMILES: {stats['compounds_with_smiles']}")
    
    # System distribution
    print("\n🏥 Traditional Medicine Systems:")
    for system, count in stats['system_distribution'].items():
        print(f"  {system}: {count}")
    
    # Region distribution
    print("\n🌍 Geographic Distribution:")
    for region, count in stats['region_distribution'].items():
        print(f"  {region}: {count}")
    
    print("\n🎉 TradChem demonstration complete!")
    print("\n📁 Files created:")
    print("  - medicines.csv (CSV format)")
    print("  - medicines.json (JSON format)")
    
    return medicines

if __name__ == "__main__":
    # Run demonstration
    medicines = demonstrate_tradchem()
    
    print("\n📖 Next Steps:")
    print("1. Explore the created data files")
    print("2. Try different search queries")
    print("3. Experiment with data validation")
    print("4. Create your own medicine data")
    print("5. Check out the tutorials in colab_examples/") 