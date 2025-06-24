# 🌿 TradChem: Traditional Medicine Chemical Analysis

A comprehensive Python package for analyzing traditional medicine data, chemical structures, and molecular properties. TradChem bridges the gap between traditional medicine systems and modern chemical analysis.

## 📋 **Table of Contents**

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Google Colab Integration](#google-colab-integration)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Use Cases](#use-cases)
- [License](#license)

## ✨ **Features**

### 🔍 **Core Analysis Components**
- **Data Loading & Validation**: Load and validate traditional medicine data from various sources
- **Chemical Structure Analysis**: Analyze molecular structures and properties using SMILES notation
- **Statistical Analysis**: Perform comprehensive statistical analysis on traditional medicine data
- **Traditional Medicine Analysis**: Analyze traditional medicine systems and their characteristics

### 🛠️ **Utility Components**
- **Data Processing Tools**: Filter, sort, and transform traditional medicine data
- **SMILES Utilities**: Validate and manipulate chemical structure notations
- **Visualization Tools**: Create comprehensive visualizations for analysis results

### 🎯 **Advanced Capabilities**
- **Drug-likeness Analysis**: Screen compounds using Lipinski's Rule of Five
- **Molecular Property Calculations**: Calculate comprehensive molecular descriptors
- **Chemical Diversity Analysis**: Analyze chemical diversity across traditional systems
- **Structure-Activity Relationships**: Identify patterns in chemical properties

## 🚀 **Installation**

### **Local Installation**
```bash
# Clone the repository
git clone https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem.git
cd Trad-Chem

# Install in development mode
pip install -e .
```

### **Installation with Analysis Dependencies**
```bash
pip install -e ".[analysis]"
```

### **Development Installation**
```bash
git clone https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem.git
cd Trad-Chem
pip install -e ".[dev]"
```

## 🎯 **Quick Start**

### **Basic Usage**
```python
from tradchem import TradChem

# Initialize TradChem
tc = TradChem()

# Load traditional medicine data
medicines = tc.load_data('medicines.csv')

# Perform basic analysis
analysis = tc.analyze_medicines(medicines)

# Analyze chemical structures
chemical_analysis = tc.analyze_chemical_structures(medicines)

# Generate statistical summary
stats = tc.statistical_analysis(medicines)

# Export results
tc.export_data(analysis, 'results.json')
```

### **Command Line Interface**
```bash
# Basic analysis
python -m tradchem.cli analyze --file medicines.csv

# Chemical analysis
python -m tradchem.cli chemical --file medicines.csv

# Generate report
python -m tradchem.cli report --file medicines.csv --output report.html
```

## 📚 **Google Colab Integration**

TradChem is fully compatible with Google Colab! Since the package is not yet published on PyPI, use our special installation method:

### **🚀 Quick Colab Setup**
```python
# Copy and paste this entire code block into a Colab cell
import subprocess
import sys
import os
from pathlib import Path

print("🧹 Clean TradChem Installation for Colab")
print("=" * 50)

# Remove existing installation
try:
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "tradchem", "-y"])
except:
    pass

import shutil
if os.path.exists("/content/Trad-Chem"):
    shutil.rmtree("/content/Trad-Chem")

# Install dependencies
dependencies = ["numpy", "pandas", "scipy", "matplotlib", "seaborn", "scikit-learn", "jsonschema", "pydantic"]
for dep in dependencies:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
    except:
        pass

# Clone and install
subprocess.check_call(["git", "clone", "https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem.git", "/content/Trad-Chem"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "/content/Trad-Chem"])

# Test installation
from tradchem import TradChem
tc = TradChem()
print("✅ TradChem is ready!")
```

### **🎓 Learning Paths**
1. **[Basic Usage Tutorial](colab_examples/tradchem_basic_usage.ipynb)** - Start here for beginners
2. **[Chemical Analysis Tutorial](colab_examples/tradchem_chemical_analysis.ipynb)** - Advanced chemical analysis
3. **[Quick Start Script](colab_examples/quick_start.py)** - Fast results

### **🧠 Knowledge Graph Navigation**
- **[TradChem Knowledge Graph](colab_examples/TRADCHEM_KNOWLEDGE_GRAPH.md)** - Complete component overview and navigation guide

### **📖 Installation Guide**
- **[Colab Installation Guide](COLAB_INSTALLATION_GUIDE.md)** - Detailed Colab setup instructions
- **[Colab Integration Guide](COLAB_INTEGRATION.md)** - Google Colab setup and usage

## 📖 **Documentation**

### **📚 Comprehensive Guides**
- **[TradChem Knowledge Graph](colab_examples/TRADCHEM_KNOWLEDGE_GRAPH.md)** - Interactive component navigation
- **[Colab Integration Guide](COLAB_INTEGRATION.md)** - Google Colab setup and usage
- **[Contribution Guide](CONTRIBUTING_PYTHON_PACKAGE.md)** - How to contribute to TradChem
- **[Colab Installation Guide](COLAB_INSTALLATION_GUIDE.md)** - Detailed Colab setup

### **🎯 Component Documentation**
- **🔍 Data Loading & Validation**: Load and validate traditional medicine data
- **🧪 Chemical Structure Analysis**: Analyze molecular structures and properties
- **📈 Statistical Analysis**: Perform statistical analysis on traditional medicine data
- **🎯 Traditional Medicine Analysis**: Analyze traditional medicine systems
- **🛠️ Utility Components**: Data processing, SMILES utilities, and visualization tools

### **📋 Examples and Tutorials**
- **[Basic Usage Examples](examples/)** - Simple usage examples
- **[Colab Tutorials](colab_examples/)** - Interactive Google Colab notebooks
- **[Sample Data](examples/sample_medicines.csv)** - Sample traditional medicine data

## 🤝 **Contributing**

We welcome contributions from the community! TradChem is built for researchers, developers, and traditional medicine enthusiasts.

### **🎯 Types of Contributions**
- **Code Contributions**: Bug fixes, new features, improvements
- **Data Contributions**: Traditional medicine data, chemical structures, research data
- **Documentation**: Tutorials, examples, API documentation
- **Community**: Discussions, issue reporting, code review

### **📋 Getting Started**
1. **Read the [Contribution Guide](CONTRIBUTING_PYTHON_PACKAGE.md)** - Comprehensive guide for contributors
2. **Explore the [Knowledge Graph](colab_examples/TRADCHEM_KNOWLEDGE_GRAPH.md)** - Understand TradChem components
3. **Check [Issues](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/issues)** - Find areas to contribute
4. **Join [Discussions](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/discussions)** - Connect with the community

### **🛠️ Development Setup**
```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/Trad-Chem.git
cd Trad-Chem

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"

# Set up pre-commit hooks
pre-commit install
```

### **📊 Data Contributions**
- **Traditional Medicine Data**: Add new medicines and compounds
- **Chemical Structures**: Add SMILES notations and molecular data
- **Research Data**: Add scientific references and studies
- **Cultural Data**: Add traditional medicine system information

For detailed contribution guidelines, see [CONTRIBUTING_PYTHON_PACKAGE.md](CONTRIBUTING_PYTHON_PACKAGE.md).

## 🎯 **Use Cases**

### **🏥 Healthcare Research**
- Analyze traditional medicine efficacy
- Study chemical compositions
- Research alternative treatments
- Understand traditional healing practices

### **🧬 Drug Discovery**
- Screen traditional compounds
- Analyze molecular properties
- Identify potential drug candidates
- Understand structure-activity relationships

### **🌍 Cultural Studies**
- Study traditional medicine systems
- Analyze cultural practices
- Understand geographic distributions
- Research historical medicine practices

### **📊 Data Science**
- Data analysis and visualization
- Statistical modeling
- Machine learning applications
- Research data processing

## 📊 **Data Format**

TradChem supports multiple data formats:

### **JSON Format**
```json
{
  "product_name": "Turmeric Extract",
  "scientific_name": "Curcuma longa",
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
}
```

### **CSV Format**
```csv
product_name,scientific_name,traditional_system,geographic_origin,benefits,diseases
Turmeric Extract,Curcuma longa,Ayurveda,India,"Anti-inflammatory,Antioxidant","Arthritis,Digestive disorders"
```

## 🧪 **Testing**

```bash
# Run all tests
pytest

# Run specific test categories
pytest tests/test_tradchem.py
pytest tests/test_chemical_analysis.py
pytest tests/test_statistical_analysis.py
```

## 📈 **Performance**

TradChem is optimized for:
- **Large datasets**: Efficient processing of thousands of medicines
- **Chemical analysis**: Fast SMILES validation and property calculation
- **Statistical analysis**: Optimized algorithms for data analysis
- **Visualization**: High-quality plots and charts

## 🔧 **Configuration**

TradChem can be configured through environment variables:

```bash
# Set database path
export TRADCHEM_DB_PATH=/path/to/database.json

# Set logging level
export TRADCHEM_LOG_LEVEL=INFO

# Enable debug mode
export TRADCHEM_DEBUG=true
```

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 **Acknowledgments**

- **Traditional Medicine Researchers**: For sharing knowledge and data
- **Chemical Analysis Community**: For tools and methodologies
- **Open Source Contributors**: For building amazing tools
- **Scientific Community**: For advancing traditional medicine research

## 📞 **Support**

- **Documentation**: [TradChem Knowledge Graph](colab_examples/TRADCHEM_KNOWLEDGE_GRAPH.md)
- **Issues**: [GitHub Issues](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/issues)
- **Discussions**: [GitHub Discussions](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/discussions)
- **Email**: contributors@tradchem.org

---

**🌿 TradChem** - Bridging traditional wisdom with modern analysis

*Built with ❤️ for the traditional medicine research community* 