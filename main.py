from sensor.logger import logging
from sensor.exception import SensorException
import sys,os

def test_test_logger_exceptiom():
     try:
          result = 3/0  
          print(result)   
     except Exception as e:
          raise SensorException (e,sys)


if __name__=="__main__":
     try:
          test_test_logger_exceptiom()
     except Exception as e:
          print(e)
     
