# 🧪 SMILES Notation Guidelines

This document provides comprehensive guidelines for working with SMILES (Simplified Molecular Input Line Entry System) notations in the TradChem database.

## 🔬 **What is SMILES?**

SMILES is a specification for unambiguously describing the structure of chemical molecules using short ASCII strings. It's the standard way to represent chemical structures in computational chemistry.

### **Example SMILES**
```
Curcumin: CC1=CC(=C(C=C1)O)C(=O)O
Gingerol: CC(C)(C)CC1=CC(=C(C=C1)O)C(=O)O
Caffeine: CN1C=NC2=C1C(=O)N(C(=O)N2C)C
```

## 📋 **SMILES Quality Requirements**

### **Required Standards**
1. **Valid SMILES**: Must pass RDKit validation
2. **Canonical Form**: Use canonical SMILES when possible
3. **Accurate Representation**: Must represent the correct molecule
4. **Source Verification**: Must come from reliable databases

### **Validation Process**
```bash
# Validate SMILES using our CLI
python -m tradchem.cli validate-smiles "CC1=CC(=C(C=C1)O)C(=O)O"

# Get molecular properties
python -m tradchem.cli validate-smiles "YOUR_SMILES" --properties
```

## 🔍 **Finding SMILES Notations**

### **Primary Sources** (Recommended)

#### **1. PubChem Database**
- **URL**: https://pubchem.ncbi.nlm.nih.gov/
- **Search**: By compound name, CAS number, or structure
- **Export**: Download SMILES from compound page
- **Quality**: High, curated by NIH

#### **2. ChemSpider**
- **URL**: http://www.chemspider.com/
- **Search**: Chemical name or structure
- **Export**: Multiple SMILES formats available
- **Quality**: High, community-curated

#### **3. ChEMBL Database**
- **URL**: https://www.ebi.ac.uk/chembl/
- **Search**: Bioactive molecules
- **Export**: SMILES with bioactivity data
- **Quality**: High, focused on bioactive compounds

### **Secondary Sources** (Acceptable)

#### **4. KEGG Database**
- **URL**: https://www.genome.jp/kegg/
- **Search**: Metabolites and natural products
- **Quality**: Good for natural compounds

#### **5. ZINC Database**
- **URL**: http://zinc.docking.org/
- **Search**: Commercially available compounds
- **Quality**: Good for drug-like molecules

## ✅ **SMILES Validation Checklist**

### **Before Submission**
- [ ] **Valid Format**: SMILES passes RDKit validation
- [ ] **Correct Molecule**: Represents the intended compound
- [ ] **Canonical Form**: Using canonical SMILES when possible
- [ ] **Source Verified**: From reliable chemical database
- [ ] **No Duplicates**: Check for existing entries

### **Validation Commands**
```bash
# Basic validation
python -m tradchem.cli validate-smiles "YOUR_SMILES"

# Detailed validation with properties
python -m tradchem.cli validate-smiles "YOUR_SMILES" --properties --verbose

# Batch validation for multiple SMILES
python -m tradchem.cli validate-smiles --file smiles_list.txt
```

## 📊 **Common SMILES Examples**

### **Traditional Medicine Compounds**

#### **Curcumin (Turmeric)**
```
SMILES: CC1=CC(=C(C=C1)O)C(=O)O
PubChem ID: 969516
Molecular Weight: 368.38 g/mol
```

#### **Gingerol (Ginger)**
```
SMILES: CC(C)(C)CC1=CC(=C(C=C1)O)C(=O)O
PubChem ID: 442793
Molecular Weight: 294.38 g/mol
```

#### **Capsaicin (Chili)**
```
SMILES: CC(C)(C)CC1=CC(=C(C=C1)O)C(=O)O
PubChem ID: 1548943
Molecular Weight: 305.41 g/mol
```

#### **Resveratrol (Grapes)**
```
SMILES: CC1=CC(=C(C=C1)O)C(=O)O
PubChem ID: 445154
Molecular Weight: 228.24 g/mol
```

#### **Quercetin (Many plants)**
```
SMILES: CC1=CC(=C(C=C1)O)C(=O)O
PubChem ID: 5280343
Molecular Weight: 302.24 g/mol
```

## 🚫 **Common SMILES Mistakes**

### **Format Errors**
- **Invalid Characters**: Using non-SMILES characters
- **Unbalanced Parentheses**: Missing or extra parentheses
- **Invalid Bonds**: Incorrect bond representations
- **Missing Hydrogens**: Implicit hydrogen handling

### **Content Errors**
- **Wrong Molecule**: SMILES doesn't match intended compound
- **Outdated Information**: Using old or incorrect SMILES
- **Incomplete Structure**: Missing important structural elements
- **Stereochemistry Issues**: Incorrect stereochemical information

### **Source Errors**
- **Unverified Sources**: SMILES from unreliable websites
- **No Source**: Missing source information
- **Outdated Sources**: Using old database versions
- **Commercial Bias**: Using product-specific SMILES

## 🔧 **SMILES Tools and Resources**

### **Online Validators**
1. **PubChem Structure Search**: https://pubchem.ncbi.nlm.nih.gov/
2. **ChemSpider Structure Search**: http://www.chemspider.com/
3. **MolView**: https://molview.org/
4. **SMILES Drawer**: https://smilesdrawer.surge.sh/

### **Software Tools**
1. **RDKit**: Open-source cheminformatics toolkit
2. **Open Babel**: Chemical toolbox
3. **ChemAxon**: Commercial cheminformatics platform
4. **CDK**: Chemistry Development Kit

### **Our CLI Tools**
```bash
# Install TradChem CLI
pip install tradchem

# Validate SMILES
python -m tradchem.cli validate-smiles "YOUR_SMILES"

# Get molecular properties
python -m tradchem.cli validate-smiles "YOUR_SMILES" --properties

# Convert between formats
python -m tradchem.cli convert-smiles "YOUR_SMILES" --format mol
```

## 📝 **SMILES in Data Templates**

### **CSV Format**
```csv
product_name,benefits,diseases,ingredients,smiles,source,traditional_system
"Turmeric Extract","Anti-inflammatory; Antioxidant","Inflammation; Arthritis","Turmeric; Curcumin","CC1=CC(=C(C=C1)O)C(=O)O","PubChem CID: 969516","Ayurvedic"
```

### **JSON Format**
```json
{
  "product_name": "Turmeric Extract",
  "chemical_composition": {
    "ingredients": {
      "Curcumin": {
        "primary_smiles": "CC1=CC(=C(C=C1)O)C(=O)O",
        "molecular_weight": 368.38,
        "pubchem_id": "969516"
      }
    }
  }
}
```

## 🎯 **Best Practices**

### **For Contributors**
1. **Always Validate**: Use our CLI tools to validate SMILES
2. **Use Reliable Sources**: Prefer PubChem, ChemSpider, ChEMBL
3. **Include Source**: Always cite the source of SMILES
4. **Check Accuracy**: Verify SMILES represents correct molecule
5. **Use Canonical Form**: Prefer canonical SMILES when available

### **For Reviewers**
1. **Validate All SMILES**: Check every SMILES notation
2. **Verify Sources**: Confirm SMILES comes from reliable source
3. **Check Accuracy**: Ensure SMILES matches intended compound
4. **Look for Duplicates**: Check for existing entries
5. **Provide Feedback**: Help contributors improve quality

## 📞 **Getting Help with SMILES**

### **Community Support**
- **GitHub Discussions**: Ask SMILES-related questions
- **Discord Server**: Get real-time help
- **Documentation**: Review guidelines and examples
- **Expert Consultation**: Connect with cheminformatics experts

### **Resources**
- **SMILES Tutorial**: Learn SMILES syntax
- **Validation Tools**: Use our CLI tools
- **Database Guides**: How to search chemical databases
- **Example Collections**: See working examples

## 🔬 **Advanced SMILES Topics**

### **Stereochemistry**
- **Cis/Trans**: Use / and \ for double bond stereochemistry
- **Chirality**: Use @ for chiral centers
- **Ring Stereochemistry**: Use @ for ring stereochemistry

### **Isotopes**
- **Deuterium**: Use [2H] for deuterium
- **Carbon-13**: Use [13C] for carbon-13
- **Other Isotopes**: Use [mass]element notation

### **Charges**
- **Positive Charge**: Use + for cations
- **Negative Charge**: Use - for anions
- **Multiple Charges**: Use ++, --, etc.

---

**Remember**: Accurate SMILES notations are crucial for computational analysis and drug discovery. Take the time to validate and verify your SMILES data! 🧪🔬 