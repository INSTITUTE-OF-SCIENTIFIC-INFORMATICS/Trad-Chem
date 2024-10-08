import json

def write_medicinal_data_to_json(file_path):
    # Data to be written to JSON
    # Trad-Chem_Library
    # Resource :
    data = [
        {
            "product_name": "Madana Modaka",
            "benefits": ["Enhances vitality", "Boosts immunity"],
            "diseases": ["Weakness", "Fatigue"],
            "ingredients": {
                "Cannabis": {
                    "THC": "C1=CC=C2C(=C1)C=CC=C2",
                    "CBD": "CC1=C2C(C=CC(=O)C2(O1)C)C"
                },
                "Bee Honey": {
                    "Glucose": "C(C1C(C(C(C(O1)O)O)O)O)O",
                    "Fructose": "C(C(C(C(C(=O)CO)O)O)O)O"
                },
                "Ghee": {
                    "Butyric Acid": "CCCC(=O)O",
                    "Palmitic Acid": "CCCCCCCCCCCCCCCC(=O)O"
                }
            }
        }
    ]

    # Writing to JSON file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Data has been written to {file_path}.")

# Call the function to write the data to a file
write_medicinal_data_to_json('madana_modhaka.json')
