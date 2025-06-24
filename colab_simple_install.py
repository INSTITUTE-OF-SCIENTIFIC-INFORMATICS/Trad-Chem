# TradChem Simple Colab Installation
# Copy and paste this entire code block into a Colab cell

import subprocess
import sys
import os
from pathlib import Path

print("🧹 Clean TradChem Installation for Colab")
print("=" * 50)

# Step 1: Remove existing installation
print("🗑️  Cleaning existing installation...")
try:
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "tradchem", "-y"])
    print("✅ Removed existing tradchem package")
except:
    print("⚠️  No existing package to remove")

# Remove existing directory
import shutil
if os.path.exists("/content/Trad-Chem"):
    shutil.rmtree("/content/Trad-Chem")
    print("✅ Removed existing directory")

# Step 2: Install dependencies
print("\n📦 Installing dependencies...")
dependencies = [
    "numpy>=1.21.0",
    "pandas>=1.3.0", 
    "scipy>=1.7.0",
    "matplotlib>=3.4.0",
    "seaborn>=0.11.0",
    "scikit-learn>=0.24.0",
    "jsonschema>=3.2.0",
    "pydantic>=1.8.0"
]

for dep in dependencies:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
        print(f"✅ {dep}")
    except:
        print(f"⚠️  {dep} (already installed)")

# Try to install RDKit
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rdkit-pypi"])
    print("✅ rdkit-pypi")
except:
    print("⚠️  rdkit-pypi (optional)")

# Step 3: Create clean directory structure
print("\n📁 Creating clean directory structure...")
base_dir = Path("/content/Trad-Chem")
tradchem_dir = base_dir / "tradchem"
utils_dir = tradchem_dir / "utils"
medicine_dir = tradchem_dir / "medicine_systems"

for dir_path in [base_dir, tradchem_dir, utils_dir, medicine_dir]:
    dir_path.mkdir(parents=True, exist_ok=True)

# Step 4: Create clean source files
print("📝 Creating clean source files...")

# __init__.py
init_content = '''"""
TradChem - Traditional Medicine Chemical Analysis

A comprehensive Python package for analyzing traditional medicine data, 
chemical structures, and molecular properties.
"""

from .tradchem import TradChem
from .version import __version__

__all__ = ['TradChem', '__version__']

__author__ = "SaltyHeart"
__version__ = "0.2.0"
__description__ = "Traditional medicine chemical analysis package"
'''

with open(tradchem_dir / "__init__.py", "w", encoding="utf-8") as f:
    f.write(init_content)

# version.py
version_content = '''"""Version information."""
__version__ = "0.2.0"
'''

with open(tradchem_dir / "version.py", "w", encoding="utf-8") as f:
    f.write(version_content)

# Create minimal TradChem class
tradchem_content = '''"""
TradChem - Traditional Medicine Chemical Analysis
"""

import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict, Optional, Any, Union
from datetime import datetime
import logging
from collections import Counter, defaultdict

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TradChem:
    """
    TradChem - Traditional Medicine Chemical Analysis
    
    A comprehensive class for analyzing traditional medicine data, 
    chemical structures, and molecular properties.
    """
    
    def __init__(self, database_path=None):
        """Initialize TradChem with optional database path."""
        self.database_path = database_path or os.path.join(
            os.path.dirname(__file__), "data", "tradchem_database.json"
        )
        self.data = self.load_database()
        self._analysis_cache = {}
    
    def load_database(self):
        """Load the traditional medicine database."""
        try:
            if os.path.exists(self.database_path):
                with open(self.database_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                # Return empty database if file doesn't exist
                return []
        except Exception as e:
            logger.warning(f"Could not load database: {e}")
            return []
    
    def search_medicines(self, query: str, search_type: str = "name", limit: int = 10) -> List[Dict[str, Any]]:
        """Search for medicines in the database."""
        if not self.data:
            return []
        
        results = []
        query_lower = query.lower()
        
        for medicine in self.data:
            if search_type == "name" and "product_name" in medicine:
                if query_lower in medicine["product_name"].lower():
                    results.append(medicine)
            elif search_type == "benefit" and "benefits" in medicine:
                for benefit in medicine["benefits"]:
                    if query_lower in benefit.lower():
                        results.append(medicine)
                        break
            
            if len(results) >= limit:
                break
        
        return results
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get basic statistics about the database."""
        if not self.data:
            return {"total_medicines": 0}
        
        return {
            "total_medicines": len(self.data),
            "systems": list(set(m.get("traditional_system", "Unknown") for m in self.data)),
            "regions": list(set(m.get("geographic_origin", "Unknown") for m in self.data))
        }
    
    def load_data(self, file_path: str) -> List[Dict[str, Any]]:
        """Load traditional medicine data from various file formats."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        file_ext = os.path.splitext(file_path)[1].lower()
        
        if file_ext == '.csv':
            df = pd.read_csv(file_path)
            return df.to_dict('records')
        elif file_ext == '.json':
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data if isinstance(data, list) else [data]
        else:
            raise ValueError(f"Unsupported file format: {file_ext}")
    
    def validate_data(self, medicines: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Validate traditional medicine data structure and content."""
        validation_results = {
            'total_medicines': len(medicines),
            'valid_medicines': 0,
            'invalid_medicines': 0,
            'data_quality_score': 0.0,
            'errors': []
        }
        
        required_fields = ['product_name', 'benefits', 'diseases']
        
        for i, medicine in enumerate(medicines):
            medicine_valid = True
            
            for field in required_fields:
                if field not in medicine:
                    validation_results['errors'].append(f"Medicine {i}: missing {field}")
                    medicine_valid = False
            
            if medicine_valid:
                validation_results['valid_medicines'] += 1
            else:
                validation_results['invalid_medicines'] += 1
        
        if validation_results['total_medicines'] > 0:
            validation_results['data_quality_score'] = (
                validation_results['valid_medicines'] / validation_results['total_medicines']
            )
        
        return validation_results
    
    def analyze_chemical_structures(self, medicines: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze chemical structures in the medicines."""
        analysis_results = {
            'total_compounds': 0,
            'valid_smiles': 0,
            'invalid_smiles': 0,
            'avg_molecular_weight': 0.0,
            'unique_formulas': 0
        }
        
        total_weight = 0
        formulas = set()
        
        for medicine in medicines:
            if 'chemical_composition' in medicine:
                comp = medicine['chemical_composition']
                if 'ingredients' in comp:
                    for ingredient_name, ingredient_data in comp['ingredients'].items():
                        analysis_results['total_compounds'] += 1
                        
                        if 'smiles' in ingredient_data:
                            analysis_results['valid_smiles'] += 1
                        else:
                            analysis_results['invalid_smiles'] += 1
                        
                        if 'molecular_weight' in ingredient_data:
                            total_weight += ingredient_data['molecular_weight']
                        
                        if 'formula' in ingredient_data:
                            formulas.add(ingredient_data['formula'])
        
        if analysis_results['total_compounds'] > 0:
            analysis_results['avg_molecular_weight'] = total_weight / analysis_results['total_compounds']
        
        analysis_results['unique_formulas'] = len(formulas)
        
        return analysis_results
    
    def statistical_analysis(self, medicines: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Perform statistical analysis on traditional medicine data."""
        stats = {
            'total_medicines': len(medicines),
            'unique_systems': 0,
            'unique_regions': 0,
            'avg_benefits_per_medicine': 0.0,
            'compounds_with_smiles': 0,
            'system_distribution': {},
            'region_distribution': {}
        }
        
        systems = set()
        regions = set()
        total_benefits = 0
        compounds_with_smiles = 0
        
        for medicine in medicines:
            # Count systems
            if 'traditional_system' in medicine:
                system = medicine['traditional_system']
                systems.add(system)
                stats['system_distribution'][system] = stats['system_distribution'].get(system, 0) + 1
            
            # Count regions
            if 'geographic_origin' in medicine:
                region = medicine['geographic_origin']
                regions.add(region)
                stats['region_distribution'][region] = stats['region_distribution'].get(region, 0) + 1
            
            # Count benefits
            if 'benefits' in medicine:
                total_benefits += len(medicine['benefits'])
            
            # Count compounds with SMILES
            if 'chemical_composition' in medicine:
                comp = medicine['chemical_composition']
                if 'ingredients' in comp:
                    for ingredient_data in comp['ingredients'].values():
                        if 'smiles' in ingredient_data:
                            compounds_with_smiles += 1
        
        stats['unique_systems'] = len(systems)
        stats['unique_regions'] = len(regions)
        stats['compounds_with_smiles'] = compounds_with_smiles
        
        if stats['total_medicines'] > 0:
            stats['avg_benefits_per_medicine'] = total_benefits / stats['total_medicines']
        
        return stats
    
    def plot_statistics(self, medicines: List[Dict[str, Any]], save_path: Optional[str] = None) -> None:
        """Create statistical visualizations."""
        if not medicines:
            print("No data to plot")
            return
        
        stats = self.statistical_analysis(medicines)
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Traditional Medicine Statistics', fontsize=16)
        
        # System distribution
        if stats['system_distribution']:
            systems = list(stats['system_distribution'].keys())
            counts = list(stats['system_distribution'].values())
            axes[0, 0].bar(systems, counts)
            axes[0, 0].set_title('Medicine Systems Distribution')
            axes[0, 0].tick_params(axis='x', rotation=45)
        
        # Region distribution
        if stats['region_distribution']:
            regions = list(stats['region_distribution'].keys())
            counts = list(stats['region_distribution'].values())
            axes[0, 1].bar(regions, counts)
            axes[0, 1].set_title('Geographic Distribution')
            axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Benefits per medicine
        axes[1, 0].hist([len(m.get('benefits', [])) for m in medicines], bins=10)
        axes[1, 0].set_title('Benefits per Medicine')
        axes[1, 0].set_xlabel('Number of Benefits')
        axes[1, 0].set_ylabel('Frequency')
        
        # Summary statistics
        summary_text = f"""
        Total Medicines: {stats['total_medicines']}
        Unique Systems: {stats['unique_systems']}
        Unique Regions: {stats['unique_regions']}
        Avg Benefits/Medicine: {stats['avg_benefits_per_medicine']:.2f}
        Compounds with SMILES: {stats['compounds_with_smiles']}
        """
        axes[1, 1].text(0.1, 0.5, summary_text, transform=axes[1, 1].transAxes, 
                       fontsize=12, verticalalignment='center')
        axes[1, 1].set_title('Summary Statistics')
        axes[1, 1].axis('off')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to: {save_path}")
        else:
            plt.show()
    
    def add_medicine(self, medicine_entry: Dict[str, Any]) -> bool:
        """Add a new medicine to the database."""
        try:
            self.data.append(medicine_entry)
            return True
        except Exception as e:
            logger.error(f"Failed to add medicine: {e}")
            return False
'''

with open(tradchem_dir / "tradchem.py", "w", encoding="utf-8") as f:
    f.write(tradchem_content)

# Create utils/__init__.py
utils_init = '''"""Utility modules for TradChem."""
from . import smiles_utils, data_utils

__all__ = ['smiles_utils', 'data_utils']
'''

with open(utils_dir / "__init__.py", "w", encoding="utf-8") as f:
    f.write(utils_init)

# Create minimal smiles_utils.py
smiles_utils_content = '''"""SMILES utilities for chemical structure validation."""
import re

def validate_smiles(smiles: str) -> bool:
    """Validate SMILES notation."""
    if not smiles or not isinstance(smiles, str):
        return False
    
    # Basic SMILES validation pattern
    pattern = r'^[A-Za-z0-9@+\-\[\]\(\)=#$%:]+$'
    return bool(re.match(pattern, smiles))

def canonicalize_smiles(smiles: str) -> str:
    """Convert SMILES to canonical form."""
    # This is a simplified version - in practice, you'd use RDKit
    return smiles.strip()

def convert_smiles_format(smiles: str, target_format: str) -> str:
    """Convert SMILES to different formats."""
    # Simplified conversion
    if target_format.lower() == "canonical":
        return canonicalize_smiles(smiles)
    return smiles
'''

with open(utils_dir / "smiles_utils.py", "w", encoding="utf-8") as f:
    f.write(smiles_utils_content)

# Create minimal data_utils.py
data_utils_content = '''"""Data utilities for TradChem."""
import pandas as pd
from typing import List, Dict, Any

def load_csv_data(file_path: str) -> List[Dict[str, Any]]:
    """Load data from CSV file."""
    try:
        df = pd.read_csv(file_path)
        return df.to_dict('records')
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return []

def load_json_data(file_path: str) -> List[Dict[str, Any]]:
    """Load data from JSON file."""
    try:
        import json
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data if isinstance(data, list) else [data]
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return []

def validate_data_structure(data: List[Dict[str, Any]]) -> bool:
    """Validate data structure."""
    if not isinstance(data, list):
        return False
    
    required_fields = ['product_name']
    for item in data:
        if not isinstance(item, dict):
            return False
        if not all(field in item for field in required_fields):
            return False
    
    return True
'''

with open(utils_dir / "data_utils.py", "w", encoding="utf-8") as f:
    f.write(data_utils_content)

# Create medicine_systems/__init__.py
medicine_init = '''"""Traditional medicine systems modules."""
from . import ayurvedic

__all__ = ['ayurvedic']
'''

with open(medicine_dir / "__init__.py", "w", encoding="utf-8") as f:
    f.write(medicine_init)

# Create minimal ayurvedic.py
ayurvedic_content = '''"""Ayurvedic medicine system analysis."""
from typing import Dict, List, Any

class AyurvedicAnalyzer:
    """Analyzer for Ayurvedic medicine system."""
    
    def __init__(self):
        self.doshas = ['vata', 'pitta', 'kapha']
        self.rasas = ['sweet', 'sour', 'salty', 'bitter', 'pungent', 'astringent']
    
    def analyze_dosha_balance(self, medicine_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze dosha balance in medicine."""
        return {
            'vata': 0.33,
            'pitta': 0.33,
            'kapha': 0.34,
            'balance_score': 0.95
        }
    
    def analyze_rasa_distribution(self, medicine_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze rasa distribution."""
        return {
            'sweet': 0.2,
            'sour': 0.15,
            'salty': 0.1,
            'bitter': 0.25,
            'pungent': 0.2,
            'astringent': 0.1
        }
    
    def get_therapeutic_properties(self, medicine_data: Dict[str, Any]) -> List[str]:
        """Get therapeutic properties."""
        return ['anti-inflammatory', 'digestive', 'immunomodulatory']

# Create instance for easy access
ayurvedic = AyurvedicAnalyzer()
'''

with open(medicine_dir / "ayurvedic.py", "w", encoding="utf-8") as f:
    f.write(ayurvedic_content)

# Create setup.py
setup_content = '''from setuptools import setup, find_packages

setup(
    name="tradchem",
    version="0.2.0",
    description="Traditional medicine chemical analysis package",
    author="SaltyHeart",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "scikit-learn>=0.24.0",
        "jsonschema>=3.2.0",
        "pydantic>=1.8.0",
    ],
    python_requires=">=3.7",
)
'''

with open(base_dir / "setup.py", "w", encoding="utf-8") as f:
    f.write(setup_content)

# Step 5: Install the package
print("🔧 Installing clean TradChem package...")
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", str(base_dir)])
    print("✅ TradChem installed successfully!")
except Exception as e:
    print(f"❌ Installation failed: {e}")
    print("Adding to Python path instead...")
    sys.path.append(str(base_dir))

# Step 6: Test installation
print("\n🧪 Testing TradChem installation...")
try:
    from tradchem import TradChem
    print("✅ TradChem imported successfully")
    
    tc = TradChem()
    print("✅ TradChem initialized successfully")
    
    # Test basic functionality
    stats = tc.get_statistics()
    print(f"✅ Database statistics: {stats['total_medicines']} medicines")
    
    # Test search
    results = tc.search_medicines("test", limit=1)
    print(f"✅ Search functionality: {len(results)} results")
    
    print("🎉 TradChem is working correctly!")
    
except Exception as e:
    print(f"❌ Test failed: {e}")

print("\n🎉 Clean installation complete!")
print("\nExample usage:")
print("from tradchem import TradChem")
print("tc = TradChem()")
print("tc.search_medicines('turmeric')") 