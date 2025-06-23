"""
Trad-Chem LLM - Database Dependency
Database dependency injection for FastAPI.
"""

from .services.tradchem_service import TradChemService
import os

# Global TradChem service instance
_tradchem_service = None

def get_tradchem_service() -> TradChemService:
    """Get TradChem service instance."""
    global _tradchem_service
    
    if _tradchem_service is None:
        # Get database path from environment or use default
        database_path = os.getenv("TRADCHEM_DATABASE_PATH")
        _tradchem_service = TradChemService(database_path)
    
    return _tradchem_service

def initialize_database():
    """Initialize the database service."""
    global _tradchem_service
    _tradchem_service = get_tradchem_service() 