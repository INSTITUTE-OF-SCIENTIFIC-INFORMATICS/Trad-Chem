# 🌿 TradChem - Traditional Medicine Chemical Database

**TradChem** is a comprehensive Python package for traditional medicine chemical database management and analysis. It provides tools for working with traditional medicine data, chemical structures (SMILES), and scientific analysis of traditional medicinal compounds.

## 🚀 **Quick Start**

### **Installation**

```bash
# Install from PyPI
pip install tradchem

# Install with analysis dependencies
pip install tradchem[analysis]

# Install from source
git clone https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem.git
cd Trad-Chem
pip install -e .
```

### **🌐 Google Colab**

TradChem works seamlessly in Google Colab! Here are the easiest ways to get started:

#### **Option 1: Automatic Setup (Recommended)**
```python
# Run this in a Colab cell
!git clone https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem.git
!pip install -e Trad-Chem/
!pip install rdkit-pypi  # For chemical analysis

# Start using TradChem
from tradchem import TradChem
tc = TradChem()
```

#### **Option 2: Quick Installation Script**
```python
# Download and run the installation script
!wget https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/colab_install.py
!python colab_install.py
```

#### **Option 3: Manual Installation**
```python
# Install dependencies
!pip install tradchem pandas matplotlib seaborn numpy
!pip install rdkit-pypi  # For chemical analysis

# Import and use
from tradchem import TradChem
tc = TradChem()
```

#### **📚 Colab Examples**
- **[Setup Notebook](colab_examples/colab_setup.ipynb)**: Automatic installation and configuration
- **[Basic Usage](colab_examples/tradchem_basic_usage.ipynb)**: Data exploration and analysis
- **[Chemical Analysis](colab_examples/tradchem_chemical_analysis.ipynb)**: Advanced cheminformatics
- **[Quick Start](colab_examples/quick_start.py)**: Python script for immediate use

### **Basic Usage**

```python
from tradchem import TradChem

# Initialize the database
tc = TradChem()

# Search for medicines
medicines = tc.search_medicines("turmeric")
print(f"Found {len(medicines)} medicines")

# Get medicine details
medicine = tc.get_medicine("turmeric")
print(f"Scientific name: {medicine.scientific_name}")
print(f"Benefits: {medicine.benefits}")

# Search by chemical structure
results = tc.search_by_smiles("CC1=CC(=C(C=C1)O)C(=O)O")
print(f"Found {len(results)} compounds with similar structure")

# Get statistics
stats = tc.get_statistics()
print(f"Total medicines: {stats['total_medicines']}")
```

### **Command Line Interface**

```bash
# Search medicines
tradchem search "ashwagandha"

# Get medicine details
tradchem info "turmeric"

# Export data
tradchem export --format csv --output medicines.csv

# Add new medicine
tradchem add --file medicine_data.json
```

## 📊 **Data Contribution**

We welcome contributions of traditional medicine data. Here are the ways to contribute:

### **1. 📄 CSV Template (Recommended for Bulk Data)**
```bash
# Download the template
python -m tradchem.cli template --file my_medicines.csv

# Fill in your data and submit a Pull Request
```

### **2. 📋 JSON Format (Developer Friendly)**
```json
{
  "product_name": "Turmeric",
  "scientific_name": "Curcuma longa",
  "description": "Golden spice with anti-inflammatory properties",
  "traditional_system": "Ayurvedic Medicine",
  "benefits": ["Anti-inflammatory", "Antioxidant"],
  "chemical_components": [
    {
      "name": "Curcumin",
      "smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
      "molecular_weight": 368.38
    }
  ]
}
```

### **3. 🐛 GitHub Issues (Quick Contribution)**
- Use our Issue template
- Fill in the medicine information
- After community review, it will be added

### **📚 Detailed Contribution Guides**
- [📊 Complete Data Contribution Guide](CONTRIBUTING_DATA.md)
- [📁 Contribution Directory Overview](contributions/README.md)
- [📋 Data Quality Standards](contributions/guidelines/data_quality.md)
- [🧪 SMILES Guidelines](contributions/guidelines/smiles_guidelines.md)
- [📚 Citation Standards](contributions/guidelines/citation_standards.md)

## 🌟 **Main Features**

### **🔍 Advanced Search**
- Search by medicine name, scientific name
- Search by therapeutic benefits
- Search by traditional medicine system
- Chemical structure search using SMILES

### **📊 Data Analysis**
- Chemical structure analysis
- Molecular property calculations
- Traditional medicine system comparison
- Statistical analysis and reporting

### **🧪 Chemical Informatics**
- SMILES notation support
- Molecular weight calculations
- Chemical structure validation
- Structure-activity relationship analysis

### **📈 Data Management**
- Import/export in multiple formats (CSV, JSON)
- Data validation and quality checks
- Version control for data updates
- Backup and restore functionality

## 🏗️ **Package Structure**

```
TradChem/
├── tradchem/              # Core package
│   ├── __init__.py        # Package initialization
│   ├── tradchem.py        # Main database class
│   ├── cli.py             # Command line interface
│   ├── version.py         # Version information
│   ├── data/              # Data storage
│   │   └── tradchem_database.json
│   ├── utils/             # Utility functions
│   │   ├── data_utils.py  # Data processing utilities
│   │   └── smiles_utils.py # SMILES processing
│   ├── medicine_systems/  # Traditional medicine systems
│   │   └── ayurvedic.py   # Ayurvedic medicine data
│   └── tests/             # Test suite
│       └── test_tradchem.py
├── examples/              # Example data and scripts
├── contributions/         # Data contribution templates
├── setup.py              # Package setup
├── requirements.txt      # Dependencies
└── README.md            # This file
```

## 🔧 **Dependencies**

### **Core Dependencies**
- `numpy>=1.21.0` - Numerical computing
- `pandas>=1.3.0` - Data manipulation
- `scipy>=1.7.0` - Scientific computing
- `jsonschema>=3.2.0` - Data validation
- `pydantic>=1.8.0` - Data models

### **Optional Dependencies**
- `rdkit-pypi>=2022.9.1` - Cheminformatics (install with `[analysis]`)
- `matplotlib>=3.4.0` - Data visualization
- `seaborn>=0.11.0` - Statistical visualization
- `scikit-learn>=0.24.0` - Machine learning

## 📚 **Supported Traditional Medicine Systems**

### **🌿 Ayurvedic Medicine**
- Indian traditional medicine system
- Based on the theory of three doshas
- Emphasizes mind-body balance

### **🏮 Traditional Chinese Medicine (TCM)**
- Chinese traditional medicine
- Yin-Yang and Five Elements theory
- Holistic treatment approach

### **🌍 Unani Medicine**
- Islamic traditional medicine
- Four humors theory
- Greco-Arabic medical tradition

### **🌱 African Traditional Medicine**
- Traditional medicine of the African continent
- Community-based treatment
- Use of indigenous plants

### **🌿 Indigenous Medicine**
- Indigenous traditional medicine worldwide
- Ecosystem integration
- Cultural heritage healing

## 🔬 **Research Applications**

### **Drug Discovery**
- Screening of traditional medicine molecules
- Identification of active ingredients
- Guidance for new drug development

### **Traditional Medicine Research**
- Digitization of traditional knowledge
- Cross-cultural medical comparison
- Historical medical literature analysis

### **Clinical Research**
- Efficacy validation of traditional medicines
- Safety assessment
- Integration with modern medicine

## 📈 **Data Statistics**

- **Traditional medicine systems**: 5+ (Ayurvedic, TCM, Unani, etc.)
- **Medicine records**: 1000+ traditional medicines
- **Chemical components**: 5000+ SMILES structures
- **Benefit categories**: 50+ therapeutic categories

## 🤝 **Contribution Guide**

### **Ways to Contribute**
1. **Data Contribution**: Add traditional medicine data
2. **Code Contribution**: Improve features and fix bugs
3. **Documentation**: Improve docs and guides
4. **Community Support**: Answer questions and help users

### **Contribution Process**
1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Create a Pull Request

### **Contributor Benefits**
- Contributor list display
- Data ownership protection
- Community badge rewards
- Research citation support

## 📞 **Community Support**

### **Get Help**
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Technical Q&A
- **Documentation**: Detailed user guides
- **Examples**: Real-world use cases

### **Learning Resources**
- [API Documentation](https://tradchem.readthedocs.io/)
- [Tutorials](examples/)
- [Data Contribution Guide](CONTRIBUTING_DATA.md)

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 **Acknowledgments**

- **Traditional Medicine Community**: For knowledge and data
- **Scientific Community**: For research and validation
- **Contributors**: For code contributions and feedback
- **Open Source Community**: For tools and libraries

---

**Built with ❤️ by SaltyHeart**

*Empowering traditional medicine research with modern technology* 