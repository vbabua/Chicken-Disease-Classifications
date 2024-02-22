import os
import urllib.request as request
import zipfile
from ChickenDiseaseClassifier.utils.common import get_file_size
from ChickenDiseaseClassifier import logger
from ChickenDiseaseClassifier.entities.setting_entity import IngestionSettings
from pathlib import Path

# Class responsible for downloading and extracting the dataset.
class DatasetDownloader:
    def __init__(self, settings: IngestionSettings):
        self.settings = settings  # Ingestion settings including URLs and directory paths.

    # Downloads the dataset from the specified URL if it's not already downloaded.
    def download_dataset(self):
        if not os.path.exists(self.settings.dataset_archive_path):
            file_name, headers = request.urlretrieve(
                url=self.settings.dataset_url,
                filename=self.settings.dataset_archive_path
            )
            logger.info(f"Downloaded: {file_name} with headers: \n{headers}")
        else:
            # Logs the existence of the dataset file if it's already downloaded.
            logger.info(f"Dataset file exists: {get_file_size(Path(self.settings.dataset_archive_path))}")

    # Extracts the dataset archive into a specified directory.
    def unzip_dataset(self):
        extraction_target = self.settings.extraction_directory
        os.makedirs(extraction_target, exist_ok=True)
        with zipfile.ZipFile(self.settings.dataset_archive_path, 'r') as zip_file:
            zip_file.extractall(extraction_target)