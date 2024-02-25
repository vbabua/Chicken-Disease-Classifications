import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from ChickenDiseaseClassifier.entities.setting_entity import BaseModelConfig

class BaseModelPreparation:
    def __init__(self, config: BaseModelConfig):
        self.config = config
        self.base_model = None
        self.full_model = None

    def load_and_prepare_base_model(self):
        # Load the VGG16 model as the base model with configurations
        self.base_model = tf.keras.applications.VGG16(
            include_top=self.config.include_pretrained_weights,
            weights=self.config.pretrained_weights,
            input_shape=self.config.image_dimensions
        )
        # Save the loaded base model
        self._save_model(self.config.initial_model_path, self.base_model)

    def _customize_model(self, model: tf.keras.Model, output_classes: int, learning_rate: float) -> tf.keras.Model:
        # Freeze all layers in the base model to prevent them from being updated during training
        model.trainable = False

        # Add custom layers on top of the base model
        flatten_layer = tf.keras.layers.Flatten()(model.output)
        prediction_layer = tf.keras.layers.Dense(units=output_classes, activation="softmax")(flatten_layer)

        # Create a new model combining the base and custom layers
        full_model = tf.keras.models.Model(inputs=model.input, outputs=prediction_layer)
        # Compile the model with the specified optimizer, loss function, and metrics
        full_model.compile(optimizer=tf.keras.optimizers.SGD(lr=learning_rate), loss='categorical_crossentropy', metrics=['accuracy'])

        # Print a summary of the model to the console
        full_model.summary()
        return full_model

    def customize_and_save_model(self):
        # Customize the base model and save the modified version
        self.full_model = self._customize_model(
            model=self.base_model,
            output_classes=self.config.output_classes,
            learning_rate=self.config.learning_rate
        )
        self._save_model(self.config.modified_model_path, self.full_model)

    @staticmethod
    def _save_model(model_path: Path, model: tf.keras.Model):
        # Save the given model to the specified path
        model.save(model_path)