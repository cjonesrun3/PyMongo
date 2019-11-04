from bson import BSON
from bson import decode_all
from pymongo import MongoClient

try:
    client = MongoClient('mongodb://user:password@server:27017/database',
                         ssl=True,
                         ssl_certfile='client.pem',
                         ssl_ca_certs='ca.pem'
                         )
    db = client.database  # DATABASE
    retrieve_request = db.Collection  # COLLECTION


    with open('Path to your backup.bson', 'rb') as f:
        retrieve_request.insert(decode_all(f.read()))

    client.close()
except Exception as e:
    print(str(e))