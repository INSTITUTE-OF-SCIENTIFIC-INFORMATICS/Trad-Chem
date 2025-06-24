"""
TradChem - Traditional Medicine Chemical Analysis

A comprehensive Python package for analyzing traditional medicine data, 
chemical structures, and molecular properties. TradChem bridges the gap 
between traditional medicine systems and modern chemical analysis.

Core Components:
- Data Loading & Validation: Load and validate traditional medicine data
- Chemical Structure Analysis: Analyze molecular structures and properties
- Statistical Analysis: Perform comprehensive statistical analysis
- Traditional Medicine Analysis: Analyze traditional medicine systems
- Data Processing Tools: Filter, sort, and transform data
- SMILES Utilities: Validate and manipulate chemical structures
- Visualization Tools: Create comprehensive visualizations

Author: SaltyHeart
License: MIT
"""

from .tradchem import TradChem
from .version import __version__

# Import utility modules for direct access
from .utils import smiles_utils, data_utils

# Import medicine systems
from .medicine_systems import ayurvedic

__all__ = [
    'TradChem', 
    '__version__',
    'smiles_utils',
    'data_utils',
    'ayurvedic'
]

# Package metadata
__author__ = "SaltyHeart"
__email__ = "contributors@tradchem.org"
__description__ = "A comprehensive Python package for traditional medicine chemical analysis"
__url__ = "https://github.com/SaltyHeart/Trad-Chem"
__license__ = "MIT"
__keywords__ = [
    "traditional medicine", 
    "chemical analysis", 
    "molecular properties", 
    "drug discovery",
    "healthcare research",
    "SMILES",
    "RDKit"
] 