# Import the centralized logger and the specific pipeline stage for data downloading.
from ChickenDiseaseClassifier import logger
from ChickenDiseaseClassifier.pipeline.stage_01_data_download import DataDownloadingTrainingPipeline

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
