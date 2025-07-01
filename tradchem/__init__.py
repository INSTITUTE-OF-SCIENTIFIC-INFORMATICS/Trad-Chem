"""
TradChem - Traditional Medicine Database for LLM Integration

A comprehensive database for traditional medicine data,
optimized for integration with LLM chatbots and AI applications.

Author: SaltyHeart
Repository: https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem
LLM Chatbot: https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem-LLM
"""

from .tradchem import TradChem
from .version import __version__

# Import utility modules
from .utils import smiles_utils, data_utils

# Import medicine systems
from .medicine_systems import ayurvedic


def llm_query(query: str, context_limit: int = 5, include_smiles: bool = False, database_path: str = None):
    """
    Main LLM query function - optimized for AI chatbots.
    
    Args:
        query: Natural language query
        context_limit: Limit of results to return
        include_smiles: Whether to include SMILES chemical formulas
        database_path: Custom database path
        
    Returns:
        Structured LLM response
    """
    tc = TradChem(database_path)
    
    query_lower = query.lower()
    results = []
    
    # Multi-field intelligent search
    for medicine in tc.data:
        score = 0
        matched_fields = []
        
        # Product name search - highest weight
        if 'product_name' in medicine and query_lower in medicine['product_name'].lower():
            score += 10
            matched_fields.append('product_name')
        
        # Scientific name search
        if 'scientific_name' in medicine and query_lower in medicine.get('scientific_name', '').lower():
            score += 8
            matched_fields.append('scientific_name')
        
        # Benefits search
        if 'benefits' in medicine:
            for benefit in medicine['benefits']:
                if query_lower in benefit.lower():
                    score += 5
                    matched_fields.append('benefits')
                    break
        
        # Disease search
        if 'diseases' in medicine:
            for disease in medicine['diseases']:
                if query_lower in disease.lower():
                    score += 5
                    matched_fields.append('diseases')
                    break
        
        # Traditional system search
        if 'traditional_system' in medicine and query_lower in medicine.get('traditional_system', '').lower():
            score += 3
            matched_fields.append('traditional_system')
        
        # Geographic origin search
        if 'geographic_origin' in medicine and query_lower in medicine.get('geographic_origin', '').lower():
            score += 3
            matched_fields.append('geographic_origin')
        
        # Chemical composition search
        if 'chemical_composition' in medicine:
            comp = medicine['chemical_composition']
            if 'ingredients' in comp:
                for ingredient_name in comp['ingredients'].keys():
                    if query_lower in ingredient_name.lower():
                        score += 4
                        matched_fields.append('chemical_composition')
                        break
        
        if score > 0:
            result_entry = medicine.copy()
            result_entry['_relevance_score'] = score
            result_entry['_matched_fields'] = matched_fields
            results.append(result_entry)
    
    # Sort by relevance and limit results
    results.sort(key=lambda x: x['_relevance_score'], reverse=True)
    results = results[:context_limit]
    
    # Format as LLM-friendly response
    response = {
        "query": query,
        "total_found": len(results),
        "context_data": [],
        "database_context": {
            "total_medicines": len(tc.data),
            "description": "Traditional medicine database with chemical compositions and SMILES notations",
            "version": __version__
        }
    }
    
    # Format each search result
    for result in results:
        context_entry = {
            "product_name": result.get('product_name', 'Unknown'),
            "scientific_name": result.get('scientific_name', ''),
            "traditional_system": result.get('traditional_system', ''),
            "geographic_origin": result.get('geographic_origin', ''),
            "benefits": result.get('benefits', []),
            "diseases": result.get('diseases', []),
            "relevance_score": result.get('_relevance_score', 0),
            "matched_fields": result.get('_matched_fields', [])
        }
        
        # Include chemical composition if requested
        if include_smiles and 'chemical_composition' in result:
            context_entry["chemical_composition"] = result['chemical_composition']
        
        response["context_data"].append(context_entry)
    
    return response


def get_database_stats():
    """Get database statistics for LLM context."""
    tc = TradChem()
    
    systems = set()
    regions = set()
    total_benefits = 0
    total_diseases = 0
    
    for medicine in tc.data:
        if medicine.get('traditional_system'):
            systems.add(medicine['traditional_system'])
        if medicine.get('geographic_origin'):
            regions.add(medicine['geographic_origin'])
        if medicine.get('benefits'):
            total_benefits += len(medicine['benefits'])
        if medicine.get('diseases'):
            total_diseases += len(medicine['diseases'])
    
    return {
        "total_medicines": len(tc.data),
        "traditional_systems": sorted(list(systems)),
        "geographic_regions": sorted(list(regions)),
        "total_benefits": total_benefits,
        "total_diseases": total_diseases,
        "version": __version__,
        "description": "Traditional medicine database with chemical compositions and SMILES notations"
    }


def search_by_benefits(benefits_query: str, limit: int = 10):
    """Search traditional medicines by benefits."""
    tc = TradChem()
    query_lower = benefits_query.lower()
    results = []
    
    for medicine in tc.data:
        if 'benefits' in medicine:
            for benefit in medicine['benefits']:
                if query_lower in benefit.lower():
                    results.append(medicine)
                    break
    
    return results[:limit]


def search_by_disease(disease_query: str, limit: int = 10):
    """Search traditional medicines by disease."""
    tc = TradChem()
    query_lower = disease_query.lower()
    results = []
    
    for medicine in tc.data:
        if 'diseases' in medicine:
            for disease in medicine['diseases']:
                if query_lower in disease.lower():
                    results.append(medicine)
                    break
    
    return results[:limit]


def search_by_system(system_query: str, limit: int = 10):
    """Search medicines by traditional medicine system."""
    tc = TradChem()
    query_lower = system_query.lower()
    results = []
    
    for medicine in tc.data:
        if 'traditional_system' in medicine:
            if query_lower in medicine['traditional_system'].lower():
                results.append(medicine)
    
    return results[:limit]


def get_all_medicines(include_smiles: bool = False):
    """Get all medicines data."""
    tc = TradChem()
    medicines = tc.data.copy()
    
    if not include_smiles:
        # Remove SMILES data to reduce size
        for medicine in medicines:
            if 'chemical_composition' in medicine:
                comp = medicine['chemical_composition']
                if 'ingredients' in comp:
                    simplified_ingredients = {}
                    for ingredient_name in comp['ingredients'].keys():
                        simplified_ingredients[ingredient_name] = "Chemical data available"
                    medicine['chemical_composition']['ingredients'] = simplified_ingredients
    
    return medicines


# Main exports for Trad-Chem LLM use
__all__ = [
    'TradChem', 
    '__version__',
    'llm_query',
    'get_database_stats',
    'search_by_benefits',
    'search_by_disease',
    'search_by_system',
    'get_all_medicines',
    'smiles_utils',
    'data_utils',
    'ayurvedic'
]

# Project metadata
__author__ = "SaltyHeart"
__description__ = "Traditional medicine database for LLM integration"
__repository__ = "https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem"
__llm_chatbot__ = "https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem-LLM"