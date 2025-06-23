# 🌿 TradChem LLM - Traditional Medicine AI Platform

**TradChem LLM** is an AI-powered traditional medicine database and chat platform, integrating traditional medicine knowledge with modern AI technology. It provides comprehensive information and intelligent Q&A services for researchers, medical professionals, and enthusiasts.

## 🚀 **Quick Start**

### **Web Application**
Visit our online platform: `https://your-tradchem-site.netlify.app`

### **Run Locally**
```bash
# Clone the project
git clone https://github.com/your-username/tradchem-llm.git
cd tradchem-llm

# Install dependencies
pip install -r requirements.txt

# Start the server
python tradchem_llm/main.py
```

## 📊 **How to Contribute Data**

We offer several ways for open-source contributors to add traditional medicine data to the project:

### **1. 🌐 Web Interface (Easiest)**
- Visit the web app
- Click the "Add Medicine" button
- Fill out the form and submit

### **2. 📄 CSV Template (Recommended for Bulk Data)**
```bash
# Download the template
python -m tradchem.cli template --file my_medicines.csv

# Fill in your data and submit a Pull Request
```

### **3. 📋 JSON Format (Developer Friendly)**
- Use structured JSON format
- Supports complex chemical composition data
- Suitable for programmatic data addition

### **4. 🐛 GitHub Issues (Quick Contribution)**
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

### **🤖 AI Chat**
- Intelligent Q&A based on traditional medicine knowledge
- Supports multiple traditional medicine systems
- Natural language interface

### **🔍 Advanced Search**
- Search by medicine name, benefits, diseases
- Query by chemical composition and SMILES
- Search by traditional medicine system

### **📊 Data Management**
- Traditional medicine database management
- Chemical structure validation
- Data import/export functions

### **🌐 Web Interface**
- Modern responsive design
- Real-time chat
- Data visualization

## 🏗️ **System Architecture**

```
TradChem LLM/
├── tradchem_llm/           # Main application directory
│   ├── main.py            # FastAPI server
│   ├── models.py          # Pydantic data models
│   ├── database.py        # Database connection
│   ├── config.py          # Configuration management
│   └── services/          # Service layer
│       ├── chat_service.py    # Chat service
│       ├── llm_service.py     # LLM integration
│       └── tradchem_service.py # TradChem data service
├── tradchem/              # Core TradChem package
│   ├── tradchem.py        # Main database class
│   ├── cli.py             # Command line tool
│   └── utils/             # Utility functions
├── contributions/         # Data contribution directory
│   ├── templates/         # Data templates
│   ├── examples/          # Example data
│   └── guidelines/        # Contribution guidelines
└── netlify/              # Netlify deployment config
```

## 🔧 **Tech Stack**

### **Backend**
- **FastAPI**: Modern Python web framework
- **Pydantic**: Data validation and serialization
- **RDKit**: Cheminformatics toolkit
- **OpenAI API**: Large language model integration

### **Frontend**
- **Bootstrap 5**: Responsive UI framework
- **JavaScript**: Interactive features
- **Chart.js**: Data visualization

### **Deployment**
- **Netlify**: Frontend and serverless functions
- **Docker**: Containerized deployment
- **GitHub Actions**: CI/CD automation

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

## 📞 **Community Support**

### **Get Help**
- **GitHub Discussions**: Technical Q&A
- **Discord Server**: Real-time community chat
- **Documentation Center**: Detailed user guides
- **Example Projects**: Real-world use cases

### **Learning Resources**
- **Getting Started Guide**: Quick start
- **API Documentation**: Developer reference
- **Video Tutorials**: Visual learning
- **Best Practices**: Experience sharing

## 📄 **License**

This project uses the **MIT License** - see [LICENSE](LICENSE) for details

## 🙏 **Acknowledgments**

Thanks to all researchers, practitioners, and enthusiasts who contribute to the preservation and dissemination of traditional medicine knowledge.

---

**🌿 Let's work together to protect and pass on the wisdom of traditional medicine!**

*Author: SaltyHeart*

# Go to supabase.com and create a new project
# Get your project URL and anon key


