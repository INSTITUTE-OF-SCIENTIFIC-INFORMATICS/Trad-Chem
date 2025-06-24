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

### **Basic Installation**
```bash
pip install tradchem
```

### **Installation with Analysis Dependencies**
```bash
pip install tradchem[analysis]
```

### **Development Installation**
```bash
git clone https://github.com/SaltyHeart/Trad-Chem.git
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

TradChem is fully compatible with Google Colab! Check out our comprehensive tutorials:

### **🎓 Learning Paths**
1. **[Basic Usage Tutorial](colab_examples/tradchem_basic_usage.ipynb)** - Start here for beginners
2. **[Chemical Analysis Tutorial](colab_examples/tradchem_chemical_analysis.ipynb)** - Advanced chemical analysis
3. **[Quick Start Script](colab_examples/quick_start.py)** - Fast results

### **🧠 Knowledge Graph Navigation**
- **[TradChem Knowledge Graph](colab_examples/TRADCHEM_KNOWLEDGE_GRAPH.md)** - Complete component overview and navigation guide

### **🚀 Quick Colab Setup**
```python
# Install TradChem in Colab
!pip install tradchem

# Import and start analyzing
from tradchem import TradChem
tc = TradChem()
```

## 📖 **Documentation**

### **📚 Comprehensive Guides**
- **[TradChem Knowledge Graph](colab_examples/TRADCHEM_KNOWLEDGE_GRAPH.md)** - Interactive component navigation
- **[Colab Integration Guide](COLAB_INTEGRATION.md)** - Google Colab setup and usage
- **[Contribution Guide](CONTRIBUTING_PYTHON_PACKAGE.md)** - How to contribute to TradChem

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
3. **Check [Issues](https://github.com/SaltyHeart/Trad-Chem/issues)** - Find areas to contribute
4. **Join [Discussions](https://github.com/SaltyHeart/Trad-Chem/discussions)** - Connect with the community

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

### **Supported Input Formats**
- **CSV**: Comma-separated values with traditional medicine data
- **JSON**: Structured data with chemical information
- **Excel**: Spreadsheet data with multiple sheets

### **Chemical Data Requirements**
- **SMILES Notation**: Canonical SMILES format for chemical structures
- **Molecular Properties**: Weight, formula, CAS numbers, PubChem IDs
- **Validation**: Automatic SMILES validation and canonicalization

### **Sample Data Structure**
```json
{
  "product_name": "Traditional Medicine",
  "scientific_name": "Scientific Name",
  "traditional_system": "Ayurvedic Medicine",
  "geographic_origin": "India",
  "benefits": ["Benefit 1", "Benefit 2"],
  "chemical_composition": {
    "ingredients": {
      "Active Compound": {
        "smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
        "molecular_weight": 368.38,
        "cas_number": "458-37-7",
        "pubchem_id": "969516"
      }
    }
  }
}
```

## 🔧 **Dependencies**

### **Core Dependencies**
- **Python**: 3.8 or higher
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Basic plotting and visualization

### **Analysis Dependencies**
- **RDKit**: Chemical structure analysis and molecular properties
- **Seaborn**: Advanced statistical visualizations
- **SciPy**: Scientific computing and statistics

### **Development Dependencies**
- **Pytest**: Testing framework
- **Black**: Code formatting
- **Flake8**: Code linting
- **MyPy**: Type checking

## 📈 **Performance**

- **Data Loading**: Optimized for large traditional medicine datasets
- **Chemical Analysis**: Efficient SMILES processing and molecular calculations
- **Statistical Analysis**: Fast statistical computations and correlations
- **Visualization**: Responsive plotting for interactive analysis

## 🌟 **Highlights**

- **🌿 Traditional Medicine Focus**: Specialized for traditional medicine analysis
- **🧪 Chemical Intelligence**: Advanced molecular property calculations
- **📊 Statistical Power**: Comprehensive statistical analysis capabilities
- **🎨 Beautiful Visualizations**: Apple Design-inspired UI and plots
- **🚀 Google Colab Ready**: Seamless integration with Google Colab
- **🤝 Community Driven**: Open source with active community support
- **📚 Comprehensive Documentation**: Extensive guides and tutorials
- **🛠️ Extensible Architecture**: Easy to extend and customize

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 **Acknowledgments**

- **Traditional Medicine Communities**: For preserving and sharing traditional knowledge
- **Scientific Community**: For developing the tools and methods that make this possible
- **Open Source Contributors**: For building the foundation libraries and tools
- **Research Institutions**: For advancing our understanding of traditional medicines

## 📞 **Support**

- **📖 Documentation**: [Knowledge Graph](colab_examples/TRADCHEM_KNOWLEDGE_GRAPH.md) and [Contribution Guide](CONTRIBUTING_PYTHON_PACKAGE.md)
- **🐛 Issues**: [GitHub Issues](https://github.com/SaltyHeart/Trad-Chem/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/SaltyHeart/Trad-Chem/discussions)
- **📧 Email**: For sensitive or private matters

## 🌟 **Star History**

[![Star History Chart](https://api.star-history.com/svg?repos=SaltyHeart/Trad-Chem&type=Date)](https://star-history.com/#SaltyHeart/Trad-Chem&Date)

---

**Built with ❤️ by the TradChem Community**

*Empowering traditional medicine research through modern chemical analysis* 🌿🧪📊 