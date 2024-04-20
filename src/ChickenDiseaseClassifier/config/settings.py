from ChickenDiseaseClassifier.constants import *
import os
from ChickenDiseaseClassifier.utils.common import read_yaml_file, create_directory_paths
from ChickenDiseaseClassifier.entities.setting_entity import (IngestionSettings,
                                                            BaseModelConfig, 
                                                            CallbackConfig)

# Class to load and manage configuration settings from YAML files.
class ConfigLoader:
    def __init__(self, settings_file_path=SETTINGS_FILE_PATH, parameters_file_path=PARAMETERS_FILE_PATH):
        # Load settings and parameters from YAML configuration files.
        self.settings = read_yaml_file(settings_file_path)
        self.parameters = read_yaml_file(parameters_file_path)

        # Ensure the base directory for storing artifacts exists.
        create_directory_paths([self.settings.artifacts_root])
    
    def fetch_ingestion_settings(self) -> IngestionSettings:
        """
        Load and return ingestion settings from the configuration, ensuring necessary directories are created.
        """
        ingestion_config = self.settings.data_download

        # Ensure the download directory exists.
        create_directory_paths([ingestion_config.download_directory])

        return IngestionSettings(
            download_directory=ingestion_config.download_directory,
            dataset_url=ingestion_config.dataset_url,
            dataset_archive_path=ingestion_config.dataset_archive_path,
            extraction_directory=ingestion_config.extraction_directory
        )

    def fetch_base_model_config(self) -> BaseModelConfig:
        """
        Load and return base model configuration, including paths and model parameters, while ensuring required directories are created.
        """
        model_config = self.settings.base_model

        # Ensure the model directory path exists.
        create_directory_paths([model_config.model_directory])

        return BaseModelConfig(
            model_directory=model_config.model_directory,
            initial_model_path=model_config.initial_model_path,
            modified_model_path=model_config.modified_model_path,
            image_dimensions=self.parameters.IMAGE_SIZE,
            learning_rate=self.parameters.LEARNING_RATE,
            include_pretrained_weights=self.parameters.INCLUDE_TOP,
            pretrained_weights=self.parameters.WEIGHTS,
            output_classes=self.parameters.CLASSES
        )
    
    def fetch_callback_config(self) -> CallbackConfig:
        """
        Load and return configuration for training callbacks such as model checkpointing and TensorBoard logging, ensuring all paths are valid and created.
        """
        callback_config = self.settings.prepare_callbacks
        
        # Ensure all necessary directories for callbacks exist, including the model checkpoint's directory and TensorBoard logs.
        create_directory_paths([
            callback_config.callbacks_directory,
            callback_config.tensorboard_logs_directory,
            os.path.dirname(callback_config.model_checkpoint_path)
        ])

        return CallbackConfig(
            callbacks_directory=Path(callback_config.callbacks_directory),
            tensorboard_logs_directory=Path(callback_config.tensorboard_logs_directory),
            model_checkpoint_path=Path(callback_config.model_checkpoint_path)
        )