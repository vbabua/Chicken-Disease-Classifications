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

# Define a data class for call back configuration
@dataclass(frozen=True)
class CallbackConfig:
    # Base directory for storing all callback-related files, such as logs and model checkpoints.
    callbacks_directory: Path

    # Directory where TensorBoard log files will be stored. These logs are used for visualizing the training process.
    tensorboard_logs_directory: Path

    # File path for saving the model's checkpoint. This includes the file name where the best model will be saved based on validation accuracy or loss.
    model_checkpoint_path: Path

# Define a dataclass for training
@dataclass(frozen=True)
class TrainingConfig:
    # Root directory where all training-related files will be stored.
    training_root_dir: Path
    
    # File path where the fully trained model will be saved.
    trained_model_path: Path
    
    # File path where the updated base model is stored, which may include pre-trained weights and modifications.
    updated_model_path: Path
    
    # Directory containing the training data, organized in a way that supports image data generators.
    training_data_dir: Path
    
    # Total number of epochs to train the model.
    num_epochs: int
    
    # Number of samples per batch to be used during training.
    batch_size: int
    
    # Flag to determine whether data augmentation should be used during training.
    use_data_augmentation: bool
    
    # The dimensions expected by the model for input images (height, width, channels).
    image_size: list

