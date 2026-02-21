# 📊 Data Contributions Directory

This directory is for open-source contributors to add traditional medicine data to the TradChem database.

## 📁 **Directory Structure**

```
contributions/
├── README.md                    # This file
├── templates/                   # Data templates
│   ├── medicine_template.csv    # CSV template
│   ├── medicine_template.json   # JSON template
│   └── bulk_import_template.xlsx # Excel template
├── submitted/                   # Submitted contributions
│   ├── contributor_name_1/      # Individual contributor folders
│   ├── contributor_name_2/
│   └── ...
├── validated/                   # Validated and approved data
├── examples/                    # Example contributions
│   ├── ayurvedic_examples.csv
│   ├── tcm_examples.csv
│   └── african_examples.csv
└── guidelines/                  # Contribution guidelines
    ├── data_quality.md
    ├── smiles_guidelines.md
    └── citation_standards.md
```

## 🚀 **How to Contribute**

### **Quick Start (Recommended)**

1. **Download a template**:
   - `templates/medicine_template.csv` - For bulk data
   - `templates/medicine_template.json` - For single entries

2. **Fill in your data** following the examples in `examples/`

3. **Create a pull request** with your data file

### **Step-by-Step Process**

#### **Step 1: Choose Your Template**
```bash
# Copy the CSV template
cp templates/medicine_template.csv my_medicines.csv

# Or use the CLI to generate one
python -m tradchem.cli template --file my_medicines.csv
```

#### **Step 2: Add Your Data**
```csv
product_name,benefits,diseases,ingredients,smiles,source,traditional_system
"Your Medicine Name","Benefit 1; Benefit 2","Disease 1; Disease 2","Ingredient 1; Ingredient 2","SMILES1; SMILES2","Your Source","System Name"
```

#### **Step 3: Validate Your Data**
```bash
# Validate SMILES notations
python -m tradchem.cli validate-smiles "YOUR_SMILES"

# Check your data format
python -m tradchem.cli import --file my_medicines.csv --format csv
```

#### **Step 4: Submit Your Contribution**
1. Create a new folder: `contributions/your_name/`
2. Add your data file
3. Create a pull request with description

## 📋 **Data Format Requirements**

### **CSV Format**
| Column | Required | Description | Example |
|--------|----------|-------------|---------|
| `product_name` | Yes | Medicine name | "Turmeric Extract" |
| `benefits` | Yes | Semicolon-separated benefits | "Anti-inflammatory; Antioxidant" |
| `diseases` | Yes | Semicolon-separated diseases | "Inflammation; Arthritis" |
| `ingredients` | Yes | Semicolon-separated ingredients | "Turmeric; Curcumin" |
| `smiles` | Yes | Semicolon-separated SMILES | "CC1=CC(=C(C=C1)O)C(=O)O" |
| `source` | No | Reference source | "Traditional Ayurvedic texts" |
| `traditional_system` | No | Medicine system | "Ayurvedic" |

### **JSON Format**
```json
{
  "product_name": "Medicine Name",
  "benefits": ["Benefit 1", "Benefit 2"],
  "diseases": ["Disease 1", "Disease 2"],
  "chemical_composition": {
    "ingredients": {
      "Ingredient Name": {
        "primary_smiles": "SMILES_NOTATION",
        "molecular_weight": 368.38,
        "bioavailability": "Low"
      }
    }
  },
  "source": "Reference source",
  "traditional_system": "System name"
}
```

## 🌿 **Traditional Medicine Systems**

### **Supported Systems**
- **Ayurvedic**: Indian traditional medicine
- **TCM**: Traditional Chinese Medicine
- **Unani**: Middle Eastern traditional medicine
- **African**: African traditional medicine
- **Indigenous**: Various indigenous systems
- **Other**: Specify the system name

### **System-Specific Guidelines**
- **Ayurvedic**: Focus on dosha balance, use Sanskrit names when appropriate
- **TCM**: Include qi concepts, use Chinese names when relevant
- **Unani**: Reference four humors theory
- **African**: Include local names and community context
- **Indigenous**: Respect cultural context and local knowledge

## 🔍 **Quality Standards**

### **Data Quality Checklist**
- [ ] Medicine name is accurate and standardized
- [ ] Benefits are evidence-based when possible
- [ ] SMILES notations are validated
- [ ] Sources are properly cited
- [ ] Traditional system is correctly identified
- [ ] No copyrighted content included

### **Research Requirements**
1. **Use Reliable Sources**:
   - Academic papers (preferred)
   - Traditional texts
   - Government databases
   - Reputable herbal medicine references

2. **Cite Sources Properly**:
   - Include DOI for papers
   - Reference traditional texts with year
   - Note the publication source

3. **Verify Information**:
   - Cross-reference multiple sources
   - Check for scientific validation
   - Note any conflicting information

## 📊 **SMILES Notation Guidelines**

### **Finding SMILES**
1. **PubChem**: https://pubchem.ncbi.nlm.nih.gov/
2. **ChemSpider**: http://www.chemspider.com/
3. **ChEMBL**: https://www.ebi.ac.uk/chembl/

### **Validating SMILES**
```bash
# Using our CLI tool
python -m tradchem.cli validate-smiles "CC1=CC(=C(C=C1)O)C(=O)O"

# Get molecular properties
python -m tradchem.cli validate-smiles "YOUR_SMILES" --properties
```

### **Common SMILES Examples**
```
Curcumin: CC1=CC(=C(C=C1)O)C(=O)O
Gingerol: CC(C)(C)CC1=CC(=C(C=C1)O)C(=O)O
Cannabigerol: CCCCCC1=CC(=C(C(=C1)O)C/C=C(\C)/CCC=C(C)C)O
Resveratrol: CC1=CC(=C(C=C1)O)C(=O)O
Quercetin: CC1=CC(=C(C=C1)O)C(=O)O
```

## 🏆 **Recognition and Credits**

### **Contributor Recognition**
- **Contributors List**: All contributors listed in main README
- **Data Attribution**: Sources credited in database
- **Community Badge**: Special badge for active contributors
- **Research Credits**: Academic citations when appropriate

### **Impact Tracking**
- **Data Usage**: Track how many times your data is accessed
- **Research Impact**: Monitor citations and usage
- **Community Growth**: See the project's global reach

## 📞 **Getting Help**

### **Community Support**
- **GitHub Discussions**: Ask questions and get help
- **Discord Server**: Real-time chat with contributors
- **Email Support**: For complex contributions

### **Resources**
- **API Documentation**: Technical integration help
- **Data Format Guide**: Detailed format specifications
- **FAQ**: Common questions and answers

## 🎯 **Example Contributions**

### **Example 1: Ayurvedic Medicine**
```csv
product_name,benefits,diseases,ingredients,smiles,source,traditional_system
"Brahmi (Bacopa)","Improves memory; Cognitive enhancement; Reduces anxiety","Memory loss; Cognitive decline; Anxiety","Brahmi; Bacosides","CC1=CC(=C(C=C1)O)C(=O)O","Charaka Samhita","Ayurvedic"
```

### **Example 2: TCM Medicine**
```csv
product_name,benefits,diseases,ingredients,smiles,source,traditional_system
"Ginseng Root","Boosts energy; Improves immunity; Anti-aging","Fatigue; Weak immunity; Aging","Ginseng; Ginsenosides","CC1=CC(=C(C=C1)O)C(=O)O","Shennong Ben Cao Jing","TCM"
```

### **Example 3: African Medicine**
```csv
product_name,benefits,diseases,ingredients,smiles,source,traditional_system
"Moringa Leaf","Rich in nutrients; Anti-inflammatory; Supports immunity","Malnutrition; Inflammation; Weak immunity","Moringa; Quercetin","CC1=CC(=C(C=C1)O)C(=O)O","Traditional African medicine","African"
```

## 🚀 **Start Contributing Today!**

1. **Choose your template** from the `templates/` folder
2. **Research your medicine** thoroughly
3. **Follow the guidelines** for quality data
4. **Submit your contribution** and join our community
5. **Track your impact** and see how your data helps others

**Every contribution matters!** Whether you add one medicine or hundreds, you're helping preserve and advance traditional medicine knowledge for future generations.

---

**Thank you for contributing to TradChem!** 🌿🤝 