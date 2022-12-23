from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os
from sensor.entity.config_entity import DataIngestionConfig
from sensor.components import data_ingestion
from sensor.components.data_validation import DataValidation
from sensor.components.model_trainer import ModelTrainer

print(__name__)
if __name__=="__main__":
     try:
          training_pipeline_config = config_entity.TrainingPipelineConfig()
          data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())
          # Dat ingestion
          data_ingestion=DataIngestion(data_ingestion_config=data_ingestion_config)
          data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
          # Data validation
          data_validation_config=config.entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
          data_validation=DataValidation(data_validation_config=data_validation_config,
                          data_ingestion_artifact=data_ingestion_artifact)

          data_validation_artifact=data_validation.initiate_data_validation()
          
          # Data transformation
          data_transformation_config=config_entity.data_transformation_config(training_pipeline_config=training_pipeline_config),
          data_transformation=DataTransformation(data_transformation_config=data_transformation_config,
          data_ingestion_artifact=data_ingestion_artifact)
          data_transformation_artifact = data_transformation.initiate_data_transformation()

          # Model trainer
          model_trainer_config=config_entity.ModelTrainer(training_pipeline_config=training_pipeline_config)
          model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
          model_trainer_artifact = model_trainer.initiate_model_trainer()

     except Exception as e:
          print(e)
     
