from pymongo import MongoClient

mongo_uri = ""

client = MongoClient(mongo_uri)
mongo_database = client['SlimeyBOT']
mongo_collection = mongo_database['Main_db']

data = input("Enter the data here:")
data_to_insert = {"key": data}
mongo_collection.insert_one(data_to_insert)

print("Inserted data!")