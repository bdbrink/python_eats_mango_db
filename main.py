from pymongo import MongoClient

# build client from local DB
client = MongoClient("localhost", 27017)
# use name defined for local db
db = client.mydbname
# field in the DB
people = db.people

people.insert_one({"name": "Josh", "age": 30})

for person in people.find():
    print(person)
