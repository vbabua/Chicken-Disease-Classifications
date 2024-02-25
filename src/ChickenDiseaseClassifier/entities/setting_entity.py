from dataclasses import dataclass
from pathlib import Path

# Define a dataclass to hold configuration settings for data ingestion.
@dataclass(frozen=True)
class IngestionSettings:
    # Local directory where dataset will be downloaded.
    download_directory: Path 

    # URL to download the dataset from. 
    dataset_url: str 

    # Local filepath to save the downloaded dataset archive. 
    dataset_archive_path: Path  

    # Directory to extract the contents of the dataset archive.
    extraction_directory: Path  


# Define a dataclass for base model configuration settings.
@dataclass(frozen=True)
class BaseModelConfig:
    # Directory for storing models and their modifications.
    model_directory: Path

    # File path for the initially loaded base model.
    initial_model_path: Path

    # File path for the customized or modified model.
    modified_model_path: Path

    # Dimensions for input images (height, width, depth).
    image_dimensions: list

    # Learning rate for the model optimizer.
    learning_rate: float

    # Flag to include pretrained weights in the model.
    include_pretrained_weights: bool

    # Source of the pretrained weights for the model.
    pretrained_weights: str

    # Number of output classes for the model.
    output_classes: int
