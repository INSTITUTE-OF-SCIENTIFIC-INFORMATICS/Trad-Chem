from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="tradchem",
    version="0.2.0",
    author="SaltyHeart",
    author_email="contributors@tradchem.org",
    description="A comprehensive Python package for traditional medicine chemical database and analysis",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem",
    project_urls={
        "Bug Reports": "https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem/issues",
        "Source": "https://github.com/INSTITUTE-OF-SCIENTIFIC-INFORMATICS/Trad-Chem",
        "Documentation": "https://tradchem.readthedocs.io/",
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "tradchem": ["data/*.json"],
    },
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.12.0",
            "black>=21.0.0",
            "flake8>=3.9.0",
            "mypy>=0.910",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=0.5.0",
        ],
        "analysis": [
            "rdkit-pypi>=2022.9.1",
            "pandas>=1.3.0",
            "numpy>=1.21.0",
            "matplotlib>=3.4.0",
            "seaborn>=0.11.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "tradchem=tradchem.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
    keywords="traditional medicine, chemistry, database, SMILES, cheminformatics, ayurveda, herbal medicine, python package",
    zip_safe=False,
)
