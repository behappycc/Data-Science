from pymongo import MongoClient
import datetime

#sudo service mongod start
#sudo service mongod stop

client = MongoClient('localhost', 27017)
db = client['ptt']

post = {"author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()}

collection = db['posts']

#remove all documents from a collection
result = collection.delete_many({})
post_id = collection.insert_one(post).inserted_id
print collection.find_one({"author": "Mike"})
print collection.find_one({"author": "hub"})

new_posts = [{"author": "Mike",
    "text": "Another post!",
    "tags": ["bulk", "insert"],
    "date": datetime.datetime(2009, 11, 12, 11, 14)},
    {"author": "Eliot",
    "title": "MongoDB is fun",
    "text": "and pretty easy too!",
    "date": datetime.datetime(2009, 11, 10, 10, 45)}]
result = collection.insert_many(new_posts)
print result.inserted_ids

for post in collection.find({"author": "Mike"}):
    print post

print collection.count()