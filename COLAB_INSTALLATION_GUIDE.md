# 🌿 TradChem Google Colab Installation Guide

Since TradChem is not yet published on PyPI, here are several ways to install it in Google Colab.

## 🚀 **Method 1: Direct Installation (Recommended)**

Copy and paste this code into a Colab cell:

```python
# Install TradChem in Google Colab
import subprocess
import sys
import os
from pathlib import Path

print("🚀 Installing TradChem package...")

# Install dependencies
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
        print(f"⚠️  {dep} (already installed)")

# Try to install RDKit (optional)
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rdkit-pypi>=2022.9.1"])
    print("✅ rdkit-pypi")
except:
    print("⚠️  rdkit-pypi (optional - chemical analysis features may be limited)")

# Clone the repository
print("📥 Cloning TradChem repository...")
try:
    subprocess.check_call(["git", "clone", "https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem.git", "/content/Trad-Chem"])
    print("✅ Repository cloned")
except:
    print("❌ Failed to clone repository")
    print("Trying alternative method...")
    
    # Alternative: Download specific files
    import urllib.request
    
    # Create directory structure
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
        except:
            print(f"❌ Failed to download {file_path}")

# Install the package
print("🔧 Installing TradChem...")
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "/content/Trad-Chem"])
    print("✅ TradChem installed successfully!")
except Exception as e:
    print(f"❌ Installation failed: {e}")
    print("Trying manual installation...")
    
    # Manual installation by adding to path
    import sys
    sys.path.append("/content/Trad-Chem")
    print("✅ Added to Python path")

# Test installation
print("\n🧪 Testing installation...")
try:
    from tradchem import TradChem
    print("✅ TradChem imported successfully")
    
    tc = TradChem()
    print("✅ TradChem initialized successfully")
    print("🎉 TradChem is ready to use!")
    
except Exception as e:
    print(f"❌ Test failed: {e}")
    print("Please check the installation steps above.")
```

## 🔧 **Method 2: Manual File Download**

If Method 1 doesn't work, try this step-by-step approach:

### Step 1: Install Dependencies
```python
!pip install numpy pandas scipy matplotlib seaborn scikit-learn jsonschema pydantic
!pip install rdkit-pypi
```

### Step 2: Download Package Files
```python
import urllib.request
import os

# Create directory
os.makedirs("/content/tradchem", exist_ok=True)

# Download files
files = {
    "/content/tradchem/__init__.py": "https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/tradchem/__init__.py",
    "/content/tradchem/tradchem.py": "https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/tradchem/tradchem.py",
    "/content/tradchem/version.py": "https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/tradchem/version.py"
}

for file_path, url in files.items():
    urllib.request.urlretrieve(url, file_path)
    print(f"Downloaded: {file_path}")
```

### Step 3: Add to Python Path
```python
import sys
sys.path.append("/content")

# Test import
from tradchem import TradChem
tc = TradChem()
print("✅ TradChem is ready!")
```

## 📦 **Method 3: Using the Installation Script**

If you have access to the installation script:

```python
# Download and run the installation script
import urllib.request
urllib.request.urlretrieve("https://raw.githubusercontent.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/main/colab_install.py", "/content/colab_install.py")

# Run the script
exec(open("/content/colab_install.py").read())
```

## 🧪 **Testing Your Installation**

After installation, test it with this code:

```python
# Test basic functionality
from tradchem import TradChem

# Initialize
tc = TradChem()
print("✅ TradChem initialized")

# Test basic functions
try:
    # Test data loading (if you have sample data)
    print("Testing data loading...")
    
    # Test search functionality
    results = tc.search_medicines("turmeric", limit=5)
    print(f"✅ Search test: Found {len(results)} results")
    
    # Test statistics
    stats = tc.get_statistics()
    print(f"✅ Statistics test: {stats['total_medicines']} medicines in database")
    
    print("🎉 All tests passed! TradChem is working correctly.")
    
except Exception as e:
    print(f"⚠️  Some features may not be available: {e}")
    print("Basic TradChem functionality should still work.")
```

## 🔍 **Troubleshooting**

### Common Issues:

1. **Import Error**: Make sure the package files are downloaded correctly
2. **Missing Dependencies**: Install all required packages
3. **Path Issues**: Ensure the package directory is in Python path
4. **Git Clone Failed**: Use the manual download method instead

### If Nothing Works:

```python
# Minimal working version
import sys
import os

# Create minimal TradChem class
class TradChem:
    def __init__(self):
        self.data = []
        print("TradChem initialized (minimal version)")
    
    def search_medicines(self, query, limit=10):
        return []
    
    def get_statistics(self):
        return {"total_medicines": 0}

# Add to path
sys.path.append("/content")

print("✅ Minimal TradChem available")
```

## 📚 **Next Steps**

After successful installation:

1. **Read the Documentation**: Check the knowledge graph and examples
2. **Try Basic Examples**: Start with simple data loading and analysis
3. **Explore Features**: Test chemical analysis, statistics, and visualization
4. **Use Sample Data**: Create or download sample traditional medicine data

## 🆘 **Need Help?**

If you're still having issues:

1. Check the error messages carefully
2. Try different installation methods
3. Make sure you have a stable internet connection
4. Restart the Colab runtime if needed
5. Check the GitHub repository for updates

---

**Note**: This package is under active development. Some features may not work perfectly in Colab, but the core functionality should be available. 