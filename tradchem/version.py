"""
TradChem Version Information
Version and metadata information for the TradChem package

Author: Anu Gamage
"""

__version__ = "1.0.0"
__author__ = "Anu Gamage"
__description__ = "Traditional Medicine Database for LLM Integration"
__repository__ = "https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem"
__llm_chatbot__ = "https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem-LLM"

# Database version for tracking updates - Database versioning for update management
DATABASE_VERSION = "1.0.0"

# Release information - Package release details
RELEASE_DATE = "2024-01-01"
LICENSE = "MIT"

# Integration compatibility - LLM integration specifications
LLM_API_VERSION = "1.0"
SUPPORTED_FORMATS = ["json", "csv", "xlsx"]

# Package metadata - Complete package information
PACKAGE_INFO = {
    "name": "TradChem",
    "version": __version__,
    "author": __author__,
    "description": __description__,
    "repository": __repository__,
    "llm_chatbot": __llm_chatbot__,
    "database_version": DATABASE_VERSION,
    "release_date": RELEASE_DATE,
    "license": LICENSE,
    "llm_api_version": LLM_API_VERSION,
    "supported_formats": SUPPORTED_FORMATS
}
