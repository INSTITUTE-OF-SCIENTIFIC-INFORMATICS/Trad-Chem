#!/usr/bin/env python3
"""
TradChem Colab Installation Script

This script installs and sets up the TradChem package in Google Colab.
Run this in a Colab cell to get started with TradChem.
"""

import subprocess
import sys
import os
from pathlib import Path

def install_package():
    """Install TradChem package in Colab."""
    print("🚀 Installing TradChem package...")
    
    # Install required dependencies first
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
            print(f"✅ Installed {dep}")
        except subprocess.CalledProcessError:
            print(f"⚠️  Failed to install {dep}")
    
    # Install optional analysis dependencies
    print("🔬 Installing analysis dependencies...")
    analysis_deps = [
        "rdkit-pypi>=2022.9.1"
    ]
    
    for dep in analysis_deps:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
            print(f"✅ Installed {dep}")
        except subprocess.CalledProcessError:
            print(f"⚠️  Failed to install {dep} (optional)")
    
    # Clone the repository if not already present
    repo_url = "https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem.git"
    repo_path = Path("/content/Trad-Chem")
    
    if not repo_path.exists():
        print("📥 Cloning TradChem repository...")
        try:
            subprocess.check_call(["git", "clone", repo_url, str(repo_path)])
            print("✅ Repository cloned successfully")
        except subprocess.CalledProcessError:
            print("❌ Failed to clone repository")
            return False
    else:
        print("📁 Repository already exists")
    
    # Install the package in development mode
    print("🔧 Installing TradChem package...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", str(repo_path)])
        print("✅ TradChem package installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install package")
        return False
    
    return True

def test_installation():
    """Test if the installation was successful."""
    print("\n🧪 Testing installation...")
    
    try:
        from tradchem import TradChem
        print("✅ TradChem package imported successfully")
        
        # Test basic functionality
        tc = TradChem()
        print("✅ TradChem database loaded successfully")
        
        # Test statistics
        stats = tc.get_statistics()
        print(f"✅ Database statistics: {stats['total_medicines']} medicines found")
        
        # Test search
        results = tc.search_medicines("turmeric", limit=1)
        print(f"✅ Search functionality: {len(results)} results for 'turmeric'")
        
        print("\n🎉 TradChem is ready to use in Colab!")
        return True
        
    except Exception as e:
        print(f"❌ Installation test failed: {e}")
        return False

def setup_colab_environment():
    """Set up Colab-specific environment."""
    print("\n⚙️  Setting up Colab environment...")
    
    # Create example directory
    example_dir = Path("/content/tradchem_examples")
    example_dir.mkdir(exist_ok=True)
    print(f"📁 Created examples directory: {example_dir}")
    
    # Set up matplotlib for Colab
    try:
        import matplotlib.pyplot as plt
        plt.style.use('default')
        print("✅ Matplotlib configured for Colab")
    except:
        print("⚠️  Matplotlib configuration failed")
    
    return True

def main():
    """Main installation function."""
    print("🌿 TradChem Colab Installation")
    print("=" * 40)
    
    # Install package
    if not install_package():
        print("❌ Installation failed")
        return
    
    # Set up environment
    setup_colab_environment()
    
    # Test installation
    if not test_installation():
        print("❌ Installation test failed")
        return
    
    print("\n" + "=" * 40)
    print("🎉 Installation Complete!")
    print("\n📖 Next steps:")
    print("1. Import the package: from tradchem import TradChem")
    print("2. Initialize: tc = TradChem()")
    print("3. Start exploring: tc.search_medicines('your_query')")
    print("\n📚 Check the examples directory for tutorials")

if __name__ == "__main__":
    main() 