# connection to mongodb

import pymongo
import os
try:
    mongo = pymongo.MongoClient(
            host = "127.0.0.1",
            port = 12017,
            serverSelectionTimeoutMS = 1000
            )
    db = mongo.students
    print(f"returned {db.status_code} success")
    info = mongo.server_info()
except Exception as e:
    print(e)
