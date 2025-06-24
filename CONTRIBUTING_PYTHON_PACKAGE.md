# 🤝 Contributing to TradChem Python Package

Thank you for your interest in contributing to TradChem! This guide will help you understand how to contribute to the Python package, whether you're adding code, data, documentation, or helping with testing.

## 📋 **Table of Contents**

- [Types of Contributions](#types-of-contributions)
- [Development Setup](#development-setup)
- [Code Contributions](#code-contributions)
- [Data Contributions](#data-contributions)
- [Documentation Contributions](#documentation-contributions)
- [Testing Contributions](#testing-contributions)
- [Pull Request Process](#pull-request-process)
- [Code of Conduct](#code-of-conduct)

## 🎯 **Types of Contributions**

### **Code Contributions**
- 🐛 **Bug fixes** - Fix issues and improve reliability
- ✨ **New features** - Add new functionality to the package
- 🔧 **Improvements** - Enhance existing features
- 🧪 **Testing** - Add or improve test coverage
- 📊 **Analysis tools** - Add new analysis methods

### **Data Contributions**
- 🌿 **Traditional medicine data** - Add new medicines and compounds
- 🧪 **Chemical structures** - Add SMILES notations and molecular data
- 📚 **Research data** - Add scientific references and studies
- 🌍 **Cultural data** - Add traditional medicine system information

### **Documentation Contributions**
- 📖 **API documentation** - Improve code documentation
- 🎓 **Tutorials** - Create learning materials
- 📚 **Examples** - Add usage examples and notebooks
- 🌐 **Website content** - Improve project documentation

### **Community Contributions**
- 💬 **Discussions** - Participate in GitHub discussions
- 🐛 **Issue reporting** - Report bugs and suggest features
- 🔍 **Code review** - Review pull requests
- 📢 **Outreach** - Help spread the word about TradChem

## 🛠️ **Development Setup**

### **Prerequisites**
- Python 3.8 or higher
- Git
- pip or conda

### **Local Development Setup**

```bash
# 1. Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/Trad-Chem.git
cd Trad-Chem

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install development dependencies
pip install -e ".[dev]"

# 4. Install additional development tools
pip install pre-commit black isort mypy

# 5. Set up pre-commit hooks
pre-commit install
```

### **Development Dependencies**

```bash
# Install all development dependencies
pip install -e ".[dev,docs,analysis]"

# Or install individually
pip install pytest pytest-cov black flake8 mypy
pip install sphinx sphinx-rtd-theme
pip install rdkit-pypi pandas matplotlib seaborn
```

### **IDE Setup**

#### **VS Code Configuration**
Create `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false
}
```

#### **PyCharm Configuration**
- Set project interpreter to your virtual environment
- Enable code inspection and formatting
- Configure pytest as test runner

## 💻 **Code Contributions**

### **Code Style Guidelines**

#### **Python Code Style**
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use Black for code formatting (line length: 88 characters)
- Use type hints for all function parameters and return values
- Write docstrings for all public functions and classes

#### **Example Code Structure**
```python
from typing import List, Dict, Optional, Any
import logging

logger = logging.getLogger(__name__)

def analyze_medicines(
    medicines: List[Dict[str, Any]], 
    analysis_type: str = "basic"
) -> Dict[str, Any]:
    """
    Analyze traditional medicines for various properties.
    
    Args:
        medicines: List of medicine dictionaries
        analysis_type: Type of analysis to perform
        
    Returns:
        Dictionary containing analysis results
        
    Raises:
        ValueError: If analysis_type is not supported
    """
    if analysis_type not in ["basic", "chemical", "statistical"]:
        raise ValueError(f"Unsupported analysis type: {analysis_type}")
    
    # Implementation here
    results = {}
    
    logger.info(f"Completed {analysis_type} analysis for {len(medicines)} medicines")
    return results
```

### **Adding New Features**

#### **1. Create a Feature Branch**
```bash
git checkout -b feature/new-analysis-method
```

#### **2. Implement the Feature**
- Add new methods to appropriate classes
- Include comprehensive docstrings
- Add type hints
- Follow existing code patterns

#### **3. Add Tests**
```python
# test_tradchem.py
import pytest
from tradchem import TradChem

def test_new_analysis_method():
    """Test the new analysis method."""
    tc = TradChem()
    
    # Test with sample data
    test_medicines = [
        {"product_name": "Test Medicine", "benefits": ["Test Benefit"]}
    ]
    
    results = tc.new_analysis_method(test_medicines)
    
    assert isinstance(results, dict)
    assert "analysis_type" in results
    # Add more specific assertions
```

#### **4. Update Documentation**
- Add docstring examples
- Update README if needed
- Add to API documentation

### **Bug Fixes**

#### **1. Reproduce the Bug**
- Create a minimal test case
- Document the expected vs actual behavior

#### **2. Fix the Issue**
- Implement the fix
- Add regression tests
- Update documentation if needed

#### **3. Test the Fix**
```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_tradchem.py::test_specific_function

# Run with coverage
pytest --cov=tradchem
```

## 📊 **Data Contributions**

### **Adding Traditional Medicine Data**

#### **1. Using CSV Template**
```bash
# Generate template
python -m tradchem.cli template --file new_medicines.csv

# Fill in the data and submit
```

#### **2. Using JSON Format**
```json
{
  "product_name": "New Medicine",
  "scientific_name": "Scientific Name",
  "description": "Description of the medicine",
  "traditional_system": "Ayurvedic Medicine",
  "geographic_origin": "India",
  "benefits": ["Benefit 1", "Benefit 2"],
  "diseases": ["Disease 1", "Disease 2"],
  "chemical_composition": {
    "ingredients": {
      "Active Compound": {
        "smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
        "molecular_weight": 368.38,
        "cas_number": "458-37-7",
        "pubchem_id": "969516"
      }
    }
  },
  "source": "Reference source",
  "source_url": "https://example.com/reference"
}
```

#### **3. Data Quality Standards**
- **Accuracy**: Verify all information is correct
- **Completeness**: Include all required fields
- **Consistency**: Follow established naming conventions
- **Citations**: Provide reliable sources
- **SMILES Validation**: Ensure chemical structures are valid

### **Adding Chemical Data**

#### **SMILES Notation Guidelines**
- Use canonical SMILES format
- Validate with RDKit or similar tools
- Include molecular weight and other properties
- Add PubChem IDs when available

#### **Example Chemical Data**
```json
{
  "ingredient_name": "Curcumin",
  "smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
  "molecular_weight": 368.38,
  "molecular_formula": "C21H20O6",
  "cas_number": "458-37-7",
  "pubchem_id": "969516",
  "iupac_name": "(1E,6E)-1,7-bis(4-hydroxy-3-methoxyphenyl)hepta-1,6-diene-3,5-dione"
}
```

## 📚 **Documentation Contributions**

### **Code Documentation**

#### **Docstring Standards**
```python
def complex_function(
    param1: str, 
    param2: Optional[int] = None
) -> Dict[str, Any]:
    """
    Brief description of what the function does.
    
    Longer description if needed, explaining the purpose,
    algorithm, or important details.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter (optional)
        
    Returns:
        Description of return value and structure
        
    Raises:
        ValueError: When parameter validation fails
        TypeError: When parameter types are incorrect
        
    Example:
        >>> result = complex_function("example", 42)
        >>> print(result)
        {'status': 'success', 'data': [...]}
        
    Note:
        Important notes about usage or limitations
    """
    pass
```

### **Tutorial and Example Contributions**

#### **Creating New Tutorials**
1. Create a new notebook in `examples/` or `colab_examples/`
2. Follow the existing notebook structure
3. Include clear explanations and comments
4. Test the notebook in a clean environment

#### **Example Tutorial Structure**
```python
# Tutorial: Advanced Chemical Analysis
"""
# Advanced Chemical Analysis with TradChem

This tutorial demonstrates advanced chemical analysis techniques
using the TradChem package.

## Learning Objectives
- Understand molecular property calculations
- Perform drug-likeness analysis
- Create chemical visualizations

## Prerequisites
- Basic Python knowledge
- Understanding of chemical structures
"""

# Import required libraries
from tradchem import TradChem
from rdkit import Chem
import matplotlib.pyplot as plt

# Tutorial content with explanations
```

## 🧪 **Testing Contributions**

### **Writing Tests**

#### **Test Structure**
```python
# test_new_feature.py
import pytest
from tradchem import TradChem

class TestNewFeature:
    """Test suite for new feature."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.tc = TradChem()
        self.sample_data = [
            {"product_name": "Test Medicine", "benefits": ["Test"]}
        ]
    
    def test_basic_functionality(self):
        """Test basic functionality of new feature."""
        result = self.tc.new_feature(self.sample_data)
        assert result is not None
        assert isinstance(result, dict)
    
    def test_edge_cases(self):
        """Test edge cases and error conditions."""
        with pytest.raises(ValueError):
            self.tc.new_feature([])
    
    def test_integration(self):
        """Test integration with existing features."""
        # Test how new feature works with existing functionality
        pass
```

#### **Running Tests**
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_tradchem.py

# Run with coverage
pytest --cov=tradchem --cov-report=html

# Run with verbose output
pytest -v

# Run tests in parallel
pytest -n auto
```

### **Test Coverage**
- Aim for >80% code coverage
- Test both success and failure cases
- Test edge cases and boundary conditions
- Test integration with other features

## 🔄 **Pull Request Process**

### **1. Prepare Your Changes**
```bash
# Ensure you're on the main branch and up to date
git checkout main
git pull origin main

# Create a feature branch
git checkout -b feature/your-feature-name

# Make your changes
# ... edit files ...

# Add and commit your changes
git add .
git commit -m "Add new feature: brief description"

# Push to your fork
git push origin feature/your-feature-name
```

### **2. Create Pull Request**
1. Go to your fork on GitHub
2. Click "New Pull Request"
3. Select your feature branch
4. Fill out the PR template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Data addition
- [ ] Test addition

## Testing
- [ ] All tests pass
- [ ] New tests added
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No breaking changes
```

### **3. Code Review Process**
- Maintainers will review your PR
- Address any feedback or requested changes
- Ensure all CI checks pass
- Update PR as needed

### **4. Merge and Release**
- Once approved, your PR will be merged
- Changes will be included in the next release
- You'll be credited in the release notes

## 📋 **Contribution Checklist**

### **Before Submitting**
- [ ] Code follows style guidelines (Black, flake8)
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] No breaking changes (or documented)
- [ ] Commit messages are clear and descriptive

### **For Data Contributions**
- [ ] Data is accurate and verified
- [ ] Sources are properly cited
- [ ] SMILES notations are valid
- [ ] Follows data format standards

### **For Code Contributions**
- [ ] Type hints are included
- [ ] Docstrings are comprehensive
- [ ] Tests cover new functionality
- [ ] No hardcoded values or secrets

## 🏆 **Recognition and Credits**

### **Contributor Recognition**
- All contributors are listed in `CONTRIBUTORS.md`
- Significant contributions are highlighted in release notes
- Contributors receive recognition in documentation

### **Types of Recognition**
- **Code Contributors**: Listed in contributors file
- **Data Contributors**: Acknowledged in data sources
- **Documentation Contributors**: Credited in docs
- **Reviewers**: Listed in PR acknowledgments

## 📞 **Getting Help**

### **Communication Channels**
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and discussions
- **Pull Requests**: Code review and feedback
- **Email**: For sensitive or private matters

### **Resources**
- **Documentation**: Check README.md and docstrings
- **Examples**: Explore example notebooks
- **Tests**: Look at test files for usage examples
- **Issues**: Search existing issues for similar problems

## 📜 **Code of Conduct**

### **Our Standards**
- Be respectful and inclusive
- Use welcoming and inclusive language
- Be collaborative and constructive
- Focus on what is best for the community

### **Unacceptable Behavior**
- Harassment or discrimination
- Trolling or insulting comments
- Publishing others' private information
- Any conduct inappropriate in a professional setting

## 🎉 **Thank You!**

Thank you for contributing to TradChem! Your contributions help make traditional medicine research more accessible and scientific. Whether you're adding code, data, documentation, or just helping with discussions, every contribution is valuable.

**Happy contributing! 🌿🧪**

---

**Built with ❤️ by the TradChem Community** 