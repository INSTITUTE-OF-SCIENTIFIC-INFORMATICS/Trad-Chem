import json
import os

class TradChem:
    def __init__(self, database_path=None):
        # Use default database if not provided
        self.database_path = database_path or os.path.join(
            os.path.dirname(__file__), "data", "tradchem_database.json"
        )
        self.data = self.load_database()

    def load_database(self):
        """Load medicinal data from the JSON database."""
        try:
            with open(self.database_path, "r") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Database file not found at {self.database_path}.")
            return []

    def add_medicine(self, medicine_entry):
        """Add a new medicine entry to the database."""
        self.data.append(medicine_entry)
        self.save_database()

    def save_database(self):
        """Save the medicinal data to the JSON database."""
        with open(self.database_path, "w") as file:
            json.dump(self.data, file, indent=4)
        print(f"Data saved to {self.database_path}.")

    def list_medicines(self):
        """Return a list of all medicine product names."""
        return [entry.get("product_name", "Unknown") for entry in self.data]

    def predict_outcome(self, input_data):
        """
        Placeholder for integrating an LLM prediction.
        The input_data can be processed to predict outcomes.
        """
        # Here you would integrate your LLM model prediction logic.
        return "Predicted outcome based on input data."

# Example usage if running as a script
if __name__ == "__main__":
    tradchem = TradChem()
    print("Current medicines:", tradchem.list_medicines())

