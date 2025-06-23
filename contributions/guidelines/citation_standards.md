# 📚 Citation and Source Attribution Guidelines

This document outlines the standards for citing sources and attributing information in the TradChem database.

## 🎯 **Why Citations Matter**

### **Importance of Proper Citations**
1. **Credibility**: Establishes trust in the data
2. **Verifiability**: Allows others to verify information
3. **Attribution**: Respects original knowledge holders
4. **Research**: Enables further investigation
5. **Legal**: Avoids copyright issues

## 📋 **Citation Format Standards**

### **Required Citation Elements**
1. **Source Type**: Academic paper, traditional text, database, etc.
2. **Title**: Full title of the source
3. **Author/Editor**: Who created the information
4. **Publication Year**: When the source was published
5. **Publisher/Journal**: Where it was published
6. **DOI/URL**: Digital identifier or web address
7. **Page Numbers**: Specific pages when relevant

### **Citation Format Examples**

#### **Academic Papers**
```
Format: Author(s). "Title." Journal Name, Year, Volume(Issue), Pages. DOI: 10.1000/example

Example: Smith, J., et al. "Curcumin: A Review of Its Anti-inflammatory Properties." 
Journal of Traditional Medicine, 2023, 15(2), 45-62. DOI: 10.1000/curcumin_study
```

#### **Traditional Texts**
```
Format: Author/Editor. "Title." Edition, Publisher, Year, Pages.

Example: Charaka. "Charaka Samhita." 1st Edition, Chaukhamba Orientalia, 2000, 
Chapter 1, Verses 15-20.
```

#### **Databases**
```
Format: Database Name. "Compound Name." Access Date. URL or DOI.

Example: PubChem. "Curcumin." Accessed 2024-01-15. 
https://pubchem.ncbi.nlm.nih.gov/compound/969516
```

#### **Books**
```
Format: Author(s). "Title." Edition, Publisher, Year, Pages.

Example: Chopra, D. "The Complete Book of Ayurvedic Home Remedies." 
1st Edition, Harmony Books, 2000, pp. 45-50.
```

## 🌿 **Traditional Medicine Source Types**

### **Primary Traditional Sources**

#### **Ayurvedic Texts**
- **Charaka Samhita**: Ancient Ayurvedic text
- **Sushruta Samhita**: Surgical and medical text
- **Ashtanga Hridaya**: Comprehensive medical text
- **Bhavaprakasha**: Materia medica text

#### **Traditional Chinese Medicine Texts**
- **Shennong Ben Cao Jing**: Divine Farmer's Materia Medica
- **Huangdi Neijing**: Yellow Emperor's Inner Canon
- **Shanghan Lun**: Treatise on Cold Damage
- **Jin Gui Yao Lue**: Essential Prescriptions from the Golden Cabinet

#### **Unani Medicine Texts**
- **Canon of Medicine**: Ibn Sina's medical encyclopedia
- **Kitab al-Hawi**: Rhazes' medical compendium
- **Zakhirah Khwarazmshahi**: Medical encyclopedia

#### **African Traditional Medicine**
- **Local Healer Knowledge**: Documented traditional knowledge
- **Community Practices**: Documented community medicine
- **Regional Texts**: Local traditional medicine texts

### **Modern Academic Sources**

#### **Peer-Reviewed Journals**
- **Journal of Ethnopharmacology**
- **Phytotherapy Research**
- **Journal of Traditional and Complementary Medicine**
- **Evidence-Based Complementary and Alternative Medicine**

#### **Research Databases**
- **PubMed**: Medical research database
- **Scopus**: Scientific literature database
- **Web of Science**: Research citation database
- **Google Scholar**: Academic search engine

## 📊 **Citation Quality Levels**

### **Excellent Citations** ⭐⭐⭐⭐⭐
- **Multiple Sources**: Information verified across multiple sources
- **Academic Papers**: Peer-reviewed research with DOIs
- **Traditional Texts**: Well-known traditional medicine texts
- **Complete Information**: All citation elements included
- **Recent Sources**: Recent publications when available

### **Good Citations** ⭐⭐⭐⭐
- **Reliable Sources**: Reputable traditional texts or academic sources
- **Complete Format**: Most citation elements included
- **Verifiable**: Sources can be found and verified
- **Appropriate**: Sources relevant to the information

### **Acceptable Citations** ⭐⭐⭐
- **Basic Sources**: Traditional knowledge or basic references
- **Partial Format**: Some citation elements missing
- **Verifiable**: Sources can be located
- **Relevant**: Sources related to the information

### **Poor Citations** ⭐⭐
- **Unclear Sources**: Vague or unclear source information
- **Incomplete**: Missing important citation elements
- **Unverifiable**: Sources cannot be found or verified
- **Irrelevant**: Sources not related to the information

## 🚫 **Unacceptable Citation Practices**

### **What to Avoid**
1. **No Citations**: Information without any source
2. **Vague Sources**: "Internet" or "traditional knowledge" without specifics
3. **Commercial Sources**: Product websites or marketing materials
4. **Unverified Claims**: Information without verifiable sources
5. **Plagiarism**: Copying content without attribution

### **Common Mistakes**
- **Missing DOIs**: Not including digital object identifiers
- **Incomplete URLs**: Broken or incomplete web addresses
- **No Access Dates**: Missing when information was accessed
- **Generic References**: "Traditional medicine" without specific text
- **Outdated Sources**: Using very old sources without modern verification

## 📝 **Citation in Data Templates**

### **CSV Format**
```csv
product_name,benefits,diseases,ingredients,smiles,source,traditional_system
"Turmeric Extract","Anti-inflammatory; Antioxidant","Inflammation; Arthritis","Turmeric; Curcumin","CC1=CC(=C(C=C1)O)C(=O)O","Charaka Samhita, Chapter 1, Verses 15-20; DOI: 10.1000/curcumin_study","Ayurvedic"
```

### **JSON Format**
```json
{
  "product_name": "Turmeric Extract",
  "source": {
    "traditional_text": "Charaka Samhita, Chapter 1, Verses 15-20",
    "academic_paper": "Smith, J., et al. 'Curcumin: A Review.' Journal of Traditional Medicine, 2023, 15(2), 45-62. DOI: 10.1000/curcumin_study",
    "database": "PubChem CID: 969516, Accessed 2024-01-15"
  },
  "traditional_system": "Ayurvedic"
}
```

## 🔍 **Citation Verification Process**

### **Verification Checklist**
- [ ] **Source Exists**: Can the source be found?
- [ ] **Information Matches**: Does the source contain the claimed information?
- [ ] **Current**: Is the source still current and relevant?
- [ ] **Accessible**: Can others access the source?
- [ ] **Complete**: Are all citation elements included?

### **Verification Tools**
1. **DOI Resolver**: https://doi.org/ to verify DOIs
2. **PubMed**: https://pubmed.ncbi.nlm.nih.gov/ for medical papers
3. **Google Scholar**: https://scholar.google.com/ for academic sources
4. **Internet Archive**: https://archive.org/ for web sources

## 📚 **Citation Resources**

### **Citation Style Guides**
1. **APA Style**: American Psychological Association
2. **Chicago Style**: University of Chicago Press
3. **MLA Style**: Modern Language Association
4. **Vancouver Style**: Biomedical journals

### **Citation Management Tools**
1. **Zotero**: Free, open-source citation manager
2. **Mendeley**: Reference manager and academic social network
3. **EndNote**: Commercial reference management software
4. **BibTeX**: LaTeX bibliography tool

## 🎯 **Best Practices for Citations**

### **For Contributors**
1. **Research Thoroughly**: Find multiple reliable sources
2. **Cite Everything**: Include citations for all information
3. **Use DOIs**: Include DOIs for academic papers
4. **Verify Sources**: Make sure sources are accessible
5. **Be Specific**: Include page numbers and specific sections

### **For Reviewers**
1. **Check Citations**: Verify all citations are accurate
2. **Verify Sources**: Confirm sources contain claimed information
3. **Check Format**: Ensure citations follow standards
4. **Look for Gaps**: Identify missing citations
5. **Provide Feedback**: Help improve citation quality

## 📞 **Getting Help with Citations**

### **Community Support**
- **GitHub Discussions**: Ask citation-related questions
- **Documentation**: Review citation guidelines
- **Examples**: See citation examples in templates
- **Expert Help**: Connect with academic librarians

### **Citation Tools**
- **DOI Lookup**: Find DOIs for papers
- **Citation Generators**: Generate properly formatted citations
- **Reference Managers**: Organize and format citations
- **Style Guides**: Learn citation format standards

## 🔬 **Special Citation Considerations**

### **Traditional Knowledge**
- **Respect**: Honor traditional knowledge holders
- **Attribution**: Give credit to traditional sources
- **Context**: Include cultural and historical context
- **Permission**: Respect traditional knowledge protocols

### **Modern Research**
- **Peer Review**: Prefer peer-reviewed sources
- **Recent**: Use recent research when available
- **Reproducible**: Ensure research can be reproduced
- **Transparent**: Include methodology and data sources

### **Database Information**
- **Access Date**: Include when information was accessed
- **Version**: Note database version if relevant
- **URL**: Include stable URLs when possible
- **Backup**: Keep local copies of important sources

---

**Remember**: Proper citations are essential for building a credible and trustworthy database. Take the time to cite your sources accurately and completely! 📚🔍 