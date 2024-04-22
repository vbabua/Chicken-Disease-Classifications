import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
        self.model = None
        self.train_generator = None
        self.valid_generator = None

    def load_base_model(self):
        self.model = tf.keras.models.load_model(self.config.updated_model_path)

    def prepare_data_generators(self):
        datagenerator_kwargs = {
            "rescale": 1./255,
            "validation_split": 0.20
        }

        dataflow_kwargs = {
            "target_size": self.config.image_size[:-1],
            "batch_size": self.config.batch_size,
            "interpolation": "bilinear"
        }

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=str(self.config.training_data_dir),
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.use_data_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=str(self.config.training_data_dir),
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    def train_model(self, callback_list: list):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.num_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list
        )

        self.save_model(self.config.trained_model_path, self.model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)