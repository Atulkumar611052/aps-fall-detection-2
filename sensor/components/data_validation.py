from sensor.entity import artifact_entity,config_entity
from sensor.logger import logging
from sensor.exception import SensorException
import os
from scipy.stats import ks_2samp
import pandas as pd 
from typing import Optional
class DataValidation:


     def __init__(self,data_validation_config:config_entity.DataValidationConfig):
        try:
            logging.info(f"{'>>'*20} data validation{'<<'*20}")
            self.data_validation_config=data_validation_config
            self.validation_error=dict()
        except Exception as e:
            raise SensorException (e,sys)

     def is_required_columns_exist(self,)->bool:...

     def drop_missing_valur_columns(self,threshold=0.3)-> DataFrame:
        """
        This function will drop the columns which contains missing values more then specified threshold

        df: except the pandas dataframe
        threshold:percentage criteria to drop a column
        =========================================================================================================
        return pandas DataFrame if atleast single column is available after missing column drop else NONE

        """
        try:
            threshold =self.data_validation_config.missing_threshold             
            null_report=df.isnull().sum()/df.shape[0]           
            # Selecting column name which contain null value
            drop_columns_name=null_report[null_report>threshold].index            
            self.validation_error["dropped_columnscolumns"]=drop_column_names
            df.drop(list(drop_columns_name),axis=1,inplace=True)

            # return none no columns left
            if len(df.columns)==0:
                return None
            return df
        except Exception as e:
            raise SensorException (e,sys)

     def is_required_columns_exist(self,base_df:pd.DataFrame,current_df:pd.DataFrame)->bool:
        try:
            base_columns=base_df.column
            current_columns=current_df.columns

            missing_columns=[]
            for base_column in base_columns:
                if base_column not in current_columns:
                    missing_columns.append(base_columns)

            if len(missing_columns)>0:
                self.validation_error["missing_columns"]=missing_columns
                return False
            return True



        except Exception as e:
            raise e





     def initiate_data_validation(self)->
