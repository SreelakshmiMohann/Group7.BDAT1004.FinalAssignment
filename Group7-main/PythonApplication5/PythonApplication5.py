import pymongo
import dns
import csv
import pandas as pd
import json
import sys, getopt, pprint

client = pymongo.MongoClient("mongodb+srv://ozan:kaya@cluster0.2v7o6.mongodb.net/<dbname>?retryWrites=true&w=majority")
db=client["cruise_db"]
col = db["cruise_records"]

#print(client.list_database_names())


csvlocation = "C:\\Users\\ozank\\source\\repos\\PythonApplication5\\data\\cruise.csv"

df = pd.read_csv(csvlocation,encoding = 'ISO-8859-1')              # loading csv file
df.to_json('yourjson.json')                               # saving to json file
jdf = open('yourjson.json').read()                        # loading the json file 
data = json.loads(jdf)                                    # reading json file 

if isinstance(data, list): 
    col.insert_many(data)   
else: 
    col.insert_one(data) 

