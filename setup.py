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
    author="TradChem Contributors",
    author_email="contributors@tradchem.org",
    description="A comprehensive chemical database for traditional medicinal systems",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/tradchem/tradchem",
    project_urls={
        "Bug Reports": "https://github.com/tradchem/tradchem/issues",
        "Source": "https://github.com/tradchem/tradchem",
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
        "full": [
            "rdkit-pypi>=2022.9.1",
            "fastapi>=0.68.0",
            "uvicorn>=0.15.0",
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
        "License :: OSI Approved :: Mozilla Public License Version 2.0",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    python_requires=">=3.7",
    keywords="traditional medicine, chemistry, database, SMILES, cheminformatics, ayurveda, herbal medicine",
    zip_safe=False,
)
