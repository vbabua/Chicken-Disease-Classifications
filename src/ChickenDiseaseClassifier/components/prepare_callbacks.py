import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from ChickenDiseaseClassifier.entities.setting_entity import CallbackConfig

class CallbackPreparer:
    def __init__(self, config: CallbackConfig):
        """
        Initialize CallbackPreparer with configuration settings for callbacks.

        Args:
            config (CallbackConfig): Configuration settings for callbacks including directories for TensorBoard logs and model checkpoint paths.
        """
        self.config = config

    @property
    def tensorboard_callback(self):
        """
        Create a TensorBoard callback configured to log events into a directory labeled with the current timestamp. This method ensures each training session has its unique logging directory.

        Returns:
            TensorBoard: A configured TensorBoard callback instance.
        """
        # Format the current time and append it to the TensorBoard logs directory to create unique subdirectories for different runs.
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tensorboard_log_dir = self.config.tensorboard_logs_directory / f"tb_logs_at_{timestamp}"
        return tf.keras.callbacks.TensorBoard(log_dir=str(tensorboard_log_dir))

    @property
    def checkpoint_callback(self):
        """
        Create a model checkpoint callback that saves the best model based on the performance on a validation set.

        Returns:
            ModelCheckpoint: A configured ModelCheckpoint callback instance.
        """
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=str(self.config.model_checkpoint_path),
            save_best_only=True  # Only save the model if it's the best on the validation set.
        )

    def get_callbacks(self):
        """
        Collect and return a list of TensorFlow callbacks including TensorBoard and model checkpointing.

        Returns:
            list: A list containing configured TensorBoard and ModelCheckpoint instances.
        """
        return [self.tensorboard_callback, self.checkpoint_callback]
