from sensor.entity import artifact_entity,config_entity
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys
from typing import Optional
from xgboost import XGBClassifier
from sensor import utils
from sklearn.metrics import f1_score

class ModelTrainer:


    def __init__(self,model_trainer_config:config_entity.ModelTrainerConfig,
                 data_transformation_artifact:artifact_entity.DataTransformationArtifact
                ):
        try:
            pass
        except Exception as e:
            raise e

    
    def train_model(self,x,y):
        xgb_clf=XGBClassifier()
        xgb_clf.fit(x,y)
        return xgb_clf

    def initiate_model_trainer(self,)->artifact_entity.ModelTrainerArtifact:
        try:
            train_arr=utils.load_numpy_array_data(file_path=sself.data_transformation_artifact.transformed_train_path)
            test_arr=utils.load_numpy_array_data(file_path=sself.data_transformation_artifact.transformed_test_path)

            x_train,y_train=train_arr[:,:-1],train_arr[:,-1]
            x_test,y_test=test_arr[:,:-1],test_arr[:,-1]


            model=train_model(x=x_train,y=y_train)

            yhat_train=model.predict(x_train)
            f1_train_score=f1_score(y_true=y_train,y_pred=yhat_train)

            yhat_test=model.predict(x_test)
            f1_test_score=f1_score(y_true=y_test,y_pred=yhat_testy)
            
            # check for overfitting or underfitting or expected score
            
        except Exception as e:
            raise e