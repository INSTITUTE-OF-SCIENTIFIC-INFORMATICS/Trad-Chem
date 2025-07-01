# TradChem Database 🌿

**Traditional Medicine Database for LLM Integration**

A comprehensive database of traditional medicines with chemical compositions, optimized for integration with AI chatbots and LLM applications.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 🎯 Purpose

This repository contains a curated database of traditional medicines and provides easy-to-use functions for integrating this data with Large Language Models (LLMs), specifically designed for the **[Trad-Chem LLM Chatbot](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem-LLM)**.

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem.git
cd Trad-Chem
pip install -r requirements.txt
```

### Basic Usage
```python
from tradchem import llm_query, get_database_stats

# Get database information
stats = get_database_stats()
print(f"Database contains {stats['total_medicines']} traditional medicines")

# Query for LLM integration
response = llm_query("What plants help with inflammation?", context_limit=5)
print(f"Found {response['total_found']} relevant medicines")

for medicine in response['context_data']:
    print(f"- {medicine['product_name']}: {', '.join(medicine['benefits'][:3])}")
```

## 🤖 LLM Integration

### Main Integration Functions

| Function | Purpose | Usage |
|----------|---------|-------|
| `llm_query()` | Main LLM integration function | Get structured data for any query |
| `get_database_stats()` | Database information | Get overview of database contents |
| `search_by_benefits()` | Search by therapeutic benefits | Find medicines for specific benefits |
| `search_by_disease()` | Search by disease treatment | Find medicines for specific conditions |
| `search_by_system()` | Search by traditional system | Find Ayurvedic, TCM, etc. medicines |

### For Gemini Flash Integration
```python
import google.generativeai as genai
from tradchem import llm_query

def chat_with_tradchem(user_query):
    # Get traditional medicine context
    context = llm_query(user_query, context_limit=5)
    
    # Format for Gemini
    prompt = f"""
    User Question: {user_query}
    
    Traditional Medicine Database Results:
    Found {context['total_found']} relevant medicines:
    """
    
    for med in context['context_data']:
        prompt += f"\n• {med['product_name']}"
        if med['benefits']:
            prompt += f" - Benefits: {', '.join(med['benefits'][:3])}"
    
    prompt += "\n\nPlease provide a comprehensive answer based on this traditional medicine data."
    
    # Send to Gemini
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text
```

## 📊 Database Structure

### Medicine Entry Format
```json
{
    "product_name": "Turmeric Extract",
    "scientific_name": "Curcuma longa",
    "traditional_system": "Ayurveda",
    "geographic_origin": "India",
    "benefits": ["Anti-inflammatory", "Antioxidant", "Digestive aid"],
    "diseases": ["Arthritis", "Indigestion", "Skin conditions"],
    "chemical_composition": {
        "ingredients": {
            "Curcumin": {
                "primary_compound": "CC1=CC(=C(C=C1)O)C(=O)CC(=O)C2=CC(=C(C=C2)O)OC",
                "molecular_weight": 368.38
            }
        }
    }
}
```

### Current Database Stats
- **Traditional Medicines**: 1000+ entries
- **Traditional Systems**: Ayurveda, TCM, Unani, Siddha, and more
- **Chemical Compounds**: SMILES notations included
- **Geographic Coverage**: Global traditional medicine systems

## 🔄 Database Updates

### Contributing New Medicines
1. Fork this repository
2. Add entries to `tradchem/data/tradchem_database.json`
3. Follow the format in `contributions/templates/`
4. Submit a pull request

### Monthly Updates
- Database is updated monthly with new contributions
- Version numbers track database updates
- Changes automatically sync with the LLM chatbot

## 🌐 Integration with Trad-Chem LLM

This database is specifically designed to work with our [Trad-Chem LLM Chatbot](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem-LLM):

```python
# In your LLM chatbot application:
from tradchem import llm_query

def handle_user_query(user_message):
    # Get relevant traditional medicine data
    context = llm_query(user_message, context_limit=5)
    
    # Pass context to your LLM
    enhanced_prompt = f"""
    User: {user_message}
    
    Traditional Medicine Context:
    {context}
    
    Provide a detailed response using the traditional medicine data above.
    """
    
    return your_llm_model.generate(enhanced_prompt)
```

## 📝 Examples

Run the integration example:
```bash
python examples/llm_integration_example.py
```

### Example 1: Search for Anti-inflammatory Medicines
```python
from tradchem import search_by_benefits

results = search_by_benefits("inflammation", limit=5)
for medicine in results:
    print(f"{medicine['product_name']} - {medicine['traditional_system']}")
```

### Example 2: Get All Ayurvedic Medicines
```python
from tradchem import search_by_system

ayurvedic_medicines = search_by_system("Ayurveda", limit=10)
print(f"Found {len(ayurvedic_medicines)} Ayurvedic medicines")
```

### Example 3: Database Statistics
```python
from tradchem import get_database_stats

stats = get_database_stats()
print(f"Total medicines: {stats['total_medicines']}")
print(f"Traditional systems: {', '.join(stats['traditional_systems'])}")
print(f"Geographic regions: {', '.join(stats['geographic_regions'])}")
```

## 🧪 Testing

Test the database functionality:
```bash
python test_database.py
```

Test LLM integration:
```bash
python INTEGRATION_EXAMPLE.py
```

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Priority areas:**
- Adding new traditional medicines with chemical data
- Improving LLM integration functions
- Enhancing data quality and accuracy
- Adding SMILES notations for chemical compounds

## 📋 Requirements

- Python 3.8+
- numpy >= 1.21.0
- pandas >= 1.3.0
- matplotlib >= 3.4.0
- jsonschema >= 3.2.0

Optional for chemical analysis:
- rdkit-pypi >= 2022.9.1

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- **[Trad-Chem LLM Chatbot](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem-LLM)** - The main chatbot application
- **[Data Contributions](contributions/)** - Templates and examples for contributing data

## 📞 Support

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/issues)
- **Discussions**: General questions via [GitHub Discussions](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/discussions)
- **LLM Integration**: Check the [Trad-Chem LLM repository](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem-LLM)

---

**Made with ❤️ by [SaltyHeart](https://github.com/SaltyHeart) for the traditional medicine community** 