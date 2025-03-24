from setuptools import setup, find_packages

setup(
    name="tradchem",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive chemical database for traditional medicinal systems.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/tradchem",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List any dependencies here, e.g.:
        # "pandas>=1.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
