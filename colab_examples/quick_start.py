#!/usr/bin/env python3
"""
TradChem Quick Start Script for Google Colab

This script provides a quick way to get started with TradChem in Google Colab.
Run this in a Colab cell to install and demonstrate basic functionality.
"""

import subprocess
import sys
import os
from pathlib import Path

def install_tradchem():
    """Install TradChem package."""
    print("🚀 Installing TradChem...")
    
    # Install core dependencies
    dependencies = [
        "tradchem",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0", 
        "seaborn>=0.11.0",
        "numpy>=1.21.0"
    ]
    
    for dep in dependencies:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
            print(f"✅ Installed {dep}")
        except subprocess.CalledProcessError:
            print(f"⚠️  Failed to install {dep}")
    
    return True

def demonstrate_basic_usage():
    """Demonstrate basic TradChem functionality."""
    print("\n🌿 TradChem Basic Usage Demonstration")
    print("=" * 50)
    
    try:
        from tradchem import TradChem
        import pandas as pd
        import matplotlib.pyplot as plt
        
        # Initialize
        print("📊 Loading TradChem database...")
        tc = TradChem()
        
        # Get statistics
        stats = tc.get_statistics()
        print(f"✅ Database loaded: {stats['total_medicines']} medicines found")
        
        # Search example
        print("\n🔍 Searching for 'turmeric':")
        results = tc.search_medicines("turmeric", limit=3)
        for i, medicine in enumerate(results, 1):
            print(f"{i}. {medicine['product_name']}")
            if medicine.get('scientific_name'):
                print(f"   Scientific: {medicine['scientific_name']}")
        
        # Get detailed info
        print("\n📋 Getting detailed information:")
        medicine = tc.get_medicine("ashwagandha")
        if medicine:
            print(f"Medicine: {medicine['product_name']}")
            print(f"System: {medicine.get('traditional_system', 'N/A')}")
            if medicine.get('benefits'):
                print(f"Benefits: {', '.join(medicine['benefits'][:3])}")
        
        # Export data
        print("\n📤 Exporting data to DataFrame:")
        data = tc.export_data(format="json")
        df = pd.DataFrame(data)
        print(f"DataFrame shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        
        # Basic visualization
        print("\n📈 Creating basic visualization:")
        plt.figure(figsize=(10, 6))
        
        # Plot medicine count by system
        if 'traditional_system' in df.columns:
            system_counts = df['traditional_system'].value_counts()
            plt.bar(system_counts.index, system_counts.values, color='#2E8B57')
            plt.title('Medicines by Traditional System')
            plt.xlabel('Traditional System')
            plt.ylabel('Number of Medicines')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        
        print("\n🎉 Basic demonstration completed!")
        return True
        
    except Exception as e:
        print(f"❌ Demonstration failed: {e}")
        return False

def demonstrate_chemical_analysis():
    """Demonstrate chemical analysis capabilities."""
    print("\n🧪 Chemical Analysis Demonstration")
    print("=" * 40)
    
    try:
        # Install RDKit if not available
        try:
            from rdkit import Chem
            print("✅ RDKit already available")
        except ImportError:
            print("📦 Installing RDKit...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "rdkit-pypi"])
            from rdkit import Chem
            print("✅ RDKit installed")
        
        from tradchem import TradChem
        from rdkit.Chem import Descriptors
        
        tc = TradChem()
        
        # Find compounds with SMILES
        print("🔬 Analyzing chemical compounds...")
        compounds_with_smiles = []
        
        for medicine in tc.data:
            chem_comp = medicine.get('chemical_composition', {})
            ingredients = chem_comp.get('ingredients', {})
            
            for ingredient, details in ingredients.items():
                if isinstance(details, dict) and details.get('smiles'):
                    compounds_with_smiles.append({
                        'medicine': medicine['product_name'],
                        'ingredient': ingredient,
                        'smiles': details['smiles']
                    })
        
        print(f"Found {len(compounds_with_smiles)} compounds with SMILES notation")
        
        # Analyze a few compounds
        if compounds_with_smiles:
            print("\n📊 Molecular Properties:")
            for compound in compounds_with_smiles[:3]:  # Show first 3
                mol = Chem.MolFromSmiles(compound['smiles'])
                if mol:
                    mw = Descriptors.MolWt(mol)
                    logp = Descriptors.MolLogP(mol)
                    print(f"• {compound['ingredient']} (from {compound['medicine']})")
                    print(f"  MW: {mw:.1f}, LogP: {logp:.2f}")
        
        print("\n✅ Chemical analysis demonstration completed!")
        return True
        
    except Exception as e:
        print(f"❌ Chemical analysis failed: {e}")
        return False

def show_usage_examples():
    """Show usage examples."""
    print("\n📖 Usage Examples")
    print("=" * 30)
    
    examples = """
# Basic Usage
from tradchem import TradChem
tc = TradChem()

# Search medicines
results = tc.search_medicines("turmeric")
medicine = tc.get_medicine("ashwagandha")

# Get statistics
stats = tc.get_statistics()

# Export data
data = tc.export_data(format="json")
df = pd.DataFrame(data)

# Chemical Analysis (with RDKit)
from rdkit import Chem
from rdkit.Chem import Descriptors

# Analyze SMILES
smiles = "CC1=CC(=C(C=C1)O)C(=O)O"  # Curcumin
mol = Chem.MolFromSmiles(smiles)
mw = Descriptors.MolWt(mol)
logp = Descriptors.MolLogP(mol)

# CLI Usage
!tradchem search "turmeric"
!tradchem stats
!tradchem export --format csv
"""
    
    print(examples)

def main():
    """Main function."""
    print("🌿 TradChem Quick Start for Google Colab")
    print("=" * 50)
    
    # Install package
    if not install_tradchem():
        print("❌ Installation failed")
        return
    
    # Demonstrate basic usage
    if not demonstrate_basic_usage():
        print("❌ Basic usage demonstration failed")
        return
    
    # Demonstrate chemical analysis
    demonstrate_chemical_analysis()
    
    # Show usage examples
    show_usage_examples()
    
    print("\n" + "=" * 50)
    print("🎉 Quick Start Complete!")
    print("\n📚 Next steps:")
    print("1. Explore the full notebooks in colab_examples/")
    print("2. Try the CLI: !tradchem stats")
    print("3. Analyze your own data")
    print("4. Contribute to the database")
    print("\n🔗 Resources:")
    print("- GitHub: https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem")
    print("- Documentation: Check README.md")
    print("- Examples: Explore colab_examples/")

if __name__ == "__main__":
    main() 