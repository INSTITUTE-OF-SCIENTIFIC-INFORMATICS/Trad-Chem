# 🌐 Google Colab Integration Guide

This guide provides comprehensive instructions for using TradChem in Google Colab for traditional medicine research and analysis.

## 🚀 **Quick Start**

### **Method 1: One-Click Installation (Recommended)**

```python
# Copy and paste this into a Colab cell
!git clone https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem.git
!pip install -e Trad-Chem/
!pip install rdkit-pypi

# Start using TradChem immediately
from tradchem import TradChem
tc = TradChem()
print("✅ TradChem is ready!")
```

### **Method 2: Using Installation Script**

```python
# Download and run the installation script
!wget https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/colab_install.py
!python colab_install.py
```

### **Method 3: Manual Installation**

```python
# Install core dependencies
!pip install tradchem pandas matplotlib seaborn numpy scikit-learn

# Install cheminformatics tools
!pip install rdkit-pypi

# Import and verify
from tradchem import TradChem
tc = TradChem()
stats = tc.get_statistics()
print(f"Database loaded: {stats['total_medicines']} medicines")
```

## 📚 **Available Notebooks**

### **1. Setup Notebook**
**File**: `colab_examples/colab_setup.ipynb`

**Features**:
- ✅ Automatic installation and configuration
- 🧪 Installation testing and verification
- 📊 Quick demonstration of capabilities
- 🔧 Environment setup for Colab

**Best for**: First-time users, setting up the environment

### **2. Basic Usage Notebook**
**File**: `colab_examples/tradchem_basic_usage.ipynb`

**Features**:
- 🔍 Medicine search and exploration
- 📊 Database statistics and visualization
- 📋 Detailed medicine information
- 📤 Data export and analysis
- 📈 Basic plotting and charts

**Best for**: Data exploration, understanding the database

### **3. Chemical Analysis Notebook**
**File**: `colab_examples/tradchem_chemical_analysis.ipynb`

**Features**:
- 🧪 SMILES notation validation
- 📊 Molecular property calculations
- 💊 Drug-likeness analysis (Lipinski's Rule of Five)
- 🎨 Chemical structure visualization
- 📈 Property correlation analysis
- 🔬 RDKit integration

**Best for**: Researchers, chemists, drug discovery

### **4. Quick Start Script**
**File**: `colab_examples/quick_start.py`

**Features**:
- 🚀 Rapid installation and setup
- 🧪 Basic functionality testing
- 📊 Quick demonstration
- 📖 Usage examples

**Best for**: Quick testing, demonstrations

## 🔧 **Dependencies**

### **Core Dependencies (Auto-installed)**
```
tradchem>=0.2.0
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=0.24.0
jsonschema>=3.2.0
pydantic>=1.8.0
```

### **Chemical Analysis Dependencies**
```
rdkit-pypi>=2022.9.1  # For cheminformatics
```

### **Optional Dependencies**
```
plotly>=5.0.0         # Interactive plots
ipywidgets>=7.6.0     # Interactive widgets
networkx>=2.6.0       # Network analysis
```

## 📖 **Usage Examples**

### **Basic Data Exploration**

```python
from tradchem import TradChem
import pandas as pd
import matplotlib.pyplot as plt

# Initialize
tc = TradChem()

# Get overview
stats = tc.get_statistics()
print(f"Database: {stats['total_medicines']} medicines")

# Search medicines
results = tc.search_medicines("turmeric")
for medicine in results:
    print(f"• {medicine['product_name']}")

# Export to DataFrame
data = tc.export_data(format="json")
df = pd.DataFrame(data)
print(f"DataFrame: {df.shape}")
```

### **Chemical Analysis**

```python
from rdkit import Chem
from rdkit.Chem import Descriptors

# Get medicine with chemical data
medicine = tc.get_medicine("turmeric")
chem_comp = medicine.get('chemical_composition', {})

# Analyze each ingredient
for ingredient, details in chem_comp.get('ingredients', {}).items():
    if isinstance(details, dict) and details.get('smiles'):
        mol = Chem.MolFromSmiles(details['smiles'])
        if mol:
            mw = Descriptors.MolWt(mol)
            logp = Descriptors.MolLogP(mol)
            print(f"{ingredient}: MW={mw:.1f}, LogP={logp:.2f}")
```

### **Data Visualization**

```python
import seaborn as sns

# Create visualizations
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot 1: Medicine count by system
system_counts = df['traditional_system'].value_counts()
ax1.bar(system_counts.index, system_counts.values, color='#2E8B57')
ax1.set_title('Medicines by Traditional System')
ax1.tick_params(axis='x', rotation=45)

# Plot 2: Benefits distribution
all_benefits = []
for benefits in df['benefits'].dropna():
    if isinstance(benefits, list):
        all_benefits.extend(benefits)
benefit_counts = pd.Series(all_benefits).value_counts().head(10)
ax2.barh(benefit_counts.index, benefit_counts.values, color='#FF6B6B')
ax2.set_title('Top 10 Therapeutic Benefits')

plt.tight_layout()
plt.show()
```

### **Advanced Analysis**

```python
# Drug-likeness analysis
def analyze_drug_likeness(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        mw = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        hbd = Descriptors.NumHDonors(mol)
        hba = Descriptors.NumHAcceptors(mol)
        
        # Lipinski's Rule of Five
        violations = 0
        if mw > 500: violations += 1
        if logp > 5: violations += 1
        if hbd > 5: violations += 1
        if hba > 10: violations += 1
        
        return {
            'mw': mw, 'logp': logp, 'hbd': hbd, 'hba': hba,
            'violations': violations, 'drug_like': violations == 0
        }
    return None

# Apply to all compounds
drug_likeness_data = []
for medicine in tc.data:
    chem_comp = medicine.get('chemical_composition', {})
    for ingredient, details in chem_comp.get('ingredients', {}).items():
        if isinstance(details, dict) and details.get('smiles'):
            analysis = analyze_drug_likeness(details['smiles'])
            if analysis:
                analysis['medicine'] = medicine['product_name']
                analysis['ingredient'] = ingredient
                drug_likeness_data.append(analysis)

# Create analysis DataFrame
drug_df = pd.DataFrame(drug_likeness_data)
print(f"Drug-likeness analysis: {len(drug_df)} compounds")
print(f"Drug-like compounds: {drug_df['drug_like'].sum()} ({drug_df['drug_like'].mean()*100:.1f}%)")
```

## 🎯 **Research Workflows**

### **Traditional Medicine Research**

```python
# 1. Literature review support
def find_medicines_for_condition(condition):
    return tc.search_medicines(condition, search_type="disease")

# 2. Cross-cultural comparison
def compare_systems():
    systems = {}
    for medicine in tc.data:
        system = medicine.get('traditional_system', 'Unknown')
        if system not in systems:
            systems[system] = {'medicines': [], 'benefits': set()}
        systems[system]['medicines'].append(medicine['product_name'])
        if medicine.get('benefits'):
            systems[system]['benefits'].update(medicine['benefits'])
    return systems

# 3. Chemical composition analysis
def analyze_chemical_diversity():
    all_ingredients = set()
    for medicine in tc.data:
        chem_comp = medicine.get('chemical_composition', {})
        ingredients = chem_comp.get('ingredients', {})
        all_ingredients.update(ingredients.keys())
    return len(all_ingredients), list(all_ingredients)
```

### **Drug Discovery Support**

```python
# 1. Lead compound identification
def find_promising_compounds():
    promising = []
    for medicine in tc.data:
        chem_comp = medicine.get('chemical_composition', {})
        for ingredient, details in chem_comp.get('ingredients', {}).items():
            if isinstance(details, dict) and details.get('smiles'):
                analysis = analyze_drug_likeness(details['smiles'])
                if analysis and analysis['drug_like']:
                    promising.append({
                        'medicine': medicine['product_name'],
                        'ingredient': ingredient,
                        'analysis': analysis
                    })
    return promising

# 2. Structure-activity relationship
def analyze_sar_patterns():
    # Group compounds by benefits and analyze structural patterns
    benefit_compounds = {}
    for medicine in tc.data:
        if medicine.get('benefits'):
            for benefit in medicine['benefits']:
                if benefit not in benefit_compounds:
                    benefit_compounds[benefit] = []
                chem_comp = medicine.get('chemical_composition', {})
                benefit_compounds[benefit].extend(chem_comp.get('ingredients', {}).keys())
    return benefit_compounds
```

## 🔍 **Troubleshooting**

### **Common Issues**

1. **Import Error**: Package not installed
   ```python
   !pip install tradchem
   ```

2. **RDKit Issues**: Chemical analysis not working
   ```python
   !pip install rdkit-pypi
   ```

3. **Display Issues**: Plots not showing
   ```python
   # Restart runtime: Runtime → Restart runtime
   ```

4. **Memory Issues**: Large dataset problems
   ```python
   # Limit results
   results = tc.search_medicines("query", limit=10)
   ```

### **Performance Tips**

1. **Use limits**: Limit search results to avoid memory issues
2. **Batch processing**: Process data in smaller chunks
3. **Restart runtime**: Clear memory when needed
4. **Use GPU**: Enable GPU acceleration for large computations

### **Getting Help**

- **GitHub Issues**: Report bugs and request features
- **Documentation**: Check README.md and examples
- **Community**: Join discussions on GitHub
- **Examples**: Explore the provided notebooks

## 📊 **Data Export and Sharing**

### **Export Results**

```python
# Export analysis results
import json
from google.colab import files

# Save results
results = {
    'statistics': tc.get_statistics(),
    'search_results': tc.search_medicines("turmeric"),
    'analysis_data': drug_likeness_data
}

with open('tradchem_analysis.json', 'w') as f:
    json.dump(results, f, indent=2)

# Download from Colab
files.download('tradchem_analysis.json')
```

### **Share Notebooks**

```python
# Save notebook with results
from google.colab import drive
drive.mount('/content/drive')

# Save to Google Drive
!cp tradchem_analysis.json /content/drive/MyDrive/
```

## 🎉 **Success Stories**

### **Academic Research**
- Traditional medicine digitization projects
- Cross-cultural medicine comparison studies
- Chemical composition analysis research
- Drug discovery from traditional sources

### **Educational Use**
- Traditional medicine courses
- Cheminformatics training
- Data science education
- Research methodology teaching

### **Industry Applications**
- Pharmaceutical research
- Natural product development
- Traditional medicine validation
- Chemical database management

## 🔮 **Future Enhancements**

### **Planned Features**
- **Interactive Dashboards**: Plotly-based interactive visualizations
- **Machine Learning Integration**: Predictive models for medicine properties
- **Network Analysis**: Compound-target interaction networks
- **API Integration**: Connect with external chemical databases

### **Community Contributions**
- **New Analysis Methods**: Community-developed analysis workflows
- **Data Validation Tools**: Automated data quality assessment
- **Visualization Templates**: Reusable plotting templates
- **Research Templates**: Standardized research workflows

---

**Happy researching with TradChem in Google Colab! 🌿🧪**

*Empowering traditional medicine research with modern cloud computing* 