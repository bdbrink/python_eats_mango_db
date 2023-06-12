from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.mydbname

people = db.people

people.insert_one({"name": "Josh", "age": 30})

for person in people.find():
    print(person)