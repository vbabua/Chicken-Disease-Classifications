from ChickenDiseaseClassifier.config.settings import ConfigManager
from ChickenDiseaseClassifier.components.prepare_base_model import BaseModelPreparation
from ChickenDiseaseClassifier import logger


# Define a constant for the stage name to improve readability and maintainability.
STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipeline:
    """
    Represents the pipeline stage for preparing the base model necessary for
    the ChickenDiseaseClassifier model training.
    """
    def __init__(self):
        """
        Initializes the PrepareBaseModelTrainingPipeline object.
        """
        pass  # Currently, no initialization is required.

    def main(self):
        """
        Main method to execute the base model preparation process.
        """
        # Load configuration settings for the base model preparation stage.
        config_manager = ConfigManager()
        base_model_config = config_manager.fetch_base_model_config()

        # Initialize the base model preparation process with the fetched configuration.
        base_model_preparer = BaseModelPreparation(config=base_model_config)

        # Load and prepare the base model
        base_model_preparer.load_and_prepare_base_model()

        # Customize the base model and save the modified version
        base_model_preparer.customize_and_save_model()

# Entry point for the script.
if __name__ == '__main__':
    try:
        # Log the start of the base model preparation stage with structured logging.
        logger.info(f"***** STAGE {STAGE_NAME} STARTED *****")

        # Create an instance of the pipeline and execute the main process.
        pipeline = PrepareBaseModelTrainingPipeline()
        pipeline.main()

        # Log the successful completion of the base model preparation stage.
        logger.info(f"***** STAGE {STAGE_NAME} COMPLETED *****\n\n==========")
    except Exception as e:
        # Log any exceptions that occur during the base model preparation process.
        logger.exception(f"Exception occurred during {STAGE_NAME} stage: {e}")
        
        # Re-raise the exception for further handling or termination.
        raise e


