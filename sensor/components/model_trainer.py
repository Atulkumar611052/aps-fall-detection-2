from sensor.entity import artifact_entity,config_entity
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys
from typing import Optional
from xgboost import XGBClassifier


class ModelTrainer:


    def __init__(self,model_trainer_config:config_entity.ModelTrainerConfig,
                 data_transformation_artifact:artifact_entity.DataTransformationArtifact
                ):
        try:
            pass
        except Exception as e:
            raise e

    @property
    def model(self):

     def initiate_model_trainer(self,)->artifact_entity.ModelTrainerArtifact:
        try:
            pass
        except Exception as e:
            raise e