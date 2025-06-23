# 🤝 Contributing to TradChem LLM

Thank you for your interest in the TradChem LLM project! We welcome all forms of contributions, including code, data, documentation, and community support.

## 🌟 **Ways to Contribute**

### **📊 Data Contribution (Most Important)**
Adding traditional medicine data is our top priority:

#### **Quick Start**
1. **Web Interface**: Visit the app and click "Add Medicine"
2. **CSV Template**: Download the template and fill in your data
3. **GitHub Issues**: Use our Issue template
4. **JSON Format**: Developer-friendly structured data

#### **Detailed Guides**
- [📊 Complete Data Contribution Guide](CONTRIBUTING_DATA.md)
- [📁 Contribution Directory Overview](contributions/README.md)
- [📋 Data Quality Standards](contributions/guidelines/data_quality.md)
- [🧪 SMILES Guidelines](contributions/guidelines/smiles_guidelines.md)
- [📚 Citation Standards](contributions/guidelines/citation_standards.md)

### **💻 Code Contribution**
Improve features, fix bugs, add new features:

#### **Development Environment Setup**
```bash
# Clone the project
git clone https://github.com/your-username/tradchem-llm.git
cd tradchem-llm

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Dev dependencies
```

#### **Code Standards**
- Follow PEP 8 Python code style
- Use type annotations
- Write unit tests
- Add English comments

### **📚 Documentation Contribution**
Improve docs, translations, tutorials:

#### **Documentation Types**
- API documentation
- User guides
- Developer docs
- Translations

### **🌍 Community Contribution**
Answer questions, support users, promote the project:

#### **Community Activities**
- Participate in GitHub Discussions
- Support on Discord
- Technical sharing and tutorials
- Project promotion

## 🚀 **Contribution Workflow**

### **1. Preparation**
- Fork the project to your GitHub account
- Clone your fork locally
- Set up the development environment

### **2. Create a Branch**
```bash
# Create a feature branch
git checkout -b feature/your-feature-name
# or
git checkout -b data/add-medicine-name
```

### **3. Make Changes**
- Write code or add data
- Follow project standards
- Test your changes

### **4. Commit Changes**
```bash
# Add changes
git add .

# Commit changes
git commit -m "feat: add new traditional medicine data"
# or
git commit -m "fix: resolve SMILES validation issue"
```

### **5. Push Changes**
```bash
# Push to your fork
git push origin feature/your-feature-name
```

### **6. Create a Pull Request**
- Create a Pull Request on GitHub
- Fill in a detailed description
- Wait for code review

## 📋 **Contribution Guidelines**

### **Code Contribution**
- **Feature Development**: Add new features or improve existing ones
- **Bug Fixes**: Fix known issues
- **Performance Optimization**: Improve system performance
- **Test Coverage**: Increase test coverage

### **Data Contribution**
- **Traditional Medicines**: Add traditional medicine information
- **Chemical Components**: Provide SMILES structures
- **Benefit Data**: Record therapeutic benefits and indications
- **Source Citation**: Provide reliable references

### **Documentation Contribution**
- **User Guides**: Write user guides
- **API Docs**: Improve API documentation
- **Developer Docs**: Write developer documentation
- **Translation**: Translate docs to other languages

## 🎯 **Contribution Priorities**

### **High Priority** 🔴
1. **Data Quality Improvement**: Validate and optimize existing data
2. **SMILES Validation**: Ensure chemical structure accuracy
3. **Source Citation**: Improve data source information
4. **Bug Fixes**: Fix critical issues

### **Medium Priority** 🟡
1. **New Feature Development**: Add user-requested features
2. **Performance Optimization**: Improve system speed
3. **UI Improvement**: Enhance user interface experience
4. **Documentation Improvement**: Add missing docs

### **Low Priority** 🟢
1. **Code Refactoring**: Improve code structure
2. **Test Coverage**: Add more test cases
3. **Translation**: Multi-language support
4. **Community Building**: Community activities and organization

## 📊 **Detailed Data Contribution Guide**

### **Data Format Requirements**
- **CSV Format**: Use the provided template
- **JSON Format**: Structured data format
- **SMILES Validation**: Must pass chemical structure validation
- **Source Citation**: Provide reliable references

### **Data Quality Standards**
- **Accuracy**: Information must be accurate
- **Completeness**: Required fields must be filled
- **Consistency**: Follow data format standards
- **Reliability**: Sources must be trustworthy and verifiable

### **Supported Traditional Medicine Systems**
- **Ayurvedic Medicine**: Indian traditional medicine
- **Traditional Chinese Medicine**: Chinese traditional medicine
- **Unani Medicine**: Islamic traditional medicine
- **African Traditional Medicine**: African continent traditional medicine
- **Indigenous Medicine**: Indigenous traditional medicine

## 🔧 **Development Tools**

### **Code Quality Tools**
```bash
# Code formatting
black tradchem_llm/
isort tradchem_llm/

# Code checking
flake8 tradchem_llm/
mypy tradchem_llm/

# Run tests
pytest tests/
```

### **Data Validation Tools**
```bash
# SMILES validation
python -m tradchem.cli validate-smiles "YOUR_SMILES"

# Data import test
python -m tradchem.cli import --file data.csv --format csv

# Data export
python -m tradchem.cli export --file output.json --format json
```

## 📞 **Get Help**

### **Technical Support**
- **GitHub Issues**: Report bugs and feature requests
- **GitHub Discussions**: Technical Q&A
- **Discord Server**: Real-time technical support
- **Email Support**: For complex issues

### **Learning Resources**
- **Getting Started Guide**: Quick start
- **API Documentation**: Developer reference
- **Example Projects**: Real-world use cases
- **Video Tutorials**: Visual learning

## 🏆 **Contributor Benefits**

### **Recognition and Rewards**
- **Contributor List**: Displayed in README
- **Data Ownership**: Protect contributor rights
- **Community Badge**: Special badge for active contributors
- **Research Citation**: Support for academic citation

### **Community Participation**
- **Decision Making**: Participate in key project decisions
- **Feature Suggestions**: Propose new features
- **Community Activities**: Join community events
- **Expert Consultation**: Get expert guidance

## 📋 **Code of Conduct**

### **Community Guidelines**
- **Respect Others**: Respect all contributors
- **Constructive Feedback**: Provide helpful feedback
- **Inclusivity**: Welcome contributors from all backgrounds
- **Professionalism**: Stay professional and polite

### **Technical Guidelines**
- **Code Quality**: Maintain high code quality
- **Complete Documentation**: Provide relevant docs
- **Test Coverage**: Write necessary tests
- **Backward Compatibility**: Consider backward compatibility

## 🚀 **Quick Contribution Templates**

### **Data Contribution Template**
```csv
product_name,benefits,diseases,ingredients,smiles,source,traditional_system
"Medicine Name","Benefit1; Benefit2; Benefit3","Disease1; Disease2; Disease3","Ingredient1; Ingredient2; Ingredient3","SMILES1; SMILES2; SMILES3","Source Reference","Traditional Medicine System"
```

### **Issue Template**
- Use our provided Issue template
- Describe the issue or suggestion in detail
- Provide reproduction steps
- Include environment information

### **Pull Request Template**
- Describe the changes
- Explain the reason for the changes
- Provide test results
- Update relevant documentation

---

**Thank you for contributing to the protection and advancement of traditional medicine knowledge!** 🌿🤝

*Let's build a better traditional medicine AI platform together!*

## Contributors

We would like to thank the following people for their contributions:

| Contributor Name | Assigned Medicinal Component | References |
|------------------|------------------------------|------------|
| [Contributor Name](https://github.com/contributor) | Component A | 1. Reference 1 <br> 2. Reference 2 |
| [Another Contributor](https://github.com/another-contributor) | Component B | 1. Reference 3 <br> 2. Reference 4 |
