import re
import logging
from typing import Dict, List, Optional, Tuple
import json

logger = logging.getLogger(__name__)

# Try to import RDKit for advanced cheminformatics
try:
    from rdkit import Chem
    from rdkit.Chem import Descriptors, rdMolDescriptors
    RDKIT_AVAILABLE = True
except ImportError:
    RDKIT_AVAILABLE = False
    logger.warning("RDKit not available. Using basic SMILES validation only.")

def validate_smiles(smiles: str) -> bool:
    """
    Validate SMILES strings using RDKit if available, otherwise basic validation.
    
    Args:
        smiles: SMILES string to validate
        
    Returns:
        bool: True if valid SMILES, False otherwise
    """
    if not smiles or not isinstance(smiles, str):
        return False
    
    if RDKIT_AVAILABLE:
        try:
            mol = Chem.MolFromSmiles(smiles)
            return mol is not None
        except Exception as e:
            logger.error(f"RDKit validation error: {e}")
            return False
    else:
        # Basic validation: must contain at least one letter and one number
        if re.search("[A-Za-z]", smiles) and re.search("[0-9]", smiles):
            return True
        return False

def canonicalize_smiles(smiles: str) -> Optional[str]:
    """
    Convert SMILES into canonical form using RDKit.
    
    Args:
        smiles: Input SMILES string
        
    Returns:
        str: Canonical SMILES string, or None if invalid
    """
    if not RDKIT_AVAILABLE:
        logger.warning("RDKit not available for canonicalization")
        return smiles.strip()
    
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return None
        return Chem.MolToSmiles(mol, canonical=True)
    except Exception as e:
        logger.error(f"Error canonicalizing SMILES: {e}")
        return None

def get_molecular_properties(smiles: str) -> Dict[str, float]:
    """
    Calculate molecular properties for a given SMILES string.
    
    Args:
        smiles: SMILES string
        
    Returns:
        dict: Dictionary containing molecular properties
    """
    if not RDKIT_AVAILABLE:
        return {"error": "RDKit not available"}
    
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return {"error": "Invalid SMILES"}
        
        properties = {
            "molecular_weight": Descriptors.MolWt(mol),
            "logp": Descriptors.MolLogP(mol),
            "hbd": Descriptors.NumHDonors(mol),
            "hba": Descriptors.NumHAcceptors(mol),
            "rotatable_bonds": Descriptors.NumRotatableBonds(mol),
            "aromatic_rings": Descriptors.NumAromaticRings(mol),
            "tpsa": Descriptors.TPSA(mol),
            "molar_refractivity": Descriptors.MolMR(mol)
        }
        
        return properties
    except Exception as e:
        logger.error(f"Error calculating molecular properties: {e}")
        return {"error": str(e)}

def compare_smiles(smiles1: str, smiles2: str) -> Dict[str, any]:
    """
    Compare two SMILES strings and calculate similarity.
    
    Args:
        smiles1: First SMILES string
        smiles2: Second SMILES string
        
    Returns:
        dict: Comparison results including similarity metrics
    """
    if not RDKIT_AVAILABLE:
        return {"error": "RDKit not available for comparison"}
    
    try:
        mol1 = Chem.MolFromSmiles(smiles1)
        mol2 = Chem.MolFromSmiles(smiles2)
        
        if mol1 is None or mol2 is None:
            return {"error": "Invalid SMILES provided"}
        
        # Calculate Tanimoto similarity using Morgan fingerprints
        fp1 = Chem.AllChem.GetMorganFingerprintAsBitVect(mol1, 2)
        fp2 = Chem.AllChem.GetMorganFingerprintAsBitVect(mol2, 2)
        similarity = Chem.DataStructs.TanimotoSimilarity(fp1, fp2)
        
        return {
            "tanimoto_similarity": similarity,
            "molecular_weight_diff": abs(Descriptors.MolWt(mol1) - Descriptors.MolWt(mol2)),
            "logp_diff": abs(Descriptors.MolLogP(mol1) - Descriptors.MolLogP(mol2))
        }
    except Exception as e:
        logger.error(f"Error comparing SMILES: {e}")
        return {"error": str(e)}

def extract_smiles_from_text(text: str) -> List[str]:
    """
    Extract potential SMILES strings from text.
    
    Args:
        text: Text containing potential SMILES strings
        
    Returns:
        list: List of potential SMILES strings found in text
    """
    # Pattern to match SMILES-like strings
    smiles_pattern = r'[A-Za-z0-9@+\-\[\]\(\)=#%\.]+'
    potential_smiles = re.findall(smiles_pattern, text)
    
    # Filter for likely SMILES strings
    valid_smiles = []
    for smiles in potential_smiles:
        if len(smiles) > 5 and validate_smiles(smiles):
            valid_smiles.append(smiles)
    
    return valid_smiles

def create_smiles_report(smiles_list: List[str]) -> Dict[str, any]:
    """
    Create a comprehensive report for a list of SMILES strings.
    
    Args:
        smiles_list: List of SMILES strings to analyze
        
    Returns:
        dict: Comprehensive report with statistics and properties
    """
    if not RDKIT_AVAILABLE:
        return {"error": "RDKit not available for detailed analysis"}
    
    report = {
        "total_smiles": len(smiles_list),
        "valid_smiles": 0,
        "invalid_smiles": 0,
        "canonical_smiles": [],
        "molecular_properties": [],
        "statistics": {}
    }
    
    valid_smiles = []
    all_properties = []
    
    for smiles in smiles_list:
        if validate_smiles(smiles):
            report["valid_smiles"] += 1
            canonical = canonicalize_smiles(smiles)
            if canonical:
                valid_smiles.append(canonical)
                properties = get_molecular_properties(canonical)
                if "error" not in properties:
                    all_properties.append(properties)
        else:
            report["invalid_smiles"] += 1
    
    report["canonical_smiles"] = valid_smiles
    
    # Calculate statistics if we have properties
    if all_properties:
        mw_values = [p.get("molecular_weight", 0) for p in all_properties]
        logp_values = [p.get("logp", 0) for p in all_properties]
        
        report["statistics"] = {
            "avg_molecular_weight": sum(mw_values) / len(mw_values),
            "min_molecular_weight": min(mw_values),
            "max_molecular_weight": max(mw_values),
            "avg_logp": sum(logp_values) / len(logp_values),
            "min_logp": min(logp_values),
            "max_logp": max(logp_values)
        }
    
    return report

def save_smiles_report(report: Dict[str, any], filename: str) -> bool:
    """
    Save a SMILES report to a JSON file.
    
    Args:
        report: SMILES report dictionary
        filename: Output filename
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)
        logger.info(f"SMILES report saved to {filename}")
        return True
    except Exception as e:
        logger.error(f"Error saving SMILES report: {e}")
        return False
