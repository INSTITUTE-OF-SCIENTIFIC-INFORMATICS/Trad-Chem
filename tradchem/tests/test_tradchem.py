import os
import json
import unittest

from tradchem.tradchem import TradChem

class TestTradChem(unittest.TestCase):

    def setUp(self):
        # Use a temporary file for testing
        self.test_db = "test_tradchem_database.json"
        sample_data = [
            {
                "product_name": "Test Medicine",
                "benefits": ["Test Benefit"],
                "diseases": ["Test Disease"],
                "chemical_composition": {},
                "SMILES": "C1=CC=CC=C1"
            }
        ]
        with open(self.test_db, "w") as f:
            json.dump(sample_data, f, indent=4)
        self.tradchem = TradChem(database_path=self.test_db)

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_load_database(self):
        self.assertEqual(len(self.tradchem.data), 1)
        self.assertEqual(self.tradchem.data[0]["product_name"], "Test Medicine")

    def test_add_medicine(self):
        new_medicine = {
            "product_name": "New Medicine",
            "benefits": ["New Benefit"],
            "diseases": ["New Disease"],
            "chemical_composition": {},
            "SMILES": "C2=CC=CC=C2"
        }
        self.tradchem.add_medicine(new_medicine)
        self.assertEqual(len(self.tradchem.data), 2)
        self.assertIn("New Medicine", self.tradchem.list_medicines())

if __name__ == "__main__":
    unittest.main()
