# 🤝 Contributing to TradChem Python Package

Thank you for your interest in contributing to TradChem! This guide provides comprehensive information for contributors who want to help improve the traditional medicine chemical analysis package.

## 📋 **Table of Contents**

- [Types of Contributions](#types-of-contributions)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Code Contribution Guidelines](#code-contribution-guidelines)
- [Data Contribution Guidelines](#data-contribution-guidelines)
- [Testing Guidelines](#testing-guidelines)
- [Documentation Guidelines](#documentation-guidelines)
- [Pull Request Process](#pull-request-process)
- [Community Guidelines](#community-guidelines)
- [Recognition](#recognition)

## 🎯 **Types of Contributions**

### **💻 Code Contributions**
- **Bug Fixes**: Fix issues and improve stability
- **New Features**: Add new analysis capabilities
- **Performance Improvements**: Optimize existing code
- **Code Refactoring**: Improve code structure and readability
- **Testing**: Add tests and improve test coverage

### **📊 Data Contributions**
- **Traditional Medicine Data**: Add new medicines and compounds
- **Chemical Structures**: Add SMILES notations and molecular data
- **Research Data**: Add scientific references and studies
- **Cultural Data**: Add traditional medicine system information

### **📚 Documentation Contributions**
- **Tutorials**: Create learning materials and examples
- **API Documentation**: Improve function and class documentation
- **User Guides**: Create comprehensive usage guides
- **Knowledge Graph**: Expand the component navigation system

### **🌍 Community Contributions**
- **Issue Reporting**: Report bugs and suggest improvements
- **Code Review**: Review pull requests and provide feedback
- **Discussions**: Participate in community discussions
- **Outreach**: Help spread awareness about TradChem

## 🚀 **Getting Started**

### **1. Understand the Project**

Before contributing, familiarize yourself with TradChem:

- **Read the [Knowledge Graph](colab_examples/TRADCHEM_KNOWLEDGE_GRAPH.md)** - Understand all components
- **Explore the [README](README.md)** - Get an overview of the project
- **Check [Issues](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/issues)** - Find areas to contribute
- **Join [Discussions](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/discussions)** - Connect with the community

### **2. Choose Your Contribution Type**

- **Beginner**: Start with documentation, testing, or simple bug fixes
- **Intermediate**: Work on features, data contributions, or tutorials
- **Advanced**: Contribute to core algorithms, performance optimization, or new analysis methods

### **3. Set Up Your Development Environment**

Follow the [Development Setup](#development-setup) section below.

## 🛠️ **Development Setup**

### **Prerequisites**

- Python 3.7 or higher
- Git
- pip or conda
- (Optional) RDKit for chemical analysis features

### **Step 1: Fork and Clone**

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/Trad-Chem.git
cd Trad-Chem

# Add the original repository as upstream
git remote add upstream https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem.git
```

### **Step 2: Create Virtual Environment**

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### **Step 3: Install Dependencies**

```bash
# Install in development mode
pip install -e ".[dev]"

# Install additional development tools
pip install pre-commit black isort flake8 pytest pytest-cov
```

### **Step 4: Set Up Pre-commit Hooks**

```bash
# Install pre-commit hooks
pre-commit install

# Run pre-commit on all files
pre-commit run --all-files
```

### **Step 5: Verify Installation**

```bash
# Run tests to ensure everything works
pytest

# Test the package
python -c "from tradchem import TradChem; tc = TradChem(); print('✅ Setup complete!')"
```

## 📝 **Code Contribution Guidelines**

### **Code Style**

TradChem follows PEP 8 style guidelines with some modifications:

```python
# Use descriptive variable names
medicine_data = load_medicine_data()
chemical_analysis = analyze_chemical_structures(medicines)

# Use type hints
def analyze_medicines(medicines: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze traditional medicine data.
    
    Args:
        medicines: List of medicine dictionaries
        
    Returns:
        Dictionary containing analysis results
    """
    pass

# Use docstrings for all functions and classes
class TradChem:
    """Traditional medicine chemical analysis package.
    
    A comprehensive class for analyzing traditional medicine data,
    chemical structures, and molecular properties.
    """
    
    def __init__(self, database_path: Optional[str] = None):
        """Initialize TradChem with optional database path.
        
        Args:
            database_path: Path to the traditional medicine database
        """
        pass
```

### **File Organization**

```
tradchem/
├── __init__.py              # Package initialization
├── tradchem.py              # Main TradChem class
├── version.py               # Version information
├── cli.py                   # Command-line interface
├── utils/                   # Utility modules
│   ├── __init__.py
│   ├── smiles_utils.py      # SMILES utilities
│   └── data_utils.py        # Data processing utilities
├── medicine_systems/        # Traditional medicine systems
│   ├── __init__.py
│   └── ayurvedic.py         # Ayurvedic medicine analysis
└── tests/                   # Test files
    ├── __init__.py
    ├── test_tradchem.py     # Main tests
    ├── test_chemical.py     # Chemical analysis tests
    └── test_utils.py        # Utility tests
```

### **Adding New Features**

1. **Create a feature branch**
   ```bash
   git checkout -b feature/new-analysis-method
   ```

2. **Implement the feature**
   ```python
   # Add new method to TradChem class
   def new_analysis_method(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
       """Perform new analysis on traditional medicine data.
       
       Args:
           data: List of medicine dictionaries
           
       Returns:
           Dictionary containing analysis results
       """
       # Implementation here
       pass
   ```

3. **Add tests**
   ```python
   # tests/test_tradchem.py
   def test_new_analysis_method():
       """Test the new analysis method."""
       tc = TradChem()
       test_data = [{"product_name": "Test Medicine"}]
       result = tc.new_analysis_method(test_data)
       assert isinstance(result, dict)
   ```

4. **Update documentation**
   - Add docstring
   - Update README if needed
   - Add to knowledge graph

### **Bug Fixes**

1. **Create a bug fix branch**
   ```bash
   git checkout -b fix/bug-description
   ```

2. **Write a test that reproduces the bug**
   ```python
   def test_bug_reproduction():
       """Test that reproduces the bug."""
       tc = TradChem()
       # Test case that fails
       pass
   ```

3. **Fix the bug**
   ```python
   # Fix the implementation
   def fixed_method(self):
       # Fixed implementation
       pass
   ```

4. **Ensure the test passes**
   ```bash
   pytest tests/test_tradchem.py::test_bug_reproduction
   ```

## 📊 **Data Contribution Guidelines**

### **Traditional Medicine Data Format**

```json
{
  "product_name": "Turmeric Extract",
  "scientific_name": "Curcuma longa",
  "description": "Traditional medicine used for anti-inflammatory properties",
  "traditional_system": "Ayurveda",
  "geographic_origin": "India",
  "benefits": ["Anti-inflammatory", "Antioxidant", "Digestive aid"],
  "diseases": ["Arthritis", "Digestive disorders"],
  "chemical_composition": {
    "ingredients": {
      "Curcumin": {
        "smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
        "molecular_weight": 368.38,
        "formula": "C21H20O6",
        "cas_number": "458-37-7"
      }
    }
  },
  "references": [
    {
      "title": "Curcumin: A Review of Its Effects on Human Health",
      "authors": ["Aggarwal BB", "Harikumar KB"],
      "journal": "Foods",
      "year": 2017,
      "doi": "10.3390/foods6100092"
    }
  ]
}
```

### **Data Quality Standards**

1. **Accuracy**: Ensure all data is accurate and verified
2. **Completeness**: Provide as much information as possible
3. **Consistency**: Follow the established data format
4. **References**: Include scientific references when available
5. **Validation**: Validate SMILES notations and molecular data

### **Submitting Data Contributions**

1. **Create a data file**
   ```bash
   # Create data file
   touch data/new_medicines.json
   ```

2. **Add your data**
   ```json
   [
     {
       "product_name": "Your Medicine",
       "scientific_name": "Scientific Name",
       // ... other fields
     }
   ]
   ```

3. **Validate the data**
   ```python
   from tradchem import TradChem
   tc = TradChem()
   
   # Load and validate
   medicines = tc.load_data('data/new_medicines.json')
   validation = tc.validate_data(medicines)
   print(f"Data quality: {validation['data_quality_score']:.2%}")
   ```

4. **Submit via pull request**

## 🧪 **Testing Guidelines**

### **Running Tests**

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_tradchem.py

# Run with coverage
pytest --cov=tradchem

# Run with verbose output
pytest -v
```

### **Writing Tests**

```python
# tests/test_tradchem.py
import pytest
from tradchem import TradChem

class TestTradChem:
    """Test cases for TradChem class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.tc = TradChem()
        self.sample_data = [
            {
                "product_name": "Test Medicine",
                "benefits": ["Test Benefit"],
                "diseases": ["Test Disease"]
            }
        ]
    
    def test_initialization(self):
        """Test TradChem initialization."""
        assert self.tc is not None
        assert hasattr(self.tc, 'data')
    
    def test_load_data(self):
        """Test data loading functionality."""
        # Test implementation
        pass
    
    def test_validate_data(self):
        """Test data validation."""
        validation = self.tc.validate_data(self.sample_data)
        assert validation['total_medicines'] == 1
        assert validation['valid_medicines'] == 1
    
    def test_search_medicines(self):
        """Test medicine search functionality."""
        results = self.tc.search_medicines("Test", limit=5)
        assert isinstance(results, list)
```

### **Test Categories**

1. **Unit Tests**: Test individual functions and methods
2. **Integration Tests**: Test how components work together
3. **Data Tests**: Test data loading and validation
4. **Performance Tests**: Test performance with large datasets
5. **Edge Case Tests**: Test boundary conditions and error handling

## 📚 **Documentation Guidelines**

### **Code Documentation**

```python
def analyze_chemical_structures(self, medicines: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze chemical structures in traditional medicine data.
    
    This method analyzes the chemical composition of traditional medicines,
    including SMILES validation, molecular property calculations, and
    chemical diversity analysis.
    
    Args:
        medicines: List of medicine dictionaries containing chemical composition data
        
    Returns:
        Dictionary containing analysis results with the following keys:
        - total_compounds: Total number of chemical compounds
        - valid_smiles: Number of valid SMILES notations
        - invalid_smiles: Number of invalid SMILES notations
        - avg_molecular_weight: Average molecular weight
        - unique_formulas: Number of unique chemical formulas
        
    Raises:
        ValueError: If medicines data is invalid
        KeyError: If required chemical composition fields are missing
        
    Example:
        >>> tc = TradChem()
        >>> medicines = [{"chemical_composition": {"ingredients": {"Curcumin": {"smiles": "CC1=CC(=C(C=C1)O)C(=O)O"}}}}]
        >>> analysis = tc.analyze_chemical_structures(medicines)
        >>> print(analysis['total_compounds'])
        1
    """
    pass
```

### **Tutorial Documentation**

Create tutorials in the `colab_examples/` directory:

```python
# colab_examples/tutorial_name.ipynb
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Tutorial Title\n",
    "\n",
    "This tutorial demonstrates how to use TradChem for specific analysis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Installation\n",
    "!pip install tradchem\n",
    "\n",
    "# Import\n",
    "from tradchem import TradChem\n",
    "tc = TradChem()"
   ]
  }
 ]
}
```

### **Knowledge Graph Updates**

Update the knowledge graph when adding new features:

```markdown
# colab_examples/TRADCHEM_KNOWLEDGE_GRAPH.md

## New Feature Section

### 🆕 **New Analysis Method**
**Purpose**: Describe what the new feature does

**Components**:
- `TradChem.new_method()` - Brief description

**Use When**:
- When you need to do X
- When you want to analyze Y

**Example**:
```python
result = tc.new_method(data)
```
```

## 🔄 **Pull Request Process**

### **1. Prepare Your Changes**

```bash
# Ensure you're on your feature branch
git checkout feature/your-feature

# Make your changes
# ... edit files ...

# Add your changes
git add .

# Commit with descriptive message
git commit -m "Add new chemical analysis method

- Implement molecular property calculation
- Add SMILES validation improvements
- Update documentation and tests

Fixes #123"
```

### **2. Update Your Branch**

```bash
# Pull latest changes from upstream
git fetch upstream
git rebase upstream/main

# Push your changes
git push origin feature/your-feature
```

### **3. Create Pull Request**

1. Go to your fork on GitHub
2. Click "New Pull Request"
3. Select your feature branch
4. Fill out the pull request template:

```markdown
## Description
Brief description of your changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Data contribution
- [ ] Other (please describe)

## Testing
- [ ] Tests pass locally
- [ ] Added new tests
- [ ] Updated existing tests

## Documentation
- [ ] Updated docstrings
- [ ] Updated README
- [ ] Updated knowledge graph
- [ ] Added tutorials

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] No breaking changes
- [ ] All tests pass
```

### **4. Review Process**

1. **Automated Checks**: CI/CD will run tests and style checks
2. **Code Review**: Maintainers will review your code
3. **Feedback**: Address any feedback or requested changes
4. **Merge**: Once approved, your changes will be merged

## 🌍 **Community Guidelines**

### **Code of Conduct**

- **Be Respectful**: Treat all contributors with respect
- **Be Inclusive**: Welcome contributors from all backgrounds
- **Be Helpful**: Help others learn and contribute
- **Be Patient**: Understand that everyone learns at their own pace

### **Communication**

- **Issues**: Use GitHub issues for bug reports and feature requests
- **Discussions**: Use GitHub discussions for questions and ideas
- **Pull Requests**: Use pull requests for code contributions
- **Email**: Use contributors@tradchem.org for private matters

### **Getting Help**

- **Documentation**: Check the knowledge graph and tutorials
- **Issues**: Search existing issues for similar problems
- **Discussions**: Ask questions in GitHub discussions
- **Community**: Connect with other contributors

## 🏆 **Recognition**

### **Contributor Recognition**

- **Contributors List**: All contributors are listed in the README
- **Release Notes**: Contributors are credited in release notes
- **Documentation**: Contributors are acknowledged in documentation
- **Community**: Recognition in community discussions

### **Types of Recognition**

- **Code Contributors**: Listed in contributors section
- **Data Contributors**: Acknowledged in data documentation
- **Documentation Contributors**: Credited in tutorials and guides
- **Community Contributors**: Recognized for community support

### **Contributor Levels**

- **New Contributor**: First contribution
- **Regular Contributor**: Multiple contributions
- **Core Contributor**: Significant contributions
- **Maintainer**: Long-term project leadership

## 📞 **Support and Resources**

### **Getting Started Resources**

- **[Knowledge Graph](colab_examples/TRADCHEM_KNOWLEDGE_GRAPH.md)**: Complete component overview
- **[Basic Tutorial](colab_examples/tradchem_basic_usage.ipynb)**: Beginner-friendly tutorial
- **[Chemical Analysis Tutorial](colab_examples/tradchem_chemical_analysis.ipynb)**: Advanced features
- **[Examples](examples/)**: Code examples and sample data

### **Development Resources**

- **[Issues](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/issues)**: Bug reports and feature requests
- **[Discussions](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/discussions)**: Community discussions
- **[Wiki](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/wiki)**: Development documentation

### **Contact Information**

- **Email**: contributors@tradchem.org
- **GitHub**: [@INSTITUTE-OF-SCIENTIFIC-INFORMATICS](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS)
- **Discussions**: [GitHub Discussions](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/discussions)

---

**🤝 Thank you for contributing to TradChem!**

*Your contributions help advance traditional medicine research and make this knowledge accessible to everyone.* 