"""
Trad-Chem LLM - TradChem Service
Service wrapper for TradChem library functionality.
"""

import logging
from typing import List, Dict, Any, Optional
import sys
import os

# Add the parent directory to path to import tradchem
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from tradchem import TradChem
    from tradchem.utils.smiles_utils import validate_smiles, get_molecular_properties
    TRADCHEM_AVAILABLE = True
except ImportError:
    TRADCHEM_AVAILABLE = False
    logging.warning("TradChem library not available. Using mock service.")

logger = logging.getLogger(__name__)

class TradChemService:
    """Service wrapper for TradChem library."""
    
    def __init__(self, database_path: Optional[str] = None):
        self.tradchem = None
        self.database_path = database_path
        
        if TRADCHEM_AVAILABLE:
            try:
                self.tradchem = TradChem(database_path)
                logger.info("TradChem service initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize TradChem: {e}")
                self.tradchem = None
        else:
            logger.info("Using mock TradChem service")
    
    def list_medicines(self) -> List[str]:
        """List all medicines in the database."""
        if self.tradchem:
            return self.tradchem.list_medicines()
        else:
            return self._mock_list_medicines()
    
    def search_medicines(self, query: str, search_type: str = "name") -> List[Dict[str, Any]]:
        """Search medicines in the database."""
        if self.tradchem:
            return self.tradchem.search_medicines(query, search_type)
        else:
            return self._mock_search_medicines(query, search_type)
    
    def get_medicine_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """Get medicine by exact name."""
        if self.tradchem:
            return self.tradchem.get_medicine_by_name(name)
        else:
            return self._mock_get_medicine_by_name(name)
    
    def add_medicine(self, medicine_data: Dict[str, Any]) -> bool:
        """Add a new medicine to the database."""
        if self.tradchem:
            return self.tradchem.add_medicine(medicine_data)
        else:
            return self._mock_add_medicine(medicine_data)
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get database statistics."""
        if self.tradchem:
            return self.tradchem.get_statistics()
        else:
            return self._mock_get_statistics()
    
    def export_to_csv(self, file_path: str) -> bool:
        """Export database to CSV."""
        if self.tradchem:
            return self.tradchem.export_to_csv(file_path)
        else:
            return self._mock_export_to_csv(file_path)
    
    def backup_database(self, backup_path: Optional[str] = None) -> bool:
        """Create database backup."""
        if self.tradchem:
            return self.tradchem.backup_database(backup_path)
        else:
            return self._mock_backup_database(backup_path)
    
    def validate_smiles(self, smiles: str) -> bool:
        """Validate SMILES string."""
        if TRADCHEM_AVAILABLE:
            return validate_smiles(smiles)
        else:
            return self._mock_validate_smiles(smiles)
    
    def get_molecular_properties(self, smiles: str) -> Dict[str, Any]:
        """Get molecular properties for SMILES string."""
        if TRADCHEM_AVAILABLE:
            return get_molecular_properties(smiles)
        else:
            return self._mock_get_molecular_properties(smiles)
    
    def get_medicines_by_ingredient(self, ingredient: str) -> List[Dict[str, Any]]:
        """Get all medicines containing a specific ingredient."""
        if self.tradchem:
            return self.tradchem.search_medicines(ingredient, "ingredient")
        else:
            return self._mock_get_medicines_by_ingredient(ingredient)
    
    def get_medicines_by_benefit(self, benefit: str) -> List[Dict[str, Any]]:
        """Get all medicines with a specific benefit."""
        if self.tradchem:
            return self.tradchem.search_medicines(benefit, "benefit")
        else:
            return self._mock_get_medicines_by_benefit(benefit)
    
    def get_medicines_by_disease(self, disease: str) -> List[Dict[str, Any]]:
        """Get all medicines for a specific disease."""
        if self.tradchem:
            return self.tradchem.search_medicines(disease, "disease")
        else:
            return self._mock_get_medicines_by_disease(disease)
    
    # Mock methods for when TradChem is not available
    def _mock_list_medicines(self) -> List[str]:
        """Mock list of medicines."""
        return [
            "Kameshwari Rasayanaya",
            "Chandraprabha Vati",
            "Turmeric Extract",
            "Ginger Root Extract",
            "Ashwagandha Powder",
            "Neem Leaf Extract",
            "Tulsi (Holy Basil)",
            "Amla (Indian Gooseberry)",
            "Shatavari Root",
            "Brahmi (Bacopa)"
        ]
    
    def _mock_search_medicines(self, query: str, search_type: str) -> List[Dict[str, Any]]:
        """Mock search results."""
        mock_medicines = [
            {
                "product_name": "Kameshwari Rasayanaya",
                "benefits": ["Enhances vitality", "Boosts immunity"],
                "diseases": ["Weakness", "Fatigue"],
                "chemical_composition": {
                    "ingredients": {
                        "Cannabis": {
                            "cannabigerolic acid": "CCCCCC1=CC(=C(C(=C1C(=O)O)O)C/C=C(\\C)/CCC=C(C)C)O"
                        },
                        "Bee Honey": {
                            "Glucose": "C(C1C(C(C(C(O1)O)O)O)O)O"
                        }
                    }
                },
                "entry_id": "TC_000001",
                "date_added": "2024-01-01T00:00:00"
            },
            {
                "product_name": "Turmeric Extract",
                "benefits": ["Anti-inflammatory", "Antioxidant"],
                "diseases": ["Inflammation", "Arthritis"],
                "chemical_composition": {
                    "ingredients": {
                        "Curcumin": {
                            "primary_smiles": "CC1=CC(=C(C=C1)O)C(=O)O"
                        }
                    }
                },
                "entry_id": "TC_000002",
                "date_added": "2024-01-01T00:00:00"
            }
        ]
        
        # Simple mock search logic
        query_lower = query.lower()
        results = []
        
        for medicine in mock_medicines:
            if search_type == "name" and query_lower in medicine["product_name"].lower():
                results.append(medicine)
            elif search_type == "benefit" and any(query_lower in benefit.lower() for benefit in medicine["benefits"]):
                results.append(medicine)
            elif search_type == "disease" and any(query_lower in disease.lower() for disease in medicine["diseases"]):
                results.append(medicine)
            elif search_type == "ingredient" and any(query_lower in ingredient.lower() for ingredient in medicine["chemical_composition"]["ingredients"].keys()):
                results.append(medicine)
        
        return results
    
    def _mock_get_medicine_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """Mock get medicine by name."""
        medicines = self._mock_search_medicines(name, "name")
        return medicines[0] if medicines else None
    
    def _mock_add_medicine(self, medicine_data: Dict[str, Any]) -> bool:
        """Mock add medicine."""
        logger.info(f"Mock: Adding medicine {medicine_data.get('product_name', 'Unknown')}")
        return True
    
    def _mock_get_statistics(self) -> Dict[str, Any]:
        """Mock database statistics."""
        return {
            "total_medicines": 10,
            "total_benefits": 25,
            "total_diseases": 15,
            "total_ingredients": 20,
            "last_updated": "2024-01-01T00:00:00",
            "traditional_systems": ["Ayurvedic", "Traditional Chinese"],
            "avg_ingredients_per_medicine": 2.5
        }
    
    def _mock_export_to_csv(self, file_path: str) -> bool:
        """Mock CSV export."""
        logger.info(f"Mock: Exporting to {file_path}")
        return True
    
    def _mock_backup_database(self, backup_path: Optional[str] = None) -> bool:
        """Mock database backup."""
        logger.info(f"Mock: Creating backup at {backup_path or 'default location'}")
        return True
    
    def _mock_validate_smiles(self, smiles: str) -> bool:
        """Mock SMILES validation."""
        return len(smiles) > 5 and any(c.isdigit() for c in smiles) and any(c.isalpha() for c in smiles)
    
    def _mock_get_molecular_properties(self, smiles: str) -> Dict[str, Any]:
        """Mock molecular properties."""
        return {
            "molecular_weight": 368.38,
            "logp": 3.2,
            "hbd": 2,
            "hba": 4,
            "rotatable_bonds": 3,
            "aromatic_rings": 2,
            "tpsa": 74.6,
            "molar_refractivity": 105.2
        }
    
    def _mock_get_medicines_by_ingredient(self, ingredient: str) -> List[Dict[str, Any]]:
        """Mock get medicines by ingredient."""
        return self._mock_search_medicines(ingredient, "ingredient")
    
    def _mock_get_medicines_by_benefit(self, benefit: str) -> List[Dict[str, Any]]:
        """Mock get medicines by benefit."""
        return self._mock_search_medicines(benefit, "benefit")
    
    def _mock_get_medicines_by_disease(self, disease: str) -> List[Dict[str, Any]]:
        """Mock get medicines by disease."""
        return self._mock_search_medicines(disease, "disease") 