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
                    json.dump(medicines, f, indent=4, ensure_ascii=False)
                else:
                    json.dump(medicines, f, ensure_ascii=False)
            
            logger.info(f"Successfully exported {len(medicines)} medicines to JSON")
            return True
            
        except Exception as e:
            logger.error(f"Error exporting to JSON: {e}")
            return False

def create_sample_csv_template(file_path: str) -> bool:
    """
    Create a sample CSV template for data entry.
    
    Args:
        file_path: Output file path
        
    Returns:
        True if successful, False otherwise
    """
    try:
        sample_data = [
            {
                "product_name": "Sample Medicine 1",
                "benefits": "Enhances vitality; Boosts immunity",
                "diseases": "Weakness; Fatigue",
                "ingredients": "Cannabis; Bee Honey",
                "smiles": "CCCCCC1=CC(=C(C(=C1C(=O)O)O)C/C=C(\\C)/CCC=C(C)C)O; C(C1C(C(C(C(O1)O)O)O)O)O"
            },
            {
                "product_name": "Sample Medicine 2",
                "benefits": "Reduces inflammation; Supports digestion",
                "diseases": "Inflammation; Digestive issues",
                "ingredients": "Turmeric; Ginger",
                "smiles": "CC1=CC(=C(C=C1C(=O)O)O)C(=O)O; CC(C)(C)CC1=CC(=C(C=C1)O)C(=O)O"
            }
        ]
        
        df = pd.DataFrame(sample_data)
        df.to_csv(file_path, index=False, encoding='utf-8')
        logger.info(f"Sample CSV template created at {file_path}")
        return True
        
    except Exception as e:
        logger.error(f"Error creating CSV template: {e}")
        return False 