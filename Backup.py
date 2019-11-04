from pymongo import MongoClient
from bson import BSON


try:
    client = MongoClient('mongodb://user:password@server:27017/database',
                         ssl=True,
                         ssl_certfile='ssl cert',
                         ssl_ca_certs='ca.pem')
    db = client.database  # DATABASE NAME
    retrieve_request = db.Collection  # COLLECTION NAME

    inquiry_result = retrieve_request.find({})  # Returns all data

    with open('path to backup location\\backup.bson', 'wb+') as f:
        for doc in inquiry_result:
            f.write(BSON.encode(doc))

    client.close()
except Exception as e:
    print(str(e))