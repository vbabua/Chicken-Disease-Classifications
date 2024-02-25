# Import the centralized logger and the specific pipeline stage for data downloading.
from ChickenDiseaseClassifier import logger
from ChickenDiseaseClassifier.pipeline.stage_01_data_download import DataDownloadingTrainingPipeline
from ChickenDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

# Constant defining the name of the current pipeline stage for logging purposes.
STAGE_NAME = "Data Downloading"

try:
    # Log the beginning of the data downloading stage to keep track of the pipeline's progress.
    logger.info(f"{STAGE_NAME} stage started")

    # Initialize the data downloading pipeline stage object.
    data_download_object = DataDownloadingTrainingPipeline()
    # Execute the main method of the data downloading pipeline stage,
    # which encompasses downloading and extracting the necessary dataset.
    data_download_object.main()

    # Log the successful completion of the data downloading stage.
    logger.info(f"{STAGE_NAME} stage completed")
    
except Exception as e:
    # In case of any exceptions during the data downloading stage, re-raise the exception.
    # This ensures that any error encountered is not silently ignored and can be handled or logged appropriately.
    raise e

# Constant defining the name of the current pipeline stage for logging purposes.
STAGE_NAME = "Preparing Base Model"

try:
    # Log the beginning of the base model preparation stage to keep track of the pipeline's progress.
    logger.info(f"{STAGE_NAME} stage started")

    # Initialize the prepare base model pipeline stage object.
    prepare_base_model_object = PrepareBaseModelTrainingPipeline()
    
    # Execute the main method of the prepare base model pipeline stage.
    prepare_base_model_object .main()

    # Log the successful completion of the base model preparation stage.
    logger.info(f"{STAGE_NAME} stage completed")
    
except Exception as e:
    # In case of any exceptions during the base model preparation stage, re-raise the exception.
    # This ensures that any error encountered is not silently ignored and can be handled or logged appropriately.
    raise e