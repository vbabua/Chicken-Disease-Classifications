import setuptools

# Reading the long description from the README.md file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Project version number
__version__ = "1.0.0"

# Repository and author details
REPO_NAME = "ChickenDiseaseClassifier"
AUTHOR_USER_NAME = "vbabua"  
SOURCE_REPO = "ChickenDiseaseClassifier"  
AUTHOR_EMAIL = "babuvadakemu@gmail.com"  

# Setup function to set package details
setuptools.setup(
    name = SOURCE_REPO,  # Name of the source package
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A comprehensive package for classifying chicken diseases using CNN",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # Project's GitHub URL
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},  # Directory for your source files
    packages = setuptools.find_packages(where="src"),  # Automatically find packages in `src`
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',  # Minimum version requirement of Python
)

