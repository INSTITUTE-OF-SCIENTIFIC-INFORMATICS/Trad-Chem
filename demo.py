#!/usr/bin/env python3
"""
TradChem Demo Script
Demonstrates the enhanced functionality of the TradChem library.
"""

import json
from tradchem import TradChem
from tradchem.utils.smiles_utils import validate_smiles, get_molecular_properties
from tradchem.utils.data_utils import DataImporter, DataExporter

def main():
    print("🌿 TradChem - Traditional Medicine Chemical Database Demo")
    print("=" * 60)
    
    # Initialize TradChem
    print("\n1. Initializing TradChem database...")
    tc = TradChem()
    
    # Show current database statistics
    print("\n2. Current Database Statistics:")
    stats = tc.get_statistics()
    for key, value in stats.items():
        if key != "last_updated":
            print(f"   {key.replace('_', ' ').title()}: {value}")
    
    # List current medicines
    print("\n3. Current Medicines in Database:")
    medicines = tc.list_medicines()
    for i, medicine in enumerate(medicines, 1):
        print(f"   {i}. {medicine}")
    
    # Demonstrate search functionality
    print("\n4. Search Functionality Demo:")
    search_results = tc.search_medicines("immunity", search_type="benefit")
    print(f"   Found {len(search_results)} medicines with 'immunity' benefits:")
    for medicine in search_results:
        print(f"   - {medicine['product_name']}")
    
    # Demonstrate SMILES validation
    print("\n5. SMILES Validation Demo:")
    test_smiles = "CC1=CC(=C(C=C1)O)C(=O)O"  # Curcumin
    is_valid = validate_smiles(test_smiles)
    print(f"   SMILES: {test_smiles}")
    print(f"   Valid: {'✓ Yes' if is_valid else '✗ No'}")
    
    if is_valid:
        properties = get_molecular_properties(test_smiles)
        if "error" not in properties:
            print(f"   Molecular Weight: {properties['molecular_weight']:.2f}")
            print(f"   LogP: {properties['logp']:.2f}")
    
    # Demonstrate adding a new medicine
    print("\n6. Adding New Medicine Demo:")
    new_medicine = {
        "product_name": "Demo Turmeric Extract",
        "benefits": ["Anti-inflammatory", "Antioxidant", "Demo purpose"],
        "diseases": ["Inflammation", "Demo condition"],
        "chemical_composition": {
            "ingredients": {
                "Curcumin": {
                    "primary_smiles": "CC1=CC(=C(C=C1)O)C(=O)O"
                },
                "Demethoxycurcumin": {
                    "primary_smiles": "CC1=CC(=C(C=C1)O)C(=O)O"
                }
            }
        }
    }
    
    if tc.add_medicine(new_medicine):
        print("   ✓ Successfully added demo medicine!")
    else:
        print("   ✗ Failed to add demo medicine")
    
    # Show updated statistics
    print("\n7. Updated Database Statistics:")
    updated_stats = tc.get_statistics()
    print(f"   Total Medicines: {updated_stats['total_medicines']}")
    
    # Demonstrate export functionality
    print("\n8. Export Functionality Demo:")
    export_success = tc.export_to_csv("demo_export.csv")
    if export_success:
        print("   ✓ Successfully exported database to demo_export.csv")
    else:
        print("   ✗ Failed to export database")
    
    # Demonstrate backup functionality
    print("\n9. Backup Functionality Demo:")
    backup_success = tc.backup_database()
    if backup_success:
        print("   ✓ Successfully created database backup")
    else:
        print("   ✗ Failed to create backup")
    
    # Show advanced search capabilities
    print("\n10. Advanced Search Demo:")
    print("   Searching by ingredient 'Cannabis':")
    cannabis_results = tc.search_medicines("Cannabis", search_type="ingredient")
    for medicine in cannabis_results:
        print(f"   - {medicine['product_name']}")
    
    print("\n   Searching by disease 'Fatigue':")
    fatigue_results = tc.search_medicines("Fatigue", search_type="disease")
    for medicine in fatigue_results:
        print(f"   - {medicine['product_name']}")
    
    # Demonstrate data import from the sample file
    print("\n11. Data Import Demo:")
    try:
        # Try to import from the sample CSV file
        sample_medicines = DataImporter.from_csv("examples/sample_medicines.csv")
        print(f"   ✓ Successfully loaded {len(sample_medicines)} medicines from sample file")
        
        # Show a few examples
        for i, medicine in enumerate(sample_medicines[:3], 1):
            print(f"   {i}. {medicine['product_name']}")
            print(f"      Benefits: {', '.join(medicine['benefits'][:2])}")
            print(f"      Ingredients: {', '.join(medicine['chemical_composition']['ingredients'].keys())}")
    except FileNotFoundError:
        print("   ⚠️  Sample file not found, skipping import demo")
    
    print("\n" + "=" * 60)
    print("🎉 Demo completed! TradChem is ready for your traditional medicine data.")
    print("\nNext steps:")
    print("1. Add your own medicine data using the CLI or Python API")
    print("2. Explore the documentation for advanced features")
    print("3. Contribute to the project by adding more traditional medicine data")
    print("4. Join the community discussions on GitHub")

if __name__ == "__main__":
    main() 