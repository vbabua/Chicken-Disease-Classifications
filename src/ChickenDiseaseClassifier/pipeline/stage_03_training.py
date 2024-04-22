from ChickenDiseaseClassifier.config.settings import ConfigLoader
from ChickenDiseaseClassifier.components.prepare_callbacks import BaseModelPreparation
from cnnClassifier.components.training import Training
from ChickenDiseaseClassifier import logger

# Define a constant for the stage name to improve readability and maintainability.
STAGE_NAME = "Training"

class PrepareModelTrainingPipeline:
    """
    Represents the pipeline stage for training the model in the ChickenDiseaseClassifier project.
    This class encapsulates the process from configuration loading to model training execution.
    """
    def __init__(self):
        """
        Initializes the PrepareModelTrainingPipeline object.
        """
        pass  # Currently, no initialization is required.

    def main(self):
        """
        Main method to execute the model training process.
        """
        # Load configuration settings for the training stage using ConfigLoader.
        config_manager = ConfigLoader()
        
        # Retrieve callback configuration and prepare callbacks.
        callbacks_config = config_manager.fetch_callback_config()
        prepare_callbacks = CallbackPreparer(config=callbacks_config)
        callback_list = prepare_callbacks.get_callbacks()

        # Retrieve training configuration and initialize the training process.
        training_config = config_manager.get_training_config()
        training = Training(config=training_config)
        
        # Load the base model, prepare data generators, and execute the training.
        training.load_base_model()
        training.prepare_data_generators()
        training.train_model(callback_list)

# Entry point for the script.
if __name__ == '__main__':
    try:
        # Log the start of the training stage with structured logging.
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Create an instance of the pipeline and execute the main process.
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        
        # Log the successful completion of the training stage.
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log any exceptions that occur during the training process.
        logger.exception(e)
        
        # Re-raise the exception for further handling or termination.
        raise e
        