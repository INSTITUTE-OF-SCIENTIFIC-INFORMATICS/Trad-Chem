# 🌿 TradChem Google Colab Integration Guide

This guide provides comprehensive instructions for using TradChem in Google Colab, including installation, setup, and best practices.

## 🚨 **Important Note**

TradChem is currently in development and not available on PyPI. Use the installation methods provided in this guide to get started in Google Colab.

## 🚀 **Quick Start**

### **Step 1: Install TradChem**

Copy and paste this code into a Colab cell:

```python
# TradChem Quick Installation for Colab
import subprocess
import sys
import os
from pathlib import Path

print("🚀 Installing TradChem for Google Colab...")

# Install dependencies
deps = ["numpy", "pandas", "scipy", "matplotlib", "seaborn", "scikit-learn", "jsonschema", "pydantic"]
for dep in deps:
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

# Clone and install
subprocess.check_call(["git", "clone", "https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem.git", "/content/Trad-Chem"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "/content/Trad-Chem"])

# Test installation
from tradchem import TradChem
tc = TradChem()
print("✅ TradChem is ready!")
```

### **Step 2: Start Using TradChem**

```python
# Basic usage
from tradchem import TradChem

# Initialize
tc = TradChem()
print("✅ TradChem initialized")

# Test basic functionality
stats = tc.get_statistics()
print(f"✅ Database statistics: {stats['total_medicines']} medicines")

# Test search
results = tc.search_medicines("turmeric", limit=5)
print(f"✅ Search functionality: {len(results)} results")

print("🎉 TradChem is working correctly!")
```

## 📚 **Installation Methods**

### **Method 1: Clean Installation (Recommended)**

For a clean installation without file corruption issues, use the comprehensive installation script from [COLAB_INSTALLATION_GUIDE.md](COLAB_INSTALLATION_GUIDE.md).

### **Method 2: Simple Git Clone**

```python
# Simple installation
!pip install numpy pandas scipy matplotlib seaborn scikit-learn jsonschema pydantic rdkit-pypi
!git clone https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem.git
!pip install -e Trad-Chem/

from tradchem import TradChem
tc = TradChem()
```

### **Method 3: Manual File Download**

```python
import urllib.request
import os
import sys

# Create directory
os.makedirs("/content/tradchem", exist_ok=True)

# Download core files
files = {
    "/content/tradchem/__init__.py": "https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/tradchem/__init__.py",
    "/content/tradchem/tradchem.py": "https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/tradchem/tradchem.py",
    "/content/tradchem/version.py": "https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/tradchem/version.py"
}

for file_path, url in files.items():
    urllib.request.urlretrieve(url, file_path)
    print(f"Downloaded: {file_path}")

# Add to Python path
sys.path.append("/content")

# Test import
from tradchem import TradChem
tc = TradChem()
```

## 🎓 **Learning Paths**

### **Beginner Path**

1. **Start with Basic Usage**
   ```python
   from tradchem import TradChem
   tc = TradChem()
   
   # Load sample data
   medicines = tc.load_data('sample_medicines.csv')
   
   # Basic analysis
   stats = tc.statistical_analysis(medicines)
   print(f"Total medicines: {stats['total_medicines']}")
   ```

2. **Try Data Validation**
   ```python
   # Validate your data
   validation = tc.validate_data(medicines)
   print(f"Data quality score: {validation['data_quality_score']:.2%}")
   ```

3. **Explore Search Functionality**
   ```python
   # Search for specific medicines
   results = tc.search_medicines("turmeric", limit=10)
   for medicine in results:
       print(f"- {medicine['product_name']}")
   ```

### **Intermediate Path**

1. **Chemical Analysis**
   ```python
   # Analyze chemical structures
   chemical_analysis = tc.analyze_chemical_structures(medicines)
   print(f"Valid SMILES: {chemical_analysis['valid_smiles']}")
   print(f"Average molecular weight: {chemical_analysis['avg_molecular_weight']:.2f}")
   ```

2. **Statistical Analysis**
   ```python
   # Perform comprehensive statistical analysis
   stats = tc.statistical_analysis(medicines)
   
   # View system distribution
   for system, count in stats['system_distribution'].items():
       print(f"{system}: {count}")
   ```

3. **Data Processing**
   ```python
   # Filter data
   ayurvedic_medicines = tc.filter_data(medicines, system='Ayurvedic')
   
   # Sort data
   sorted_medicines = tc.sort_data(medicines, by='molecular_weight')
   ```

### **Advanced Path**

1. **Visualization**
   ```python
   # Create statistical plots
   tc.plot_statistics(medicines)
   
   # Save plots
   tc.plot_statistics(medicines, save_path='medicine_stats.png')
   ```

2. **Custom Analysis**
   ```python
   # Create custom analysis workflows
   def custom_analysis(medicines):
       # Your custom analysis here
       pass
   ```

3. **Integration with Other Tools**
   ```python
   # Integrate with pandas for advanced analysis
   import pandas as pd
   
   df = pd.DataFrame(medicines)
   # Use pandas for additional analysis
   ```

## 📖 **Tutorials and Examples**

### **Available Tutorials**

1. **[Basic Usage Tutorial](colab_examples/tradchem_basic_usage.ipynb)**
   - Introduction to TradChem
   - Data loading and validation
   - Basic analysis functions
   - Search and filtering

2. **[Chemical Analysis Tutorial](colab_examples/tradchem_chemical_analysis.ipynb)**
   - SMILES validation
   - Molecular property calculations
   - Chemical structure analysis
   - Advanced chemical features

3. **[Quick Start Script](colab_examples/quick_start.py)**
   - Fast results
   - Common use cases
   - Ready-to-run examples

### **Knowledge Graph Navigation**

- **[TradChem Knowledge Graph](colab_examples/TRADCHEM_KNOWLEDGE_GRAPH.md)**
  - Complete component overview
  - Interactive navigation
  - Learning paths
  - Use case examples

## 🛠️ **Best Practices**

### **Data Management**

1. **Use Proper Data Formats**
   ```python
   # Preferred JSON format
   medicine_data = {
       "product_name": "Turmeric Extract",
       "scientific_name": "Curcuma longa",
       "traditional_system": "Ayurveda",
       "benefits": ["Anti-inflammatory", "Antioxidant"],
       "chemical_composition": {
           "ingredients": {
               "Curcumin": {
                   "smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
                   "molecular_weight": 368.38
               }
           }
       }
   }
   ```

2. **Validate Your Data**
   ```python
   # Always validate before analysis
   validation = tc.validate_data(medicines)
   if validation['data_quality_score'] < 0.8:
       print("Warning: Low data quality detected")
   ```

3. **Handle Large Datasets**
   ```python
   # Process data in chunks for large datasets
   chunk_size = 1000
   for i in range(0, len(medicines), chunk_size):
       chunk = medicines[i:i+chunk_size]
       analysis = tc.analyze_chemical_structures(chunk)
   ```

### **Performance Optimization**

1. **Use Caching**
   ```python
   # Results are cached automatically
   # First call - computes results
   stats1 = tc.statistical_analysis(medicines)
   
   # Second call - uses cached results
   stats2 = tc.statistical_analysis(medicines)  # Fast!
   ```

2. **Optimize Visualizations**
   ```python
   # Save plots instead of displaying for large datasets
   tc.plot_statistics(medicines, save_path='results.png')
   ```

3. **Memory Management**
   ```python
   # Clear cache when needed
   tc._analysis_cache.clear()
   ```

## 🔍 **Troubleshooting**

### **Common Issues**

#### **1. Installation Problems**
- **Issue**: Package not found
- **Solution**: Use the installation methods in this guide
- **Alternative**: Try the clean installation script

#### **2. Import Errors**
- **Issue**: `ModuleNotFoundError: No module named 'tradchem'`
- **Solution**: Check installation, restart runtime if needed

#### **3. Data Loading Issues**
- **Issue**: File format not supported
- **Solution**: Use CSV or JSON format
- **Alternative**: Convert your data to supported formats

#### **4. Memory Issues**
- **Issue**: Out of memory errors
- **Solution**: Process data in chunks
- **Alternative**: Use smaller datasets

### **Getting Help**

1. **Check Documentation**: [Knowledge Graph](colab_examples/TRADCHEM_KNOWLEDGE_GRAPH.md)
2. **Report Issues**: [GitHub Issues](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/issues)
3. **Join Discussions**: [GitHub Discussions](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/discussions)

## 🎯 **Use Cases in Colab**

### **Research Projects**

```python
# Traditional medicine research
medicines = tc.load_data('research_data.csv')
analysis = tc.analyze_chemical_structures(medicines)
tc.plot_statistics(medicines, save_path='research_results.png')
```

### **Educational Purposes**

```python
# Learning traditional medicine systems
ayurvedic_medicines = tc.filter_data(medicines, system='Ayurvedic')
stats = tc.statistical_analysis(ayurvedic_medicines)
print("Ayurvedic medicine characteristics:")
print(f"- Total medicines: {stats['total_medicines']}")
print(f"- Common benefits: {stats['common_benefits']}")
```

### **Data Analysis**

```python
# Comprehensive data analysis
validation = tc.validate_data(medicines)
chemical_analysis = tc.analyze_chemical_structures(medicines)
statistical_analysis = tc.statistical_analysis(medicines)

# Create comprehensive report
print("=== TradChem Analysis Report ===")
print(f"Data Quality: {validation['data_quality_score']:.2%}")
print(f"Chemical Compounds: {chemical_analysis['total_compounds']}")
print(f"Medicine Systems: {statistical_analysis['unique_systems']}")
```

## 📊 **Integration with Other Colab Tools**

### **Pandas Integration**

```python
import pandas as pd

# Convert TradChem data to pandas DataFrame
df = pd.DataFrame(medicines)

# Use pandas for additional analysis
system_counts = df['traditional_system'].value_counts()
print(system_counts)
```

### **Matplotlib Integration**

```python
import matplotlib.pyplot as plt

# Create custom visualizations
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(system_counts.index, system_counts.values)
ax.set_title('Traditional Medicine Systems Distribution')
plt.xticks(rotation=45)
plt.show()
```

### **Machine Learning Integration**

```python
from sklearn.cluster import KMeans

# Use TradChem data for machine learning
# Extract features from chemical compositions
features = []
for medicine in medicines:
    if 'chemical_composition' in medicine:
        # Extract molecular weights as features
        weights = [ing['molecular_weight'] for ing in medicine['chemical_composition']['ingredients'].values()]
        features.append(sum(weights) / len(weights) if weights else 0)
    else:
        features.append(0)

# Perform clustering
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(features)
```

## 🚀 **Advanced Features**

### **Custom Analysis Functions**

```python
def custom_medicine_analysis(tc, medicines):
    """Custom analysis function."""
    results = {
        'total_medicines': len(medicines),
        'systems_analysis': {},
        'chemical_diversity': 0
    }
    
    # Analyze by system
    for medicine in medicines:
        system = medicine.get('traditional_system', 'Unknown')
        if system not in results['systems_analysis']:
            results['systems_analysis'][system] = 0
        results['systems_analysis'][system] += 1
    
    # Calculate chemical diversity
    unique_compounds = set()
    for medicine in medicines:
        if 'chemical_composition' in medicine:
            for ingredient in medicine['chemical_composition']['ingredients']:
                unique_compounds.add(ingredient)
    
    results['chemical_diversity'] = len(unique_compounds)
    
    return results

# Use custom analysis
custom_results = custom_medicine_analysis(tc, medicines)
print(custom_results)
```

### **Batch Processing**

```python
def batch_process_medicines(tc, medicine_files):
    """Process multiple medicine files."""
    all_results = []
    
    for file_path in medicine_files:
        try:
            medicines = tc.load_data(file_path)
            analysis = tc.analyze_chemical_structures(medicines)
            all_results.append({
                'file': file_path,
                'medicines': len(medicines),
                'compounds': analysis['total_compounds']
            })
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    return all_results

# Process multiple files
files = ['medicines1.csv', 'medicines2.csv', 'medicines3.csv']
batch_results = batch_process_medicines(tc, files)
```

## 📞 **Support and Community**

### **Getting Help**

- **Documentation**: [Knowledge Graph](colab_examples/TRADCHEM_KNOWLEDGE_GRAPH.md)
- **Installation Guide**: [COLAB_INSTALLATION_GUIDE.md](COLAB_INSTALLATION_GUIDE.md)
- **Issues**: [GitHub Issues](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/issues)
- **Discussions**: [GitHub Discussions](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/discussions)

### **Contributing**

- **Code Contributions**: See [CONTRIBUTING_PYTHON_PACKAGE.md](CONTRIBUTING_PYTHON_PACKAGE.md)
- **Data Contributions**: Add traditional medicine data
- **Documentation**: Improve tutorials and guides
- **Community**: Share use cases and examples

---

**🌿 TradChem** - Empowering traditional medicine research in Google Colab!

*Built for researchers, educators, and traditional medicine enthusiasts* 