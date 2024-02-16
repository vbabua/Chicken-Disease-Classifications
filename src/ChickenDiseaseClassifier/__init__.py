# Importing necessary libraries
import os
import sys
import logging

# Define a string that specifies the format of the log messages
logging_format = "[%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(message)s]"

# Specify the directory where the log files should be stored.
log_directory = "logs"

# Specify the file name for the log file.
log_filename = "application_logs.log"

# Construct full path for the log file.
log_filepath = os.path.join(log_directory, log_filename)

# Create a log directory if it doesn't exist
os.makedirs(log_directory, exist_ok = True)

# Configure the logging system
logging.basicConfig(
    level = logging.INFO, 
    format = logging_format,
    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
        ]
        )

logger = logging.getLogger("chickenDiseaseClassifierLogger")