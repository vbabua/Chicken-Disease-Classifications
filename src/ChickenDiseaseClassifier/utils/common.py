from ensure import ensure_annotations
from pathlib import Path
from ChickenDiseaseClassifier import logger
from box import ConfigBox
from typing import List

import yaml
import os

@ensure_annotations
def read_yaml_file(yaml_path: Path) -> ConfigBox:
    """
    Read a YAML file and returns its contents as a ConfigBox.
    
    Args:
        yaml_path (Path): The path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.

    Returns:
        ConfigBox: The YAML content as a ConfigBox.
    """
    try:
        with open(yaml_path, 'r') as file:
            content = yaml.safe_load(file)
            if not content:
                raise ValueError("YAML file is empty")
            logger.info(f"YAML file {yaml_path} loaded successfully.")
            return ConfigBox(content)
    except yaml.YAMLError as e:
        logger.error(f"Error reading YAML file {yaml_path}: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise

@ensure_annotations
def create_directory_paths(path_to_directories: list, verbose=True):
    """
    Create a list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def get_file_size(path: Path) -> str:
    """
    Get size of file in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size = round(os.path.getsize(path)/1024)
    return f"~ {size} KB"
