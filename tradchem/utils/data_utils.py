"""
Data utilities for TradChem - Import/Export functionality for various formats.
"""

import json
import csv
import logging
from typing import List, Dict, Any, Optional
from pathlib import Path
import pandas as pd

logger = logging.getLogger(__name__)

class DataImporter:
    """Utility class for importing data from various formats."""
    
    @staticmethod
    def from_csv(file_path: str) -> List[Dict[str, Any]]:
        """
        Import data from CSV file.
        
        Expected CSV columns:
        - product_name: Name of the medicine
        - benefits: Semicolon-separated list of benefits
        - diseases: Semicolon-separated list of diseases
        - ingredients: Semicolon-separated list of ingredients
        - smiles: Semicolon-separated list of SMILES strings
        
        Args:
            file_path: Path to CSV file
            
        Returns:
            List of medicine dictionaries
        """
        try:
            df = pd.read_csv(file_path)
            medicines = []
            
            for _, row in df.iterrows():
                medicine = {
                    "product_name": str(row.get("product_name", "")),
                    "benefits": [b.strip() for b in str(row.get("benefits", "")).split(";") if b.strip()],
                    "diseases": [d.strip() for d in str(row.get("diseases", "")).split(";") if d.strip()],
                    "chemical_composition": {
                        "ingredients": {}
                    }
                }
                
                # Parse ingredients and SMILES
                ingredients = str(row.get("ingredients", "")).split(";")
                smiles_list = str(row.get("smiles", "")).split(";")
                
                for i, ingredient in enumerate(ingredients):
                    ingredient = ingredient.strip()
                    if ingredient:
                        if i < len(smiles_list):
                            smiles = smiles_list[i].strip()
                            if smiles:
                                medicine["chemical_composition"]["ingredients"][ingredient] = {
                                    "primary_smiles": smiles
                                }
                        else:
                            medicine["chemical_composition"]["ingredients"][ingredient] = {}
                
                medicines.append(medicine)
            
            logger.info(f"Successfully imported {len(medicines)} medicines from CSV")
            return medicines
            
        except Exception as e:
            logger.error(f"Error importing from CSV: {e}")
            return []

    @staticmethod
    def from_excel(file_path: str, sheet_name: str = "Sheet1") -> List[Dict[str, Any]]:
        """
        Import data from Excel file.
        
        Args:
            file_path: Path to Excel file
            sheet_name: Name of the sheet to read
            
        Returns:
            List of medicine dictionaries
        """
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            return DataImporter.from_dataframe(df)
        except Exception as e:
            logger.error(f"Error importing from Excel: {e}")
            return []

    @staticmethod
    def from_dataframe(df: pd.DataFrame) -> List[Dict[str, Any]]:
        """
        Import data from pandas DataFrame.
        
        Args:
            df: Pandas DataFrame with medicine data
            
        Returns:
            List of medicine dictionaries
        """
        medicines = []
        
        for _, row in df.iterrows():
            medicine = {
                "product_name": str(row.get("product_name", "")),
                "benefits": [b.strip() for b in str(row.get("benefits", "")).split(";") if b.strip()],
                "diseases": [d.strip() for d in str(row.get("diseases", "")).split(";") if d.strip()],
                "chemical_composition": {
                    "ingredients": {}
                }
            }
            
            # Parse ingredients and SMILES
            ingredients = str(row.get("ingredients", "")).split(";")
            smiles_list = str(row.get("smiles", "")).split(";")
            
            for i, ingredient in enumerate(ingredients):
                ingredient = ingredient.strip()
                if ingredient:
                    if i < len(smiles_list):
                        smiles = smiles_list[i].strip()
                        if smiles:
                            medicine["chemical_composition"]["ingredients"][ingredient] = {
                                "primary_smiles": smiles
                            }
                    else:
                        medicine["chemical_composition"]["ingredients"][ingredient] = {}
            
            medicines.append(medicine)
        
        return medicines

    @staticmethod
    def from_json(file_path: str) -> List[Dict[str, Any]]:
        """
        Import data from JSON file.
        
        Args:
            file_path: Path to JSON file
            
        Returns:
            List of medicine dictionaries
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and "medicines" in data:
                return data["medicines"]
            else:
                logger.error("Invalid JSON format")
                return []
                
        except Exception as e:
            logger.error(f"Error importing from JSON: {e}")
            return []

class DataExporter:
    """Utility class for exporting data to various formats."""
    
    @staticmethod
    def to_csv(medicines: List[Dict[str, Any]], file_path: str) -> bool:
        """
        Export medicines to CSV format.
        
        Args:
            medicines: List of medicine dictionaries
            file_path: Output file path
            
        Returns:
            True if successful, False otherwise
        """
        try:
            data = []
            for medicine in medicines:
                row = {
                    "product_name": medicine.get("product_name", ""),
                    "benefits": "; ".join(medicine.get("benefits", [])),
                    "diseases": "; ".join(medicine.get("diseases", [])),
                    "ingredients": "; ".join(medicine.get("chemical_composition", {}).get("ingredients", {}).keys()),
                    "smiles": "; ".join([
                        list(comp.values())[0].get("primary_smiles", "") 
                        for comp in medicine.get("chemical_composition", {}).get("ingredients", {}).values()
                        if comp and "primary_smiles" in comp
                    ]),
                    "entry_id": medicine.get("entry_id", ""),
                    "date_added": medicine.get("date_added", "")
                }
                data.append(row)
            
            df = pd.DataFrame(data)
            df.to_csv(file_path, index=False, encoding='utf-8')
            logger.info(f"Successfully exported {len(medicines)} medicines to CSV")
            return True
            
        except Exception as e:
            logger.error(f"Error exporting to CSV: {e}")
            return False

    @staticmethod
    def to_excel(medicines: List[Dict[str, Any]], file_path: str) -> bool:
        """
        Export medicines to Excel format.
        
        Args:
            medicines: List of medicine dictionaries
            file_path: Output file path
            
        Returns:
            True if successful, False otherwise
        """
        try:
            data = []
            for medicine in medicines:
                row = {
                    "product_name": medicine.get("product_name", ""),
                    "benefits": "; ".join(medicine.get("benefits", [])),
                    "diseases": "; ".join(medicine.get("diseases", [])),
                    "ingredients": "; ".join(medicine.get("chemical_composition", {}).get("ingredients", {}).keys()),
                    "smiles": "; ".join([
                        list(comp.values())[0].get("primary_smiles", "") 
                        for comp in medicine.get("chemical_composition", {}).get("ingredients", {}).values()
                        if comp and "primary_smiles" in comp
                    ]),
                    "entry_id": medicine.get("entry_id", ""),
                    "date_added": medicine.get("date_added", "")
                }
                data.append(row)
            
            df = pd.DataFrame(data)
            df.to_excel(file_path, index=False, engine='openpyxl')
            logger.info(f"Successfully exported {len(medicines)} medicines to Excel")
            return True
            
        except Exception as e:
            logger.error(f"Error exporting to Excel: {e}")
            return False

    @staticmethod
    def to_json(medicines: List[Dict[str, Any]], file_path: str, pretty: bool = True) -> bool:
        """
        Export medicines to JSON format.
        
        Args:
            medicines: List of medicine dictionaries
            file_path: Output file path
            pretty: Whether to format JSON with indentation
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                if pretty:
                    json.dump(medicines, f, indent=2, ensure_ascii=False)
                else:
                    json.dump(medicines, f, ensure_ascii=False)
            
            logger.info(f"Successfully exported {len(medicines)} medicines to JSON")
            return True
            
        except Exception as e:
            logger.error(f"Error exporting to JSON: {e}")
            return False

def create_sample_csv_template(file_path: str) -> bool:
    """
    Create a sample CSV template for medicine data.
    
    Args:
        file_path: Path where to create the template
        
    Returns:
        True if successful, False otherwise
    """
    try:
        sample_data = [
            {
                "product_name": "Turmeric",
                "benefits": "Anti-inflammatory; Antioxidant; Digestive health",
                "diseases": "Arthritis; Inflammation; Digestive disorders",
                "ingredients": "Curcumin; Turmerone; Zingiberene",
                "smiles": "CC(=O)OC1=CC=CC=C1C(=O)O; CC1=CC=C(C=C1)C(=O)CC2=CC=C(C=C2)OC; CC1=CC=C(C=C1)C(=O)CC2=CC=C(C=C2)OC"
            },
            {
                "product_name": "Ashwagandha",
                "benefits": "Stress relief; Energy boost; Immune support",
                "diseases": "Stress; Anxiety; Fatigue",
                "ingredients": "Withanolides; Withaferin A; Withanone",
                "smiles": "CC1=CC=C(C=C1)C(=O)CC2=CC=C(C=C2)OC; CC1=CC=C(C=C1)C(=O)CC2=CC=C(C=C2)OC; CC1=CC=C(C=C1)C(=O)CC2=CC=C(C=C2)OC"
            }
        ]
        
        df = pd.DataFrame(sample_data)
        df.to_csv(file_path, index=False, encoding='utf-8')
        logger.info(f"Sample CSV template created: {file_path}")
        return True
        
    except Exception as e:
        logger.error(f"Error creating CSV template: {e}")
        return False

# ============================================================================
# CHEMICAL ANALYSIS UTILITIES
# ============================================================================

def calculate_molecular_properties(smiles: str) -> Dict[str, Any]:
    """
    Calculate molecular properties for a given SMILES string.
    
    Args:
        smiles: SMILES string
        
    Returns:
        Dictionary containing molecular properties
    """
    try:
        # Import smiles_utils to use its molecular property calculation
        from .smiles_utils import get_molecular_properties, validate_smiles
        
        if not validate_smiles(smiles):
            return {"error": "Invalid SMILES string"}
        
        properties = get_molecular_properties(smiles)
        
        # Add molecular formula if available
        try:
            from rdkit import Chem
            mol = Chem.MolFromSmiles(smiles)
            if mol:
                properties["molecular_formula"] = Chem.rdMolDescriptors.CalcMolFormula(mol)
        except ImportError:
            pass
        
        return properties
        
    except Exception as e:
        logger.error(f"Error calculating molecular properties: {e}")
        return {"error": str(e)}

def validate_smiles(smiles: str) -> bool:
    """
    Validate SMILES string.
    
    Args:
        smiles: SMILES string to validate
        
    Returns:
        True if valid, False otherwise
    """
    try:
        from .smiles_utils import validate_smiles as smiles_validate
        return smiles_validate(smiles)
    except Exception as e:
        logger.error(f"Error validating SMILES: {e}")
        return False

def canonicalize_smiles(smiles: str) -> Optional[str]:
    """
    Convert SMILES to canonical form.
    
    Args:
        smiles: Input SMILES string
        
    Returns:
        Canonical SMILES string or None if invalid
    """
    try:
        from .smiles_utils import canonicalize_smiles as smiles_canonicalize
        return smiles_canonicalize(smiles)
    except Exception as e:
        logger.error(f"Error canonicalizing SMILES: {e}")
        return None

# ============================================================================
# DATA VALIDATION UTILITIES
# ============================================================================

def validate_medicine_data(medicine: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate medicine data structure and content.
    
    Args:
        medicine: Medicine dictionary to validate
        
    Returns:
        Dictionary containing validation results
    """
    validation_result = {
        "valid": True,
        "errors": [],
        "warnings": []
    }
    
    # Check required fields
    required_fields = ["product_name", "benefits", "diseases", "chemical_composition"]
    for field in required_fields:
        if field not in medicine:
            validation_result["valid"] = False
            validation_result["errors"].append(f"Missing required field: {field}")
    
    # Check data types
    if "product_name" in medicine and not isinstance(medicine["product_name"], str):
        validation_result["valid"] = False
        validation_result["errors"].append("product_name must be a string")
    
    if "benefits" in medicine and not isinstance(medicine["benefits"], list):
        validation_result["valid"] = False
        validation_result["errors"].append("benefits must be a list")
    
    if "diseases" in medicine and not isinstance(medicine["diseases"], list):
        validation_result["valid"] = False
        validation_result["errors"].append("diseases must be a list")
    
    if "chemical_composition" in medicine and not isinstance(medicine["chemical_composition"], dict):
        validation_result["valid"] = False
        validation_result["errors"].append("chemical_composition must be a dictionary")
    
    # Validate SMILES if present
    if "chemical_composition" in medicine and "ingredients" in medicine["chemical_composition"]:
        for ingredient_name, ingredient_data in medicine["chemical_composition"]["ingredients"].items():
            if isinstance(ingredient_data, dict) and "smiles" in ingredient_data:
                smiles = ingredient_data["smiles"]
                if not validate_smiles(smiles):
                    validation_result["warnings"].append(f"Invalid SMILES for {ingredient_name}: {smiles}")
    
    return validation_result

def clean_medicine_data(medicine: Dict[str, Any]) -> Dict[str, Any]:
    """
    Clean and standardize medicine data.
    
    Args:
        medicine: Medicine dictionary to clean
        
    Returns:
        Cleaned medicine dictionary
    """
    cleaned_medicine = medicine.copy()
    
    # Standardize string fields
    if "product_name" in cleaned_medicine:
        cleaned_medicine["product_name"] = str(cleaned_medicine["product_name"]).strip()
    
    if "scientific_name" in cleaned_medicine:
        cleaned_medicine["scientific_name"] = str(cleaned_medicine["scientific_name"]).strip()
    
    if "description" in cleaned_medicine:
        cleaned_medicine["description"] = str(cleaned_medicine["description"]).strip()
    
    # Ensure lists are properly formatted
    if "benefits" in cleaned_medicine:
        if isinstance(cleaned_medicine["benefits"], str):
            cleaned_medicine["benefits"] = [b.strip() for b in cleaned_medicine["benefits"].split(",") if b.strip()]
        elif not isinstance(cleaned_medicine["benefits"], list):
            cleaned_medicine["benefits"] = []
    
    if "diseases" in cleaned_medicine:
        if isinstance(cleaned_medicine["diseases"], str):
            cleaned_medicine["diseases"] = [d.strip() for d in cleaned_medicine["diseases"].split(",") if d.strip()]
        elif not isinstance(cleaned_medicine["diseases"], list):
            cleaned_medicine["diseases"] = []
    
    # Clean chemical composition
    if "chemical_composition" in cleaned_medicine and isinstance(cleaned_medicine["chemical_composition"], dict):
        if "ingredients" in cleaned_medicine["chemical_composition"]:
            for ingredient_name, ingredient_data in cleaned_medicine["chemical_composition"]["ingredients"].items():
                if isinstance(ingredient_data, dict) and "smiles" in ingredient_data:
                    smiles = ingredient_data["smiles"]
                    if validate_smiles(smiles):
                        canonical_smiles = canonicalize_smiles(smiles)
                        if canonical_smiles:
                            ingredient_data["smiles"] = canonical_smiles
    
    return cleaned_medicine 