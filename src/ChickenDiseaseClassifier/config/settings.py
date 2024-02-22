from ChickenDiseaseClassifier.constants import *
from ChickenDiseaseClassifier.utils.common import read_yaml_file, create_directory_paths
from ChickenDiseaseClassifier.entities.setting_entity import IngestionSettings

# Class to load and manage configuration settings from YAML files.
class ConfigLoader:
    def __init__(self, settings_file_path=SETTINGS_FILE_PATH, parameters_file_path=PARAMETERS_FILE_PATH):
        # Load settings and parameters from YAML configuration files.
        self.settings = read_yaml_file(settings_file_path)
        self.parameters = read_yaml_file(parameters_file_path)

        # Ensure the base directory for storing artifacts exists.
        create_directory_paths([self.settings.artifacts_root])
    
    # Retrieve and return ingestion settings as an IngestionSettings instance.
    def fetch_ingestion_settings(self) -> IngestionSettings:
        ingestion_config = self.settings.data_download

        # Ensure the download directory exists.
        create_directory_paths([ingestion_config.download_directory])

        return IngestionSettings(
            download_directory=ingestion_config.download_directory,
            dataset_url=ingestion_config.dataset_url,
            dataset_archive_path=ingestion_config.dataset_archive_path,
            extraction_directory=ingestion_config.extraction_directory
        )