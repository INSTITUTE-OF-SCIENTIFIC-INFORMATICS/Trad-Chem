# Contributing to TradChem Database

Thank you for your interest in contributing to the TradChem traditional medicine database! This project is designed to integrate with our [Trad-Chem LLM chatbot](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem-LLM).

## 🎯 Main Areas for Contribution

### 1. **Database Contributions** (Most Needed!)
- **Add new traditional medicines** to the database
- **Update existing medicine information** with more details
- **Add chemical compositions** and SMILES notations
- **Improve data quality** and fix errors

### 2. **LLM Integration Improvements**
- Enhance search algorithms for better LLM responses
- Improve data formatting for AI chatbots
- Add new query types and response formats

### 3. **Code Improvements**
- Bug fixes and performance improvements
- Documentation updates
- Testing improvements

## 📊 Adding New Medicines to Database

### Quick Method
1. Edit `tradchem/data/tradchem_database.json`
2. Add your medicine following this format:

```json
{
    "product_name": "Medicine Name",
    "scientific_name": "Scientific Name (if available)",
    "traditional_system": "Ayurveda/TCM/Unani/etc",
    "geographic_origin": "Country/Region",
    "benefits": [
        "Benefit 1",
        "Benefit 2",
        "Benefit 3"
    ],
    "diseases": [
        "Disease 1",
        "Disease 2"
    ],
    "chemical_composition": {
        "ingredients": {
            "Ingredient Name": {
                "compound_name": "SMILES_notation_here",
                "molecular_weight": 123.45
            }
        }
    },
    "source": "Your source/reference",
    "date_added": "2024-01-01",
    "entry_id": "TC_XXXXXX"
}
```

### Using CSV Template
1. Download `contributions/templates/medicine_template.csv`
2. Fill in your data
3. Submit via pull request

## 🔬 Chemical Data Guidelines

### SMILES Notations
- Use standard SMILES format
- Verify using online tools like ChemSketch or RDKit
- Include molecular weight when possible

### Data Quality Standards
- **Accurate information only** - cite your sources
- **Complete entries preferred** - fill as many fields as possible  
- **Consistent naming** - use standard plant/medicine names
- **Verify traditional uses** - cross-reference with reliable sources

## 🤝 How to Contribute

### For Database Updates
1. **Fork** this repository
2. **Clone** your fork locally
3. **Create a branch**: `git checkout -b add-new-medicines`
4. **Add your data** to `tradchem/data/tradchem_database.json`
5. **Test your changes**: `python examples/llm_integration_example.py`
6. **Commit**: `git commit -m "Add: [Medicine Name] and [Number] other medicines"`
7. **Push**: `git push origin add-new-medicines`
8. **Create Pull Request** with description of what you added

### For Code Improvements
1. Follow the same fork/branch/PR process
2. Focus on the `tradchem/__init__.py` main functions:
   - `llm_query()`
   - `get_database_stats()`
   - `search_by_*()` functions
3. Test with the LLM integration example
4. Keep changes focused on LLM integration

## 🧪 Testing Your Contributions

### Quick Test
```python
from tradchem import llm_query, get_database_stats

# Test database loads correctly
stats = get_database_stats()
print(f"Database contains {stats['total_medicines']} medicines")

# Test your new medicine appears in search
results = llm_query("your_medicine_name", context_limit=5)
print(f"Found {results['total_found']} results")
```

### Run Integration Example
```bash
python examples/llm_integration_example.py
```

## 📋 Data Sources We Accept

✅ **Accepted Sources:**
- Peer-reviewed research papers
- Traditional medicine textbooks
- Government health databases
- Verified ethnobotanical studies
- Clinical trial data

❌ **Not Accepted:**
- Wikipedia or unreliable web sources
- Personal anecdotes without verification
- Commercial product claims
- Unverified social media posts

## 🎯 Priority Contributions

### High Priority
1. **Ayurvedic medicines** with SMILES data
2. **Traditional Chinese Medicine (TCM)** entries
3. **Chemical composition data** for existing entries
4. **Verified therapeutic uses** with references

### Medium Priority  
1. Geographic distribution improvements
2. Scientific name standardization
3. Additional traditional medicine systems
4. Data quality improvements

## 🔄 Database Update Process

### Monthly Updates
- We review and merge contributions monthly
- Database version numbers are updated
- Changes are reflected in the LLM chatbot

### Quality Assurance
- All contributions are reviewed for accuracy
- Chemical data is verified using computational tools
- Traditional uses are cross-referenced with literature

## 💬 Questions and Support

- **Issues**: Open an issue on GitHub for questions
- **Discussions**: Use GitHub Discussions for general questions
- **LLM Integration**: Check the [Trad-Chem LLM repo](https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem-LLM)

## 📜 License and Attribution

- All contributions are released under MIT License
- Contributors are credited in release notes
- Large contributions may be highlighted in documentation

---

**Ready to contribute?** Start by adding one traditional medicine you know well to the database! 🌿
