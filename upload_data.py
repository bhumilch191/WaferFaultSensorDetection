from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# uniform resource identifier
uri = "mongodb+srv://bhumilchauhan:bhumil1914@cluster0.sgxl5qk.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Create database name and collection name
DATABASE_NAME = 'Project_database'
COLLECTION_NAME = 'waferfault'


# read data as dataframe
df = pd.read_csv("D:\Sources(MSD)\Models\Waffer-Fault-Sensor-Detection\notebook\wafer_Dataset.csv")
df = df.drop("Unnamed: 0", axis=1)

# convert data into json
json_record = list(json.loads(df.T.to_json()).values())

# now dump the data into database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
