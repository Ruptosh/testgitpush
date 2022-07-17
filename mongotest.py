import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:ineuron12@cluster0.coepdpz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "ruptosh",
    "email" : "rup@gmail",
    "surname" : "chatterjee"
}

d = {
    "name" : "ruptosh",
    "email" : "rup@gmail",
    "surname" : "chatterjee"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)