"""
Ayurvedic Medicine System Analysis

This module provides comprehensive analysis tools for Ayurvedic traditional medicine,
including dosha analysis, rasa (taste) classification, and therapeutic properties.
"""

import logging
from typing import List, Dict, Any, Optional
from collections import Counter, defaultdict

logger = logging.getLogger(__name__)

# Ayurvedic classification systems
DOSHAS = ["Vata", "Pitta", "Kapha"]
RASAS = ["Madhura", "Amla", "Lavana", "Katu", "Tikta", "Kashaya"]
VIRYAS = ["Ushna", "Shita"]
VIPAKAS = ["Madhura", "Amla", "Katu"]

class AyurvedicAnalyzer:
    """
    Comprehensive analyzer for Ayurvedic medicine systems.
    
    Provides analysis of dosha balance, rasa classification, therapeutic properties,
    and traditional Ayurvedic formulations.
    """
    
    def __init__(self):
        """Initialize the Ayurvedic analyzer."""
        self.dosha_properties = self._load_dosha_properties()
        self.rasa_properties = self._load_rasa_properties()
        self.herb_classifications = self._load_herb_classifications()
    
    def _load_dosha_properties(self) -> Dict[str, Dict[str, Any]]:
        """Load dosha properties and characteristics."""
        return {
            "Vata": {
                "elements": ["Air", "Ether"],
                "qualities": ["Dry", "Light", "Cold", "Rough", "Subtle", "Mobile"],
                "functions": ["Movement", "Breathing", "Circulation", "Nerve impulses"],
                "imbalance_symptoms": ["Anxiety", "Insomnia", "Constipation", "Dry skin"]
            },
            "Pitta": {
                "elements": ["Fire", "Water"],
                "qualities": ["Hot", "Sharp", "Light", "Liquid", "Oily", "Spreading"],
                "functions": ["Digestion", "Metabolism", "Body temperature", "Intelligence"],
                "imbalance_symptoms": ["Acidity", "Inflammation", "Skin rashes", "Irritability"]
            },
            "Kapha": {
                "elements": ["Earth", "Water"],
                "qualities": ["Heavy", "Slow", "Cold", "Oily", "Smooth", "Dense"],
                "functions": ["Structure", "Lubrication", "Stability", "Immunity"],
                "imbalance_symptoms": ["Weight gain", "Lethargy", "Congestion", "Depression"]
            }
        }
    
    def _load_rasa_properties(self) -> Dict[str, Dict[str, Any]]:
        """Load rasa (taste) properties and effects."""
        return {
            "Madhura": {
                "taste": "Sweet",
                "elements": ["Earth", "Water"],
                "effects": ["Nourishing", "Calming", "Building"],
                "dosha_effect": {"Vata": "Decreases", "Pitta": "Decreases", "Kapha": "Increases"}
            },
            "Amla": {
                "taste": "Sour",
                "elements": ["Earth", "Fire"],
                "effects": ["Digestive", "Appetizing", "Heating"],
                "dosha_effect": {"Vata": "Decreases", "Pitta": "Increases", "Kapha": "Increases"}
            },
            "Lavana": {
                "taste": "Salty",
                "elements": ["Water", "Fire"],
                "effects": ["Digestive", "Laxative", "Heating"],
                "dosha_effect": {"Vata": "Decreases", "Pitta": "Increases", "Kapha": "Increases"}
            },
            "Katu": {
                "taste": "Pungent",
                "elements": ["Fire", "Air"],
                "effects": ["Stimulating", "Clearing", "Heating"],
                "dosha_effect": {"Vata": "Increases", "Pitta": "Increases", "Kapha": "Decreases"}
            },
            "Tikta": {
                "taste": "Bitter",
                "elements": ["Air", "Ether"],
                "effects": ["Detoxifying", "Cooling", "Lightening"],
                "dosha_effect": {"Vata": "Increases", "Pitta": "Decreases", "Kapha": "Decreases"}
            },
            "Kashaya": {
                "taste": "Astringent",
                "elements": ["Air", "Earth"],
                "effects": ["Absorbing", "Cooling", "Drying"],
                "dosha_effect": {"Vata": "Increases", "Pitta": "Decreases", "Kapha": "Decreases"}
            }
        }
    
    def _load_herb_classifications(self) -> Dict[str, Dict[str, Any]]:
        """Load herb classifications and properties."""
        return {
            "Turmeric": {
                "rasa": "Katu",
                "virya": "Ushna",
                "vipaka": "Katu",
                "dosha_effect": {"Vata": "Decreases", "Pitta": "Decreases", "Kapha": "Decreases"},
                "properties": ["Anti-inflammatory", "Antioxidant", "Digestive"]
            },
            "Ginger": {
                "rasa": "Katu",
                "virya": "Ushna",
                "vipaka": "Madhura",
                "dosha_effect": {"Vata": "Decreases", "Pitta": "Increases", "Kapha": "Decreases"},
                "properties": ["Digestive", "Anti-nausea", "Anti-inflammatory"]
            },
            "Ashwagandha": {
                "rasa": "Tikta",
                "virya": "Ushna",
                "vipaka": "Madhura",
                "dosha_effect": {"Vata": "Decreases", "Pitta": "Decreases", "Kapha": "Increases"},
                "properties": ["Adaptogenic", "Tonic", "Calming"]
            },
            "Tulsi": {
                "rasa": "Katu",
                "virya": "Ushna",
                "vipaka": "Katu",
                "dosha_effect": {"Vata": "Decreases", "Pitta": "Decreases", "Kapha": "Decreases"},
                "properties": ["Immunomodulatory", "Antimicrobial", "Adaptogenic"]
            }
        }
    
    def analyze_dosha_balance(self, medicines: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analyze dosha balance in Ayurvedic medicines.
        
        Args:
            medicines: List of medicine dictionaries
            
        Returns:
            Dictionary containing dosha analysis results
        """
        dosha_analysis = {
            "total_medicines": len(medicines),
            "dosha_distribution": {"Vata": 0, "Pitta": 0, "Kapha": 0},
            "dosha_balancing": {"Vata": 0, "Pitta": 0, "Kapha": 0},
            "dosha_aggravating": {"Vata": 0, "Pitta": 0, "Kapha": 0},
            "common_herbs": [],
            "dosha_properties": self.dosha_properties
        }
        
        all_herbs = []
        
        for medicine in medicines:
            if "chemical_composition" in medicine and "ingredients" in medicine["chemical_composition"]:
                for herb_name in medicine["chemical_composition"]["ingredients"].keys():
                    all_herbs.append(herb_name)
                    
                    # Check if herb is in our classification
                    if herb_name in self.herb_classifications:
                        herb_data = self.herb_classifications[herb_name]
                        
                        # Count dosha effects
                        for dosha, effect in herb_data["dosha_effect"].items():
                            if effect == "Decreases":
                                dosha_analysis["dosha_balancing"][dosha] += 1
                            elif effect == "Increases":
                                dosha_analysis["dosha_aggravating"][dosha] += 1
        
        # Count herb frequencies
        herb_counts = Counter(all_herbs)
        dosha_analysis["common_herbs"] = [herb for herb, count in herb_counts.most_common(10)]
        
        return dosha_analysis
    
    def analyze_rasa_distribution(self, medicines: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analyze rasa (taste) distribution in Ayurvedic medicines.
        
        Args:
            medicines: List of medicine dictionaries
            
        Returns:
            Dictionary containing rasa analysis results
        """
        rasa_analysis = {
            "total_medicines": len(medicines),
            "rasa_distribution": {rasa: 0 for rasa in RASAS},
            "rasa_combinations": [],
            "rasa_properties": self.rasa_properties,
            "common_rasas": []
        }
        
        rasa_combinations = []
        
        for medicine in medicines:
            if "chemical_composition" in medicine and "ingredients" in medicine["chemical_composition"]:
                medicine_rasas = []
                
                for herb_name in medicine["chemical_composition"]["ingredients"].keys():
                    if herb_name in self.herb_classifications:
                        herb_rasa = self.herb_classifications[herb_name]["rasa"]
                        medicine_rasas.append(herb_rasa)
                        rasa_analysis["rasa_distribution"][herb_rasa] += 1
                
                if medicine_rasas:
                    rasa_combinations.append(tuple(sorted(set(medicine_rasas))))
        
        # Count rasa combinations
        combination_counts = Counter(rasa_combinations)
        rasa_analysis["rasa_combinations"] = [
            {"combination": list(combo), "count": count} 
            for combo, count in combination_counts.most_common(5)
        ]
        
        # Find most common rasas
        rasa_analysis["common_rasas"] = [
            rasa for rasa, count in sorted(
                rasa_analysis["rasa_distribution"].items(), 
                key=lambda x: x[1], reverse=True
            )[:3]
        ]
        
        return rasa_analysis
    
    def analyze_therapeutic_properties(self, medicines: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analyze therapeutic properties of Ayurvedic medicines.
        
        Args:
            medicines: List of medicine dictionaries
            
        Returns:
            Dictionary containing therapeutic analysis results
        """
        therapeutic_analysis = {
            "total_medicines": len(medicines),
            "therapeutic_categories": {},
            "common_properties": [],
            "dosha_specific_remedies": {"Vata": [], "Pitta": [], "Kapha": []},
            "herb_property_mapping": {}
        }
        
        all_properties = []
        herb_properties = defaultdict(set)
        
        for medicine in medicines:
            if "chemical_composition" in medicine and "ingredients" in medicine["chemical_composition"]:
                for herb_name in medicine["chemical_composition"]["ingredients"].keys():
                    if herb_name in self.herb_classifications:
                        herb_data = self.herb_classifications[herb_name]
                        properties = herb_data.get("properties", [])
                        
                        all_properties.extend(properties)
                        
                        for prop in properties:
                            herb_properties[herb_name].add(prop)
                        
                        # Categorize by dosha effect
                        for dosha, effect in herb_data["dosha_effect"].items():
                            if effect == "Decreases":
                                therapeutic_analysis["dosha_specific_remedies"][dosha].append(herb_name)
        
        # Count property frequencies
        property_counts = Counter(all_properties)
        therapeutic_analysis["common_properties"] = [
            prop for prop, count in property_counts.most_common(10)
        ]
        
        # Create herb-property mapping
        therapeutic_analysis["herb_property_mapping"] = {
            herb: list(props) for herb, props in herb_properties.items()
        }
        
        return therapeutic_analysis
    
    def recommend_formulations(self, dosha_imbalance: str, symptoms: List[str]) -> Dict[str, Any]:
        """
        Recommend Ayurvedic formulations based on dosha imbalance and symptoms.
        
        Args:
            dosha_imbalance: Primary dosha imbalance ("Vata", "Pitta", "Kapha")
            symptoms: List of symptoms
            
        Returns:
            Dictionary containing formulation recommendations
        """
        recommendations = {
            "dosha_imbalance": dosha_imbalance,
            "symptoms": symptoms,
            "recommended_herbs": [],
            "avoid_herbs": [],
            "formulation_suggestions": [],
            "lifestyle_recommendations": []
        }
        
        # Find herbs that balance the imbalanced dosha
        balancing_herbs = []
        aggravating_herbs = []
        
        for herb_name, herb_data in self.herb_classifications.items():
            dosha_effect = herb_data["dosha_effect"].get(dosha_imbalance, "Neutral")
            
            if dosha_effect == "Decreases":
                balancing_herbs.append({
                    "herb": herb_name,
                    "rasa": herb_data["rasa"],
                    "properties": herb_data["properties"]
                })
            elif dosha_effect == "Increases":
                aggravating_herbs.append(herb_name)
        
        recommendations["recommended_herbs"] = balancing_herbs[:5]  # Top 5
        recommendations["avoid_herbs"] = aggravating_herbs[:5]  # Top 5 to avoid
        
        # Generate formulation suggestions
        if balancing_herbs:
            recommendations["formulation_suggestions"] = [
                f"Combine {balancing_herbs[0]['herb']} with {balancing_herbs[1]['herb']} for {dosha_imbalance} balance",
                f"Use {balancing_herbs[0]['herb']} tea for daily consumption",
                f"Create a powder blend with {', '.join([h['herb'] for h in balancing_herbs[:3]])}"
            ]
        
        # Lifestyle recommendations based on dosha
        dosha_props = self.dosha_properties.get(dosha_imbalance, {})
        recommendations["lifestyle_recommendations"] = [
            f"Follow {dosha_imbalance.lower()} pacifying diet",
            f"Practice calming activities to balance {dosha_imbalance}",
            f"Avoid {', '.join(dosha_props.get('imbalance_symptoms', [])[:2])}"
        ]
        
        return recommendations
    
    def analyze_herb_interactions(self, herbs: List[str]) -> Dict[str, Any]:
        """
        Analyze potential herb interactions and synergies.
        
        Args:
            herbs: List of herb names
            
        Returns:
            Dictionary containing interaction analysis
        """
        interaction_analysis = {
            "herbs": herbs,
            "synergistic_combinations": [],
            "potential_conflicts": [],
            "dosha_effects": {"Vata": 0, "Pitta": 0, "Kapha": 0},
            "rasa_balance": {rasa: 0 for rasa in RASAS}
        }
        
        # Calculate combined dosha effects
        for herb in herbs:
            if herb in self.herb_classifications:
                herb_data = self.herb_classifications[herb]
                
                # Count dosha effects
                for dosha, effect in herb_data["dosha_effect"].items():
                    if effect == "Increases":
                        interaction_analysis["dosha_effects"][dosha] += 1
                    elif effect == "Decreases":
                        interaction_analysis["dosha_effects"][dosha] -= 1
                
                # Count rasa distribution
                rasa = herb_data["rasa"]
                interaction_analysis["rasa_balance"][rasa] += 1
        
        # Find synergistic combinations
        for i, herb1 in enumerate(herbs):
            for herb2 in herbs[i+1:]:
                if herb1 in self.herb_classifications and herb2 in self.herb_classifications:
                    herb1_data = self.herb_classifications[herb1]
                    herb2_data = self.herb_classifications[herb2]
                    
                    # Check if they have complementary effects
                    if herb1_data["rasa"] != herb2_data["rasa"]:
                        interaction_analysis["synergistic_combinations"].append({
                            "herbs": [herb1, herb2],
                            "reason": f"Complementary rasas: {herb1_data['rasa']} and {herb2_data['rasa']}"
                        })
        
        return interaction_analysis

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

# Convenience functions for easy access
def analyze_ayurvedic_medicines(medicines: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Perform comprehensive Ayurvedic analysis on medicines.
    
    Args:
        medicines: List of medicine dictionaries
        
    Returns:
        Dictionary containing comprehensive Ayurvedic analysis
    """
    analyzer = AyurvedicAnalyzer()
    
    return {
        "dosha_analysis": analyzer.analyze_dosha_balance(medicines),
        "rasa_analysis": analyzer.analyze_rasa_distribution(medicines),
        "therapeutic_analysis": analyzer.analyze_therapeutic_properties(medicines)
    }

def get_ayurvedic_recommendations(dosha_imbalance: str, symptoms: List[str]) -> Dict[str, Any]:
    """
    Get Ayurvedic recommendations for dosha imbalance.
    
    Args:
        dosha_imbalance: Primary dosha imbalance
        symptoms: List of symptoms
        
    Returns:
        Dictionary containing recommendations
    """
    analyzer = AyurvedicAnalyzer()
    return analyzer.recommend_formulations(dosha_imbalance, symptoms)
