from ChickenDiseaseClassifier.config.settings import ConfigLoader
from ChickenDiseaseClassifier.components.data_downloader import DatasetDownloader
from ChickenDiseaseClassifier import logger

# Define a constant for the stage name to improve readability and maintainability.
STAGE_NAME = "Data Downloading"

class DataDownloadingTrainingPipeline:
    """
    Represents the pipeline stage for downloading and extracting the dataset
    necessary for training the ChickenDiseaseClassifier model.
    """
    def __init__(self):
        """
        Initializes the DataDownloadingTrainingPipeline object.
        """
        pass  # Currently, no initialization is required.
    
    def main(self):
        """
        Main method to execute the data downloading and extraction process.
        """
        # Load configuration settings for the data downloading stage.
        loader = ConfigLoader()
        ingestion_settings = loader.fetch_ingestion_settings()

        # Initialize the DatasetDownloader with the fetched settings.
        downloader = DatasetDownloader(settings=ingestion_settings)

        # Perform the dataset downloading and extraction.
        downloader.download_dataset()
        downloader.unzip_dataset()

# Entry point for the script.
if __name__ == "__main__":
    try:
        # Log the start of the data downloading stage.
        logger.info(f"{STAGE_NAME} stage started")

        # Create an instance of the pipeline and execute the main process.
        pipeline = DataDownloadingTrainingPipeline()
        pipeline.main()

        # Log the completion of the data downloading stage.
        logger.info(f"{STAGE_NAME} stage completed")
    
    except Exception as e:
        # Log any exceptions that occur during the data downloading process.
        logger.error(f"Error occurred during the {STAGE_NAME} stage: {e}")
        
        # Re-raise the exception for further handling or termination.
        raise e  
