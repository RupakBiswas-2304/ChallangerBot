from pymongo import MongoClient
CONNECTION_STRING = "mongodb+srv://hacker:flag{404}@cluster0.abtw8.mongodb.net/?retryWrites=true&w=majority"
import datetime

def create_challange(req):
    dbclient = MongoClient(CONNECTION_STRING)
    db = dbclient['CSec']
    collection = db['challenge']
    
    now = datetime.datetime.now()
    challange = req
    collection.insert_one(challange)
    print("Challange created!")
        
if __name__ == "__main__":
    now = datetime.datetime.now()
    req = {
        "created-at": now,
            "title": "February Challange",
            "status" : "active",
            "description": "This is a description",
            "files" : "https://www.w3schools.com/python/python_mongodb_insert.asp",
            "problems" : {
                "p1" : {
                    "title" : "Problem 1",
                    "description" : "This is a description",
                    "score" : 200,
                    "flag" : "njack{discord-bot-challange}",
                    "top-hackers" : [],
                    "created-at" : now
                },
                "p2" : {
                    "title" : "Problem 2",
                    "description" : "This is a description",
                    "score" : 200,
                    "flag" : "njack{discord-bot-challange2}",
                    "top-hackers" : [],
                    "created-at" : now
                }
            }
    }
    create_challange(req)