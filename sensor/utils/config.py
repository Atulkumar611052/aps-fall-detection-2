import pymongo
import pandas as pd 
import json
from dataclasses import dataclass
# Provide the mongodb localhost url to connect python to mongodb.

@dataclass
class Environmentvariable:
    mongo_db_url:str = os.getenv("MONGO_DB_UR")
    aws_access_key_id:str=os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_secret_key_id:str=os.getenv("AWS_SECRET_ACCESS_KEY_ID")


env_var = Environmentvariable()
client=pymongo.MongoClient(env_var.mongo_db_url)