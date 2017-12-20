### wrapper method for MongoDB
from pymongo import MongoClient
import datetime
import bson
from db import DB


class PyMongoDB(DB):
    # singleton db oject (this should be pooled to avoid multiple db connections)
    db = None
    def __init__(self, host=None, port=None, db_name=None):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.doc = {} # document properties
        self._id = None
        super().__init__()

    # connect to db
    def _connect(self):
        if not PyMongoDB.db:
            print("connecting to pymongo\n")
            client = MongoClient(self.host or 'localhost', self.port or 27017)
            PyMongoDB.db = client[db_name] if self.db_name else client['test']
        # self.collection_name is defined by child class
        self.collection = PyMongoDB.db[self.collection_name]

    # Save new or changed document
    def save(self, doc = {}):
        if doc: # override current document
            self.doc = doc
        self.doc['updated_at'] = datetime.datetime.utcnow()
        # if document already exists update else insert
        if 'created_at' not in self.doc:
            self.doc['created_at'] = datetime.datetime.utcnow()
            self._save()
        else:
            self._update()

    # Save to DB
    def _save(self):
        self._id = self.collection.insert_one(self.doc).inserted_id

    # Update docuement in DB
    def _update(self):
        pass

    def find_one(self, query):
        return self.collection.find_one(query)

    def find(self, query):
        return self.collection.find(query) 

    def delete(self, query={}):
        self.collection.delete_one(query)
