import json
import os
from typing import List, Dict, Optional, Any
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TradChem:
    def __init__(self, database_path=None):
        # Use default database if not provided
        self.database_path = database_path or os.path.join(
            os.path.dirname(__file__), "data", "tradchem_database.json"
        )
        self.data = self.load_database()
        self._validate_database_structure()

    def _validate_database_structure(self):
        """Validate that all entries in the database have the required structure."""
        required_fields = ["product_name", "benefits", "diseases", "chemical_composition"]
        for i, entry in enumerate(self.data):
            missing_fields = [field for field in required_fields if field not in entry]
            if missing_fields:
                logger.warning(f"Entry {i} missing required fields: {missing_fields}")

    def load_database(self):
        """Load medicinal data from the JSON database."""
        try:
            with open(self.database_path, "r", encoding='utf-8') as file:
                data = json.load(file)
            logger.info(f"Successfully loaded {len(data)} entries from database")
            return data
        except FileNotFoundError:
            logger.error(f"Database file not found at {self.database_path}")
            return []
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in database file: {e}")
            return []

    def add_medicine(self, medicine_entry: Dict[str, Any]) -> bool:
        """Add a new medicine entry to the database with validation."""
        if self._validate_medicine_entry(medicine_entry):
            # Add metadata
            medicine_entry["date_added"] = datetime.now().isoformat()
            medicine_entry["entry_id"] = self._generate_entry_id()
            
            self.data.append(medicine_entry)
            self.save_database()
            logger.info(f"Successfully added medicine: {medicine_entry.get('product_name', 'Unknown')}")
            return True
        return False

    def _validate_medicine_entry(self, entry: Dict[str, Any]) -> bool:
        """Validate a medicine entry before adding to database."""
        required_fields = ["product_name", "benefits", "diseases", "chemical_composition"]
        
        # Check required fields
        for field in required_fields:
            if field not in entry:
                logger.error(f"Missing required field: {field}")
                return False
        
        # Check data types
        if not isinstance(entry["product_name"], str):
            logger.error("product_name must be a string")
            return False
        
        if not isinstance(entry["benefits"], list):
            logger.error("benefits must be a list")
            return False
            
        if not isinstance(entry["diseases"], list):
            logger.error("diseases must be a list")
            return False
            
        if not isinstance(entry["chemical_composition"], dict):
            logger.error("chemical_composition must be a dictionary")
            return False
        
        # Check for duplicate product names
        existing_names = [item.get("product_name", "") for item in self.data]
        if entry["product_name"] in existing_names:
            logger.warning(f"Medicine with name '{entry['product_name']}' already exists")
            return False
        
        return True

    def _generate_entry_id(self) -> str:
        """Generate a unique entry ID."""
        return f"TC_{len(self.data) + 1:06d}"

    def save_database(self):
        """Save the medicinal data to the JSON database."""
        try:
            with open(self.database_path, "w", encoding='utf-8') as file:
                json.dump(self.data, file, indent=4, ensure_ascii=False)
            logger.info(f"Data saved to {self.database_path}")
        except Exception as e:
            logger.error(f"Error saving database: {e}")

    def list_medicines(self) -> List[str]:
        """Return a list of all medicine product names."""
        return [entry.get("product_name", "Unknown") for entry in self.data]

    def search_medicines(self, query: str, search_type: str = "name") -> List[Dict[str, Any]]:
        """
        Search medicines by various criteria.
        
        Args:
            query: Search term
            search_type: Type of search ('name', 'benefit', 'disease', 'ingredient')
        """
        query = query.lower()
        results = []
        
        for entry in self.data:
            if search_type == "name":
                if query in entry.get("product_name", "").lower():
                    results.append(entry)
            elif search_type == "benefit":
                benefits = [b.lower() for b in entry.get("benefits", [])]
                if any(query in benefit for benefit in benefits):
                    results.append(entry)
            elif search_type == "disease":
                diseases = [d.lower() for d in entry.get("diseases", [])]
                if any(query in disease for disease in diseases):
                    results.append(entry)
            elif search_type == "ingredient":
                ingredients = entry.get("chemical_composition", {}).get("ingredients", {})
                if any(query in ingredient.lower() for ingredient in ingredients.keys()):
                    results.append(entry)
        
        return results

    def get_medicine_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """Get a specific medicine by its exact name."""
        for entry in self.data:
            if entry.get("product_name", "").lower() == name.lower():
                return entry
        return None

    def get_statistics(self) -> Dict[str, Any]:
        """Get database statistics."""
        total_medicines = len(self.data)
        total_benefits = len(set(benefit for entry in self.data for benefit in entry.get("benefits", [])))
        total_diseases = len(set(disease for entry in self.data for disease in entry.get("diseases", [])))
        
        # Count unique ingredients
        all_ingredients = set()
        for entry in self.data:
            ingredients = entry.get("chemical_composition", {}).get("ingredients", {})
            all_ingredients.update(ingredients.keys())
        
        return {
            "total_medicines": total_medicines,
            "total_benefits": total_benefits,
            "total_diseases": total_diseases,
            "total_ingredients": len(all_ingredients),
            "last_updated": datetime.now().isoformat()
        }

    def export_to_csv(self, output_path: str) -> bool:
        """Export database to CSV format for analysis."""
        try:
            import pandas as pd
            
            # Flatten the data for CSV export
            flattened_data = []
            for entry in self.data:
                flat_entry = {
                    "product_name": entry.get("product_name", ""),
                    "benefits": "; ".join(entry.get("benefits", [])),
                    "diseases": "; ".join(entry.get("diseases", [])),
                    "ingredients": "; ".join(entry.get("chemical_composition", {}).get("ingredients", {}).keys()),
                    "date_added": entry.get("date_added", ""),
                    "entry_id": entry.get("entry_id", "")
                }
                flattened_data.append(flat_entry)
            
            df = pd.DataFrame(flattened_data)
            df.to_csv(output_path, index=False, encoding='utf-8')
            logger.info(f"Database exported to {output_path}")
            return True
        except ImportError:
            logger.error("pandas is required for CSV export")
            return False
        except Exception as e:
            logger.error(f"Error exporting to CSV: {e}")
            return False

    def predict_outcome(self, input_data: Dict[str, Any]) -> str:
        """
        Placeholder for integrating an LLM prediction.
        The input_data can be processed to predict outcomes.
        """
        # Here you would integrate your LLM model prediction logic.
        return "Predicted outcome based on input data."

    def backup_database(self, backup_path: str = None) -> bool:
        """Create a backup of the current database."""
        if backup_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = f"{self.database_path}.backup_{timestamp}"
        
        try:
            with open(backup_path, "w", encoding='utf-8') as file:
                json.dump(self.data, file, indent=4, ensure_ascii=False)
            logger.info(f"Database backed up to {backup_path}")
            return True
        except Exception as e:
            logger.error(f"Error creating backup: {e}")
            return False

# Example usage if running as a script
if __name__ == "__main__":
    tradchem = TradChem()
    print("Current medicines:", tradchem.list_medicines())
    print("Database statistics:", tradchem.get_statistics())

