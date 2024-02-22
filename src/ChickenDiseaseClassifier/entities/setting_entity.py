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
