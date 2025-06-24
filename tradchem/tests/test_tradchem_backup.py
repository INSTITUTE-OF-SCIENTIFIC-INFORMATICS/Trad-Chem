"""
Comprehensive tests for TradChem package.

Tests all components including data loading, chemical analysis, statistical analysis,
traditional medicine analysis, and visualization tools.
"""

import pytest
import json
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

from tradchem import TradChem
from tradchem.utils import smiles_utils, data_utils
from tradchem.medicine_systems import ayurvedic


class TestTradChemCore:
    """Test core TradChem functionality."""
    
    def setup_method(self):
        """Set up test data."""
        self.sample_medicines = [
            {
                "product_name": "Turmeric Extract",
                "scientific_name": "Curcuma longa",
                "description": "Traditional anti-inflammatory herb",
                "traditional_system": "Ayurveda",
                "geographic_origin": "India",
                "benefits": ["Anti-inflammatory", "Antioxidant", "Digestive health"],
                "diseases": ["Arthritis", "Inflammation", "Digestive disorders"],
                "chemical_composition": {
                    "ingredients": {
                        "Curcumin": {
                            "smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
                            "molecular_weight": 368.38
                        },
                        "Turmerone": {
                            "smiles": "CC1=CC=C(C=C1)C(=O)CC2=CC=C(C=C2)OC",
                            "molecular_weight": 216.32
                        }
                    }
                }
            },
            {
                "product_name": "Ashwagandha Root",
                "scientific_name": "Withania somnifera",
                "description": "Adaptogenic herb for stress relief",
                "traditional_system": "Ayurveda",
                "geographic_origin": "India",
                "benefits": ["Stress relief", "Energy boost", "Immune support"],
                "diseases": ["Stress", "Anxiety", "Fatigue"],
                "chemical_composition": {
                    "ingredients": {
                        "Withanolides": {
                            "smiles": "CC1=CC=C(C=C1)C(=O)CC2=CC=C(C=C2)OC",
                            "molecular_weight": 470.62
                        }
                    }
                }
            }
        ]
        
        self.tc = TradChem()
    
    def test_initialization(self):
        """Test TradChem initialization."""
        assert self.tc is not None
        assert hasattr(self.tc, 'data')
        assert hasattr(self.tc, 'database_path')
    
    def test_load_data_json(self):
        """Test loading data from JSON file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(self.sample_medicines, f)
            temp_file = f.name
        
        try:
            medicines = self.tc.load_data(temp_file)
            assert len(medicines) == 2
            assert medicines[0]["product_name"] == "Turmeric Extract"
        finally:
            os.unlink(temp_file)
    
    def test_validate_data(self):
        """Test data validation."""
        validation_results = self.tc.validate_data(self.sample_medicines)
        
        assert validation_results["total_medicines"] == 2
        assert validation_results["valid_medicines"] == 2
        assert validation_results["invalid_medicines"] == 0
        assert validation_results["data_quality_score"] == 1.0
    
    def test_clean_data(self):
        """Test data cleaning."""
        # Add some unclean data
        unclean_medicines = [
            {
                "product_name": "  Test Medicine  ",
                "benefits": "Benefit1, Benefit2",
                "diseases": "Disease1, Disease2",
                "chemical_composition": {"ingredients": {}}
            }
        ]
        
        cleaned_medicines = self.tc.clean_data(unclean_medicines)
        
        assert cleaned_medicines[0]["product_name"] == "Test Medicine"
        assert isinstance(cleaned_medicines[0]["benefits"], list)
        assert len(cleaned_medicines[0]["benefits"]) == 2


class TestChemicalAnalysis:
    """Test chemical structure analysis functionality."""
    
    def setup_method(self):
        """Set up test data."""
        self.tc = TradChem()
        self.medicines_with_smiles = [
            {
                "product_name": "Test Medicine",
                "benefits": ["Test benefit"],
                "diseases": ["Test disease"],
                "chemical_composition": {
                    "ingredients": {
                        "Test Compound": {
                            "smiles": "CCO"  # Ethanol
                        }
                    }
                }
            }
        ]
    
    def test_analyze_chemical_structures(self):
        """Test chemical structure analysis."""
        analysis_results = self.tc.analyze_chemical_structures(self.medicines_with_smiles)
        
        assert analysis_results["total_compounds"] == 1
        assert "molecular_properties" in analysis_results
    
    def test_validate_smiles(self):
        """Test SMILES validation."""
        validation_results = self.tc.validate_smiles(self.medicines_with_smiles)
        
        assert validation_results["valid_count"] >= 0
        assert validation_results["invalid_count"] >= 0
        assert "validation_rate" in validation_results
    
    def test_calculate_molecular_properties(self):
        """Test molecular property calculation."""
        chemical_analysis = self.tc.analyze_chemical_structures(self.medicines_with_smiles)
        properties = self.tc.calculate_molecular_properties(chemical_analysis)
        
        assert isinstance(properties, dict)


class TestStatisticalAnalysis:
    """Test statistical analysis functionality."""
    
    def setup_method(self):
        """Set up test data."""
        self.tc = TradChem()
        self.test_medicines = [
            {
                "product_name": "Medicine 1",
                "traditional_system": "Ayurveda",
                "geographic_origin": "India",
                "benefits": ["Benefit 1", "Benefit 2"],
                "diseases": ["Disease 1"],
                "chemical_composition": {"ingredients": {}}
            },
            {
                "product_name": "Medicine 2",
                "traditional_system": "TCM",
                "geographic_origin": "China",
                "benefits": ["Benefit 1"],
                "diseases": ["Disease 2"],
                "chemical_composition": {"ingredients": {}}
            }
        ]
    
    def test_statistical_analysis(self):
        """Test statistical analysis."""
        stats_results = self.tc.statistical_analysis(self.test_medicines)
        
        assert stats_results["total_medicines"] == 2
        assert stats_results["unique_systems"] == 2
        assert stats_results["unique_regions"] == 2
        assert stats_results["avg_benefits_per_medicine"] == 1.5
        assert "system_distribution" in stats_results
        assert "region_distribution" in stats_results
        assert "benefit_frequency" in stats_results
    
    def test_correlation_analysis(self):
        """Test correlation analysis."""
        correlation_results = self.tc.correlation_analysis(self.test_medicines)
        
        assert isinstance(correlation_results, dict)
        assert "correlations" in correlation_results
        assert "strong_correlations" in correlation_results
    
    def test_pattern_analysis(self):
        """Test pattern analysis."""
        pattern_results = self.tc.pattern_analysis(self.test_medicines)
        
        assert isinstance(pattern_results, dict)
        assert "patterns" in pattern_results
        assert "common_combinations" in pattern_results


class TestTraditionalMedicineAnalysis:
    """Test traditional medicine analysis functionality."""
    
    def setup_method(self):
        """Set up test data."""
        self.tc = TradChem()
        self.test_medicines = [
            {
                "product_name": "Ayurvedic Medicine",
                "traditional_system": "Ayurveda",
                "geographic_origin": "India",
                "benefits": ["Anti-inflammatory", "Digestive"],
                "diseases": ["Arthritis", "Indigestion"],
                "chemical_composition": {
                    "ingredients": {
                        "Turmeric": {"smiles": "CCO"},
                        "Ginger": {"smiles": "CCO"}
                    }
                }
            }
        ]
    
    def test_analyze_traditional_systems(self):
        """Test traditional systems analysis."""
        system_results = self.tc.analyze_traditional_systems(self.test_medicines)
        
        assert "Ayurveda" in system_results
        assert system_results["Ayurveda"]["count"] == 1
        assert "geographic_origins" in system_results["Ayurveda"]
        assert "common_benefits" in system_results["Ayurveda"]
    
    def test_geographic_analysis(self):
        """Test geographic analysis."""
        geo_results = self.tc.geographic_analysis(self.test_medicines)
        
        assert "India" in geo_results
        assert geo_results["India"]["count"] == 1
        assert "systems" in geo_results["India"]
        assert "common_ingredients" in geo_results["India"]
    
    def test_benefit_analysis(self):
        """Test benefit analysis."""
        benefit_results = self.tc.benefit_analysis(self.test_medicines)
        
        assert "unique_benefits" in benefit_results
        assert "benefit_frequency" in benefit_results
        assert "benefit_by_system" in benefit_results
        assert "benefit_by_region" in benefit_results


class TestDataProcessing:
    """Test data processing functionality."""
    
    def setup_method(self):
        """Set up test data."""
        self.tc = TradChem()
        self.test_medicines = [
            {
                "product_name": "Medicine A",
                "traditional_system": "Ayurveda",
                "geographic_origin": "India",
                "benefits": ["Benefit A"],
                "diseases": ["Disease A"],
                "chemical_composition": {"ingredients": {}}
            },
            {
                "product_name": "Medicine B",
                "traditional_system": "TCM",
                "geographic_origin": "China",
                "benefits": ["Benefit B"],
                "diseases": ["Disease B"],
                "chemical_composition": {"ingredients": {}}
            }
        ]
    
    def test_filter_data(self):
        """Test data filtering."""
        # Filter by system
        filtered_ayurveda = self.tc.filter_data(self.test_medicines, system="Ayurveda")
        assert len(filtered_ayurveda) == 1
        assert filtered_ayurveda[0]["traditional_system"] == "Ayurveda"
        
        # Filter by region
        filtered_india = self.tc.filter_data(self.test_medicines, region="India")
        assert len(filtered_india) == 1
        assert filtered_india[0]["geographic_origin"] == "India"
    
    def test_sort_data(self):
        """Test data sorting."""
        # Sort by name
        sorted_by_name = self.tc.sort_data(self.test_medicines, by="name")
        assert sorted_by_name[0]["product_name"] == "Medicine A"
        assert sorted_by_name[1]["product_name"] == "Medicine B"
        
        # Sort by system
        sorted_by_system = self.tc.sort_data(self.test_medicines, by="system")
        assert sorted_by_system[0]["traditional_system"] == "Ayurveda"
        assert sorted_by_system[1]["traditional_system"] == "TCM"
    
    def test_export_data(self):
        """Test data export."""
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
            temp_file = f.name
        
        try:
            # Test JSON export
            success = self.tc.export_data(self.test_medicines, temp_file, 'json')
            assert success
            
            # Verify file was created
            assert os.path.exists(temp_file)
            
            # Test CSV export
            csv_file = temp_file.replace('.json', '.csv')
            success = self.tc.export_data(self.test_medicines, csv_file, 'csv')
            assert success
            assert os.path.exists(csv_file)
            
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
            if os.path.exists(csv_file):
                os.unlink(csv_file)


class TestVisualization:
    """Test visualization functionality."""
    
    def setup_method(self):
        """Set up test data."""
        self.tc = TradChem()
        self.test_medicines = [
            {
                "product_name": "Test Medicine",
                "traditional_system": "Ayurveda",
                "geographic_origin": "India",
                "benefits": ["Benefit 1", "Benefit 2"],
                "diseases": ["Disease 1"],
                "chemical_composition": {
                    "ingredients": {
                        "Test Compound": {
                            "smiles": "CCO",
                            "molecular_weight": 46.07
                        }
                    }
                }
            }
        ]
    
    @patch('matplotlib.pyplot.show')
    def test_plot_chemical_structures(self, mock_show):
        """Test chemical structure plotting."""
        self.tc.plot_chemical_structures(self.test_medicines)
        # Just verify the method doesn't raise an exception
        assert True
    
    @patch('matplotlib.pyplot.show')
    def test_plot_statistics(self, mock_show):
        """Test statistical plotting."""
        self.tc.plot_statistics(self.test_medicines)
        # Just verify the method doesn't raise an exception
        assert True
    
    @patch('matplotlib.pyplot.show')
    def test_plot_geographic_distribution(self, mock_show):
        """Test geographic distribution plotting."""
        self.tc.plot_geographic_distribution(self.test_medicines)
        # Just verify the method doesn't raise an exception
        assert True


class TestAyurvedicAnalysis:
    """Test Ayurvedic medicine system analysis."""
    
    def setup_method(self):
        """Set up test data."""
        self.test_medicines = [
            {
                "product_name": "Turmeric Medicine",
                "chemical_composition": {
                    "ingredients": {
                        "Turmeric": {"smiles": "CCO"},
                        "Ginger": {"smiles": "CCO"}
                    }
                }
            }
        ]
    
    def test_ayurvedic_analyzer_initialization(self):
        """Test AyurvedicAnalyzer initialization."""
        analyzer = ayurvedic.AyurvedicAnalyzer()
        assert analyzer is not None
        assert hasattr(analyzer, 'dosha_properties')
        assert hasattr(analyzer, 'rasa_properties')
        assert hasattr(analyzer, 'herb_classifications')
    
    def test_analyze_dosha_balance(self):
        """Test dosha balance analysis."""
        analyzer = ayurvedic.AyurvedicAnalyzer()
        dosha_results = analyzer.analyze_dosha_balance(self.test_medicines)
        
        assert "total_medicines" in dosha_results
        assert "dosha_distribution" in dosha_results
        assert "dosha_balancing" in dosha_results
        assert "dosha_aggravating" in dosha_results
    
    def test_analyze_rasa_distribution(self):
        """Test rasa distribution analysis."""
        analyzer = ayurvedic.AyurvedicAnalyzer()
        rasa_results = analyzer.analyze_rasa_distribution(self.test_medicines)
        
        assert "total_medicines" in rasa_results
        assert "rasa_distribution" in rasa_results
        assert "rasa_combinations" in rasa_results
        assert "common_rasas" in rasa_results
    
    def test_analyze_therapeutic_properties(self):
        """Test therapeutic properties analysis."""
        analyzer = ayurvedic.AyurvedicAnalyzer()
        therapeutic_results = analyzer.analyze_therapeutic_properties(self.test_medicines)
        
        assert "total_medicines" in therapeutic_results
        assert "therapeutic_categories" in therapeutic_results
        assert "common_properties" in therapeutic_results
        assert "dosha_specific_remedies" in therapeutic_results
    
    def test_recommend_formulations(self):
        """Test formulation recommendations."""
        analyzer = ayurvedic.AyurvedicAnalyzer()
        recommendations = analyzer.recommend_formulations("Vata", ["Anxiety", "Insomnia"])
        
        assert "dosha_imbalance" in recommendations
        assert "symptoms" in recommendations
        assert "recommended_herbs" in recommendations
        assert "avoid_herbs" in recommendations
        assert "formulation_suggestions" in recommendations
    
    def test_analyze_herb_interactions(self):
        """Test herb interaction analysis."""
        analyzer = ayurvedic.AyurvedicAnalyzer()
        interaction_results = analyzer.analyze_herb_interactions(["Turmeric", "Ginger"])
        
        assert "herbs" in interaction_results
        assert "synergistic_combinations" in interaction_results
        assert "potential_conflicts" in interaction_results
        assert "dosha_effects" in interaction_results
        assert "rasa_balance" in interaction_results
    
    def test_convenience_functions(self):
        """Test convenience functions."""
        # Test comprehensive analysis
        analysis_results = ayurvedic.analyze_ayurvedic_medicines(self.test_medicines)
        assert "dosha_analysis" in analysis_results
        assert "rasa_analysis" in analysis_results
        assert "therapeutic_analysis" in analysis_results
        
        # Test recommendations
        recommendations = ayurvedic.get_ayurvedic_recommendations("Pitta", ["Acidity"])
        assert "dosha_imbalance" in recommendations
        assert "recommended_herbs" in recommendations


class TestUtilityFunctions:
    """Test utility functions."""
    
    def test_smiles_utils(self):
        """Test SMILES utility functions."""
        # Test validation
        assert smiles_utils.validate_smiles("CCO")  # Valid SMILES
        assert not smiles_utils.validate_smiles("invalid")  # Invalid SMILES
        
        # Test canonicalization
        canonical = smiles_utils.canonicalize_smiles("CCO")
        assert canonical is not None
        
        # Test molecular properties
        properties = smiles_utils.get_molecular_properties("CCO")
        assert isinstance(properties, dict)
    
    def test_data_utils(self):
        """Test data utility functions."""
        # Test validation
        medicine = {
            "product_name": "Test",
            "benefits": ["Benefit"],
            "diseases": ["Disease"],
            "chemical_composition": {"ingredients": {}}
        }
        
        validation_result = data_utils.validate_medicine_data(medicine)
        assert validation_result["valid"] == True
        
        # Test cleaning
        cleaned_medicine = data_utils.clean_medicine_data(medicine)
        assert cleaned_medicine["product_name"] == "Test"
    
    def test_molecular_properties_calculation(self):
        """Test molecular properties calculation."""
        properties = data_utils.calculate_molecular_properties("CCO")
        assert isinstance(properties, dict)
    
    def test_smiles_validation(self):
        """Test SMILES validation in data utils."""
        assert data_utils.validate_smiles("CCO")
        assert not data_utils.validate_smiles("invalid")
    
    def test_smiles_canonicalization(self):
        """Test SMILES canonicalization in data utils."""
        canonical = data_utils.canonicalize_smiles("CCO")
        assert canonical is not None


class TestComprehensiveAnalysis:
    """Test comprehensive analysis functionality."""
    
    def setup_method(self):
        """Set up test data."""
        self.tc = TradChem()
        self.comprehensive_test_data = [
            {
                "product_name": "Comprehensive Medicine",
                "scientific_name": "Test Species",
                "description": "A comprehensive test medicine",
                "traditional_system": "Ayurveda",
                "geographic_origin": "India",
                "benefits": ["Anti-inflammatory", "Antioxidant", "Digestive"],
                "diseases": ["Arthritis", "Inflammation", "Indigestion"],
                "chemical_composition": {
                    "ingredients": {
                        "Curcumin": {
                            "smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
                            "molecular_weight": 368.38
                        },
                        "Gingerol": {
                            "smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
                            "molecular_weight": 294.38
                        }
                    }
                }
            }
        ]
    
    def test_comprehensive_analysis(self):
        """Test comprehensive analysis of medicines."""
        analysis_results = self.tc.analyze_medicines(self.comprehensive_test_data)
        
        # Check all analysis components are present
        assert "data_validation" in analysis_results
        assert "chemical_analysis" in analysis_results
        assert "statistical_analysis" in analysis_results
        assert "traditional_analysis" in analysis_results
        assert "geographic_analysis" in analysis_results
        assert "benefit_analysis" in analysis_results
        
        # Verify data validation
        validation = analysis_results["data_validation"]
        assert validation["total_medicines"] == 1
        assert validation["valid_medicines"] == 1
        
        # Verify chemical analysis
        chemical = analysis_results["chemical_analysis"]
        assert chemical["total_compounds"] >= 0
        
        # Verify statistical analysis
        stats = analysis_results["statistical_analysis"]
        assert stats["total_medicines"] == 1
        assert stats["unique_systems"] == 1
        
        # Verify traditional analysis
        traditional = analysis_results["traditional_analysis"]
        assert "Ayurveda" in traditional
        
        # Verify geographic analysis
        geographic = analysis_results["geographic_analysis"]
        assert "India" in geographic
        
        # Verify benefit analysis
        benefits = analysis_results["benefit_analysis"]
        assert "unique_benefits" in benefits
        assert "benefit_frequency" in benefits


if __name__ == "__main__":
    pytest.main([__file__])
