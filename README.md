# TradChem - Traditional Medicine Database for LLM Integration

**Status: ✅ READY FOR LLM INTEGRATION**

A comprehensive database for traditional medicine data, optimized for integration with LLM chatbots and AI applications.

## 🎯 Project Overview

TradChem is an open-source traditional medicine database project designed specifically for:
- **LLM Chatbot Integration**: Seamless integration with AI chatbots
- **Research Applications**: Academic and scientific research
- **Open Contribution**: Community-driven database growth
- **Chemical Analysis**: SMILES notations and molecular data

**Author**: Anu Gamage  
**Organization**: Institute of Scientific Informatics

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem.git
cd Trad-Chem

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage
```python
import tradchem

# Get database statistics
stats = tradchem.get_database_stats()
print(f"Database contains {stats['total_medicines']} medicines")

# LLM-optimized query
result = tradchem.llm_query("immunity boost", context_limit=3)
print(f"Found {result['total_found']} relevant medicines")

# Search by specific criteria
immunity_medicines = tradchem.search_by_benefits("immunity")
fatigue_medicines = tradchem.search_by_disease("fatigue")
```

## 🤖 LLM Integration

### Integration with Trad-Chem LLM Chatbot

TradChem is designed to work seamlessly with the [Trad-Chem LLM Chatbot](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem-LLM):

```python
# Example LLM integration
import tradchem

def get_medicine_context(user_query):
    """Get relevant medicine data for LLM context"""
    result = tradchem.llm_query(
        query=user_query,
        context_limit=5,
        include_smiles=False  # Include chemical data if needed
    )
    
    return result['context_data']

# Usage in LLM prompt
context = get_medicine_context("What helps with stress and anxiety?")
# Use context in your LLM prompt...
```

### LLM-Friendly Features

- **Structured JSON Response**: Ready for LLM context injection
- **Relevance Scoring**: Intelligent ranking of search results
- **Multi-field Search**: Product names, benefits, diseases, chemical composition
- **Configurable Output**: Include/exclude SMILES chemical notations
- **Context Limiting**: Control response size for token efficiency

## 📊 Database Statistics

Current database contains:
- **4 Traditional Medicines**: Comprehensive entries with benefits and diseases
- **Multiple Traditional Systems**: Ayurveda, Traditional Chinese Medicine
- **Chemical Compositions**: SMILES notations for molecular analysis  
- **Geographic Data**: Origins and regional information
- **English Names**: Clear English translations for all traditional names

### Sample Medicines:
- **Kameshwari Rasayana** (Vitality Enhancement Tonic)
- **Ginseng Root Extract** (American Ginseng Root Extract)
- **Turmeric Curcumin Complex** (Anti-inflammatory Complex)
- **Ashwagandha Root Extract** (Winter Cherry Adaptogenic Extract)

## 🔧 API Reference

### Core Functions

#### `llm_query(query, context_limit=5, include_smiles=False)`
Main LLM query function with intelligent search and relevance scoring.

#### `get_database_stats()`
Get comprehensive database statistics for LLM context.

#### `search_by_benefits(query, limit=10)`
Search medicines by therapeutic benefits.

#### `search_by_disease(query, limit=10)`
Search medicines by treatable diseases.

#### `get_all_medicines(include_smiles=False)`
Retrieve all medicines with optional chemical data.

## 🤝 Contributing

We welcome contributions to expand the traditional medicine database!

### How to Contribute

1. **Add New Medicines**: Use the provided templates in `contributions/templates/`
2. **Improve Data Quality**: Verify and enhance existing entries
3. **Submit Pull Requests**: Follow our contribution guidelines

### Data Format

```json
{
  "product_name": "Traditional Name",
  "english_name": "English Translation",
  "description": "Detailed description",
  "benefits": ["Benefit 1", "Benefit 2"],
  "diseases": ["Disease 1", "Disease 2"],
  "chemical_composition": {
    "ingredients": {
      "Ingredient Name": {
        "compound_name": "SMILES_notation"
      }
    }
  },
  "traditional_system": "System Name",
  "geographic_origin": "Region"
}
```

## 🔗 Related Projects

- **[Trad-Chem LLM](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem-LLM)**: AI chatbot for traditional medicine queries
- **Research Applications**: Academic papers and studies using TradChem data

## 📋 Recent Updates

### v1.0.0 - Production Ready ✅
- **FIXED**: Complete resolution of null bytes corruption in Python files
- **UPDATED**: Author changed to Anu Gamage throughout codebase
- **TRANSLATED**: All Chinese comments converted to English
- **IMPROVED**: Enhanced database with real traditional medicines
- **OPTIMIZED**: Enhanced LLM query functionality with better English content
- **TESTED**: Comprehensive integration testing completed
- **READY**: Fully prepared for Trad-Chem LLM integration

### Key Improvements:
- ✅ Clean UTF-8 encoding throughout all files
- ✅ Author updated to Anu Gamage in all files
- ✅ Complete English localization (no Chinese text remaining)
- ✅ Improved database content with 4 real traditional medicines
- ✅ Enhanced LLM-friendly JSON responses
- ✅ Improved search relevance scoring
- ✅ Comprehensive error handling
- ✅ All functionality tested and verified

## 📞 Support

- **Issues**: Report bugs via GitHub Issues
- **Features**: Request features via GitHub Discussions
- **Contact**: [Institute of Scientific Informatics](mailto:contact@example.com)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Traditional medicine practitioners and researchers
- Open-source community contributors
- Chemical database providers
- Academic institutions supporting this research

---

**Author**: Anu Gamage  
**Organization**: Institute of Scientific Informatics  
**Last Updated**: 2024-01-01  
**Status**: Production Ready for LLM Integration 