# 🌿 TradChem Google Colab Examples

This directory contains Jupyter notebooks designed to work seamlessly in Google Colab for exploring and analyzing traditional medicine data with the TradChem package.

## 📚 Available Notebooks

### 1. **tradchem_basic_usage.ipynb**
**Basic usage and data exploration**

- ✅ Package installation and setup
- ✅ Database statistics and visualization
- ✅ Medicine search and information retrieval
- ✅ Data export and analysis
- ✅ Basic plotting and data exploration

**Perfect for**: Beginners, data exploration, understanding the database structure

### 2. **tradchem_chemical_analysis.ipynb**
**Advanced chemical analysis and cheminformatics**

- 🧪 SMILES notation validation and analysis
- 📊 Molecular property calculations
- 💊 Drug-likeness analysis (Lipinski's Rule of Five)
- 🎨 Chemical structure visualization
- 📈 Property correlation analysis
- 🔬 RDKit integration for cheminformatics

**Perfect for**: Researchers, chemists, drug discovery, molecular analysis

## 🚀 Quick Start in Google Colab

### Method 1: Direct Installation
```python
# Install TradChem package
!pip install tradchem

# Import and use
from tradchem import TradChem
tc = TradChem()
```

### Method 2: From GitHub (Latest Version)
```python
# Clone and install from GitHub
!git clone https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem.git
!pip install -e Trad-Chem/

# Import and use
from tradchem import TradChem
tc = TradChem()
```

### Method 3: Using Installation Script
```python
# Download and run installation script
!wget https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/colab_install.py
!python colab_install.py
```

## 📋 Prerequisites

### Basic Usage Notebook
- Python 3.7+
- pandas
- matplotlib
- seaborn

### Chemical Analysis Notebook
- Python 3.7+
- rdkit-pypi
- pandas
- matplotlib
- seaborn
- numpy

## 🔧 Installation Commands

### Install All Dependencies
```python
# Install core dependencies
!pip install tradchem pandas matplotlib seaborn numpy

# Install cheminformatics dependencies
!pip install rdkit-pypi
```

### Verify Installation
```python
# Test import
from tradchem import TradChem
tc = TradChem()
print("✅ TradChem installed successfully!")

# Test basic functionality
stats = tc.get_statistics()
print(f"Database contains {stats['total_medicines']} medicines")
```

## 📖 Usage Examples

### Basic Data Exploration
```python
from tradchem import TradChem
import pandas as pd
import matplotlib.pyplot as plt

# Initialize
tc = TradChem()

# Get statistics
stats = tc.get_statistics()
print(f"Total medicines: {stats['total_medicines']}")

# Search medicines
results = tc.search_medicines("turmeric")
print(f"Found {len(results)} results")

# Export data
data = tc.export_data(format="json")
df = pd.DataFrame(data)
```

### Chemical Analysis
```python
from rdkit import Chem
from rdkit.Chem import Descriptors

# Get medicine with chemical data
medicine = tc.get_medicine("turmeric")
chem_comp = medicine.get('chemical_composition', {})

# Analyze SMILES
for ingredient, details in chem_comp.get('ingredients', {}).items():
    if isinstance(details, dict) and details.get('smiles'):
        mol = Chem.MolFromSmiles(details['smiles'])
        if mol:
            mw = Descriptors.MolWt(mol)
            logp = Descriptors.MolLogP(mol)
            print(f"{ingredient}: MW={mw:.1f}, LogP={logp:.2f}")
```

## 🎯 Key Features Demonstrated

### Data Management
- Database loading and validation
- Search functionality (name, benefits, diseases, ingredients)
- Data export in multiple formats
- Statistics and reporting

### Chemical Analysis
- SMILES notation validation
- Molecular property calculations
- Drug-likeness assessment
- Chemical structure visualization
- Property correlation analysis

### Visualization
- Statistical plots and charts
- Chemical structure diagrams
- Property distribution histograms
- Correlation heatmaps

## 🔍 Troubleshooting

### Common Issues

1. **Import Error**: Make sure TradChem is installed
   ```python
   !pip install tradchem
   ```

2. **RDKit Installation Issues**: Use the specific package
   ```python
   !pip install rdkit-pypi
   ```

3. **Display Issues**: Restart runtime if plots don't show
   ```python
   # Restart runtime: Runtime → Restart runtime
   ```

4. **Memory Issues**: Use smaller datasets or restart runtime
   ```python
   # Limit search results
   results = tc.search_medicines("query", limit=10)
   ```

### Getting Help

- **GitHub Issues**: Report bugs and request features
- **Documentation**: Check the main README.md
- **Examples**: Explore the notebooks in this directory
- **Community**: Join discussions on GitHub

## 📈 Advanced Usage

### Custom Analysis
```python
# Custom molecular property analysis
def analyze_compound(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        return {
            'mw': Descriptors.MolWt(mol),
            'logp': Descriptors.MolLogP(mol),
            'hbd': Descriptors.NumHDonors(mol),
            'hba': Descriptors.NumHAcceptors(mol)
        }
    return None

# Apply to all compounds
properties = []
for medicine in tc.data:
    chem_comp = medicine.get('chemical_composition', {})
    for ingredient, details in chem_comp.get('ingredients', {}).items():
        if isinstance(details, dict) and details.get('smiles'):
            props = analyze_compound(details['smiles'])
            if props:
                props['medicine'] = medicine['product_name']
                props['ingredient'] = ingredient
                properties.append(props)
```

### Data Export and Sharing
```python
# Export analysis results
import json

# Save results
with open('tradchem_analysis.json', 'w') as f:
    json.dump(properties, f, indent=2)

# Download from Colab
from google.colab import files
files.download('tradchem_analysis.json')
```

## 🎉 Contributing

We welcome contributions to improve these examples:

1. **Add new analysis methods**
2. **Improve visualizations**
3. **Add more use cases**
4. **Fix bugs and issues**
5. **Improve documentation**

## 📄 License

These examples are part of the TradChem project and are licensed under the MIT License.

---

**Happy exploring traditional medicine with modern Python tools! 🌿🧪** 