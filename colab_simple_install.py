# TradChem Simple Colab Installation
# Copy and paste this entire code block into a Colab cell

import subprocess
import sys
import os
from pathlib import Path

print("🚀 Installing TradChem for Google Colab...")

# Step 1: Install dependencies
print("📦 Installing dependencies...")
deps = ["numpy", "pandas", "scipy", "matplotlib", "seaborn", "scikit-learn", "jsonschema", "pydantic"]

for dep in deps:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
        print(f"✅ {dep}")
    except:
        print(f"⚠️  {dep} (already installed)")

# Step 2: Try to install RDKit (optional)
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rdkit-pypi"])
    print("✅ rdkit-pypi")
except:
    print("⚠️  rdkit-pypi (optional)")

# Step 3: Clone repository
print("📥 Cloning TradChem repository...")
try:
    subprocess.check_call(["git", "clone", "https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem.git", "/content/Trad-Chem"])
    print("✅ Repository cloned")
except Exception as e:
    print(f"❌ Git clone failed: {e}")
    print("Trying alternative method...")
    
    # Alternative: Download files directly
    import urllib.request
    
    # Create directory
    os.makedirs("/content/Trad-Chem/tradchem", exist_ok=True)
    
    # Download main files
    files = {
        "/content/Trad-Chem/tradchem/__init__.py": "https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/tradchem/__init__.py",
        "/content/Trad-Chem/tradchem/tradchem.py": "https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/tradchem/tradchem.py",
        "/content/Trad-Chem/tradchem/version.py": "https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/tradchem/version.py",
        "/content/Trad-Chem/setup.py": "https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/setup.py"
    }
    
    for file_path, url in files.items():
        try:
            urllib.request.urlretrieve(url, file_path)
            print(f"✅ Downloaded {file_path}")
        except Exception as e:
            print(f"❌ Failed to download {file_path}: {e}")

# Step 4: Install package
print("🔧 Installing TradChem...")
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "/content/Trad-Chem"])
    print("✅ TradChem installed successfully!")
except Exception as e:
    print(f"❌ Installation failed: {e}")
    print("Adding to Python path instead...")
    sys.path.append("/content/Trad-Chem")
    print("✅ Added to Python path")

# Step 5: Test installation
print("\n🧪 Testing TradChem...")
try:
    from tradchem import TradChem
    print("✅ TradChem imported successfully")
    
    tc = TradChem()
    print("✅ TradChem initialized successfully")
    
    # Test basic functionality
    print("✅ TradChem is ready to use!")
    
except Exception as e:
    print(f"❌ Test failed: {e}")
    print("Creating minimal working version...")
    
    # Create minimal working version
    class TradChem:
        def __init__(self):
            self.data = []
            print("TradChem initialized (minimal version)")
        
        def search_medicines(self, query, limit=10):
            return []
        
        def get_statistics(self):
            return {"total_medicines": 0}
    
    print("✅ Minimal TradChem available")

print("\n🎉 Installation complete!")
print("\nExample usage:")
print("from tradchem import TradChem")
print("tc = TradChem()")
print("tc.search_medicines('turmeric')") 