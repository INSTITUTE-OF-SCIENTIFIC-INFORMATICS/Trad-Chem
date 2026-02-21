# 📊 Data Quality Guidelines

This document outlines the quality standards that all contributors must follow when adding data to the TradChem database.

## 🎯 **Quality Standards Overview**

### **Core Principles**
1. **Accuracy**: All information must be factually correct
2. **Completeness**: Required fields must be filled
3. **Consistency**: Data format must follow established standards
4. **Reliability**: Sources must be credible and verifiable
5. **Transparency**: Sources must be properly cited

## 📋 **Required Data Quality Checklist**

### **Before Submission**
- [ ] **Medicine name** is accurate and standardized
- [ ] **Benefits** are evidence-based when possible
- [ ] **Diseases** are properly categorized
- [ ] **SMILES notations** are validated
- [ ] **Sources** are properly cited
- [ ] **Traditional system** is correctly identified
- [ ] **No copyrighted content** is included
- [ ] **Data format** follows template standards

### **Validation Steps**
1. **SMILES Validation**: Use our CLI tool to validate
2. **Source Verification**: Check that sources are accessible
3. **Cross-Reference**: Verify information across multiple sources
4. **Format Check**: Ensure data follows template format

## 🔍 **Data Quality Categories**

### **Excellent Quality** ⭐⭐⭐⭐⭐
- **Sources**: Multiple academic papers with DOIs
- **SMILES**: Validated and accurate
- **Benefits**: Evidence-based with clinical studies
- **Completeness**: All fields filled with detailed information
- **Citations**: Proper academic citations

### **Good Quality** ⭐⭐⭐⭐
- **Sources**: Traditional texts + some academic references
- **SMILES**: Validated
- **Benefits**: Traditional knowledge + some evidence
- **Completeness**: Most fields filled
- **Citations**: Traditional text citations

### **Acceptable Quality** ⭐⭐⭐
- **Sources**: Traditional texts or reputable references
- **SMILES**: Validated
- **Benefits**: Traditional knowledge
- **Completeness**: Required fields filled
- **Citations**: Basic source information

### **Needs Improvement** ⭐⭐
- **Sources**: Unclear or unreliable
- **SMILES**: Missing or invalid
- **Benefits**: Vague or unsubstantiated
- **Completeness**: Missing required fields
- **Citations**: Missing or inadequate

## 📚 **Source Quality Standards**

### **Preferred Sources** (High Priority)
1. **Academic Papers**
   - Peer-reviewed journals
   - Include DOI when available
   - Recent publications (within 10 years preferred)

2. **Traditional Texts**
   - Well-known traditional medicine texts
   - Include publication year and edition
   - Translated versions with original references

3. **Government Databases**
   - WHO Traditional Medicine Database
   - National medicine databases
   - Official pharmacopoeias

### **Acceptable Sources** (Medium Priority)
1. **Reputable Herbal Medicine References**
   - Published books by recognized experts
   - Include author and publication details

2. **Traditional Practitioner Knowledge**
   - From recognized traditional healers
   - Include practitioner credentials
   - Documented through interviews or publications

### **Unacceptable Sources** (Not Allowed)
1. **Unverified Internet Sources**
   - Random websites
   - Social media posts
   - Unverified blogs

2. **Commercial Product Claims**
   - Product marketing materials
   - Sales websites
   - Unverified supplement claims

## 🧪 **SMILES Quality Standards**

### **SMILES Validation Requirements**
1. **Chemical Accuracy**: SMILES must represent the correct molecule
2. **Format Validation**: Must pass RDKit validation
3. **Source Verification**: Must come from reliable chemical databases

### **Preferred SMILES Sources**
1. **PubChem**: https://pubchem.ncbi.nlm.nih.gov/
2. **ChemSpider**: http://www.chemspider.com/
3. **ChEMBL**: https://www.ebi.ac.uk/chembl/

### **SMILES Quality Levels**
- **Excellent**: Validated, canonical SMILES from reliable database
- **Good**: Validated SMILES with molecular properties
- **Acceptable**: Valid SMILES format
- **Poor**: Invalid or missing SMILES

## 📝 **Content Quality Standards**

### **Medicine Names**
- **Standardized**: Use official botanical names when possible
- **Consistent**: Follow established naming conventions
- **Complete**: Include common names and scientific names

### **Benefits**
- **Specific**: Avoid vague terms like "good for health"
- **Evidence-Based**: Include scientific evidence when available
- **Traditional**: Respect traditional knowledge and terminology

### **Diseases**
- **Accurate**: Use proper medical terminology
- **Specific**: Avoid overly broad categories
- **Traditional**: Include traditional disease concepts when relevant

### **Descriptions**
- **Informative**: Provide useful context
- **Accurate**: Factually correct information
- **Respectful**: Honor traditional knowledge and practices

## 🔄 **Quality Review Process**

### **Automated Validation**
1. **Format Check**: Ensures data follows template format
2. **SMILES Validation**: Validates chemical structures
3. **Required Fields**: Checks for missing required information

### **Manual Review**
1. **Source Verification**: Checks source credibility
2. **Content Accuracy**: Reviews factual accuracy
3. **Cultural Sensitivity**: Ensures respectful representation

### **Community Review**
1. **Peer Review**: Other contributors review submissions
2. **Expert Review**: Traditional medicine experts review
3. **Final Approval**: Project maintainers approve

## 🚫 **Common Quality Issues to Avoid**

### **Data Issues**
- **Missing SMILES**: All medicines should have SMILES notations
- **Vague Benefits**: Avoid generic statements like "good for health"
- **Incomplete Sources**: Always include proper citations
- **Inconsistent Format**: Follow template format exactly

### **Content Issues**
- **Cultural Appropriation**: Respect traditional knowledge
- **Medical Claims**: Avoid unsubstantiated medical claims
- **Commercial Bias**: Don't promote specific products
- **Misinformation**: Ensure all information is accurate

### **Technical Issues**
- **Invalid SMILES**: Always validate chemical structures
- **Missing Fields**: Fill all required fields
- **Format Errors**: Follow CSV/JSON format standards
- **Encoding Issues**: Use proper UTF-8 encoding

## 📊 **Quality Metrics**

### **Data Completeness**
- **Required Fields**: 100% completion required
- **Optional Fields**: 70% completion recommended
- **Source Citations**: 100% completion required

### **Data Accuracy**
- **SMILES Validation**: 100% validation required
- **Source Verification**: 90% verification recommended
- **Cross-Reference**: 80% agreement across sources

### **Data Consistency**
- **Format Compliance**: 100% compliance required
- **Naming Standards**: 95% standardization recommended
- **Classification Accuracy**: 90% accuracy recommended

## 🎯 **Quality Improvement Tips**

### **For Contributors**
1. **Research Thoroughly**: Use multiple reliable sources
2. **Validate Everything**: Check SMILES and verify sources
3. **Follow Templates**: Use provided templates exactly
4. **Ask for Help**: Reach out to community for guidance
5. **Review Before Submitting**: Double-check your data

### **For Reviewers**
1. **Be Thorough**: Check all aspects of submissions
2. **Be Constructive**: Provide helpful feedback
3. **Be Consistent**: Apply standards uniformly
4. **Be Respectful**: Honor traditional knowledge
5. **Be Collaborative**: Work with contributors to improve quality

## 📞 **Quality Support**

### **Getting Help**
- **GitHub Discussions**: Ask quality-related questions
- **Community Chat**: Get real-time feedback
- **Documentation**: Review guidelines and examples
- **Expert Consultation**: Connect with traditional medicine experts

### **Quality Resources**
- **Validation Tools**: Use our CLI tools for validation
- **Template Examples**: Follow provided examples
- **Quality Checklist**: Use the checklist before submission
- **Review Guidelines**: Understand review criteria

---

**Remember**: Quality data helps preserve traditional medicine knowledge and advances research. Every contribution matters! 🌿📊 