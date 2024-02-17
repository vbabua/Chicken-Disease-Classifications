import os
from pathlib import Path
import logging

# Setup basic logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(levelname)s: %(message)s')

def create_project_structure(files_and_directories):
    """
    Create the directories and files for the project structure.

    Args:
    files_and_directories (list): A list of file and directory paths to create.
    """
    for path_str in files_and_directories:
        path = Path(path_str)
        try:
            # Check if the path is for a file
            if path.suffix:
                # Ensure the directory exists
                path.parent.mkdir(parents=True, exist_ok=True)
                
                # Create the file if it doesn't exist
                path.touch(exist_ok=True)
                
                logging.info(f"File created or already exists: {path}")
            else:
                # It's a directory; create it
                path.mkdir(parents=True, exist_ok=True)
                
                logging.info(f"Directory created or already exists: {path}")
        except Exception as e:
            logging.error(f"Failed to create {path}: {e}")

if __name__ == "__main__":
    # Project name for directory structuring
    project_name = "ChickenDiseaseClassifier"
    
    # List of directories and files to be created
    files_and_directories = [
        # Documentation folder
        "docs/.gitkeep",
        
        # Tests folder
        "tests/.gitkeep",
        # GitHub Actions CI/CD folder
        ".github/workflows/.gitkeep",
        
        # Source code directory
        f"src/{project_name}/__init__.py",
        
        # Components module within the project
        f"src/{project_name}/components/__init__.py",
        
        # Utilities module within the project
        f"src/{project_name}/utils/__init__.py",
        
        # Configuration module within the project
        f"src/{project_name}/config/__init__.py",
        
        # Configuration settings file
        f"src/{project_name}/config/settings.py",
        
        # Pipeline module within the project
        f"src/{project_name}/pipeline/__init__.py",
        
        # Entity definitions module
        f"src/{project_name}/entities/__init__.py",
        
        # Constants definitions module
        f"src/{project_name}/constants/__init__.py",
        
        # Application settings file
        "config/settings.yaml",
        
        # Data directory for storing datasets
        "data/.gitkeep",

        # DVC Configuration: Defines stages in the project's data processing and ML workflow.
        "dvc.yaml",
        
        # Parameters: YAML file.
        "parameters.yaml",
        
        # Jupyter notebooks for trials and research
        "notebooks/trials.ipynb",
        
        # Project dependencies file
        "requirements.txt",
        
        # Setup script for installation
        "setup.py",
        
        # Web templates directory
        "web/templates/index.html",
    ]

    create_project_structure(files_and_directories)
