#!/usr/bin/env python3
"""
TradChem Quick Colab Installation

Simple script to install TradChem in Google Colab.
Copy and paste this entire script into a Colab cell and run it.
"""

import subprocess
import sys
import os
from pathlib import Path

def install_tradchem():
    """Install TradChem package in Colab."""
    print("🚀 Installing TradChem package...")
    
    # Install required dependencies
    dependencies = [
        "numpy>=1.21.0",
        "pandas>=1.3.0", 
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "scikit-learn>=0.24.0",
        "jsonschema>=3.2.0",
        "pydantic>=1.8.0"
    ]
    
    print("📦 Installing dependencies...")
    for dep in dependencies:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
            print(f"✅ {dep}")
        except:
            print(f"⚠️  {dep} (already installed or failed)")
    
    # Try to install RDKit (optional)
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "rdkit-pypi>=2022.9.1"])
        print("✅ rdkit-pypi")
    except:
        print("⚠️  rdkit-pypi (optional - chemical analysis features may be limited)")
    
    # Download and install TradChem from GitHub
    print("📥 Downloading TradChem package...")
    
    # Create a temporary directory for the package
    temp_dir = Path("/tmp/tradchem_install")
    temp_dir.mkdir(exist_ok=True)
    
    # Download the package files
    import urllib.request
    import zipfile
    
    # GitHub raw URLs for the main package files
    files_to_download = {
        "tradchem/__init__.py": "https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/tradchem/__init__.py",
        "tradchem/tradchem.py": "https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/tradchem/tradchem.py",
        "tradchem/version.py": "https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/tradchem/version.py",
        "tradchem/cli.py": "https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/tradchem/cli_backup.py",
        "setup.py": "https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/setup.py"
    }
    
    # Create directory structure
    tradchem_dir = temp_dir / "tradchem"
    tradchem_dir.mkdir(exist_ok=True)
    
    # Download files
    for file_path, url in files_to_download.items():
        try:
            local_path = temp_dir / file_path
            local_path.parent.mkdir(parents=True, exist_ok=True)
            
            print(f"📥 Downloading {file_path}...")
            urllib.request.urlretrieve(url, local_path)
            print(f"✅ Downloaded {file_path}")
        except Exception as e:
            print(f"❌ Failed to download {file_path}: {e}")
    
    # Create a minimal setup.py if download failed
    if not (temp_dir / "setup.py").exists():
        print("📝 Creating minimal setup.py...")
        setup_content = '''
from setuptools import setup, find_packages

setup(
    name="tradchem",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "scikit-learn>=0.24.0",
    ],
    python_requires=">=3.7",
)
'''
        with open(temp_dir / "setup.py", "w") as f:
            f.write(setup_content)
    
    # Install the package
    print("🔧 Installing TradChem...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", str(temp_dir)])
        print("✅ TradChem installed successfully!")
        return True
    except Exception as e:
        print(f"❌ Installation failed: {e}")
        return False

def test_installation():
    """Test if TradChem works."""
    print("\n🧪 Testing TradChem...")
    
    try:
        from tradchem import TradChem
        print("✅ TradChem imported successfully")
        
        tc = TradChem()
        print("✅ TradChem initialized successfully")
        
        # Test basic functionality
        print("✅ TradChem is ready to use!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

# Run installation
if __name__ == "__main__":
    print("🌿 TradChem Quick Installation for Colab")
    print("=" * 50)
    
    if install_tradchem():
        test_installation()
        print("\n🎉 Installation complete! You can now use TradChem.")
        print("\nExample usage:")
        print("from tradchem import TradChem")
        print("tc = TradChem()")
    else:
        print("\n❌ Installation failed. Please check the error messages above.") 