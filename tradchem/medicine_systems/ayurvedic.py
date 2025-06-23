def get_ayurvedic_medicines():
    """
    Returns a sample list of Ayurvedic medicines.
    In a real-world scenario, this data would be loaded from a dedicated
    database or an external API.
    """
    return [
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
            }
        },
        {
            "product_name": "Chandraprabha Vati",
            "benefits": ["Supports urinary health", "Reduces inflammation"],
            "diseases": ["Urinary tract infections", "Diabetes"],
            "chemical_composition": {
                "ingredients": {
                    "Guggulu": {
                        "guggulsterone": "C1=CC(=O)C=C1"
                    },
                    "Shilajit": {
                        "fulvic_acid": "Fulvic acid SMILES placeholder"
                    }
                }
            }
        }
    ]
