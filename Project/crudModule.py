from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username):
        # Connection Variables
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'localhost'
        PORT = 27017
        DB = 'AAC'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.collection.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

    # Method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            results = self.collection.find(query)  # data should be dictionary
            return list(results)
        else:
            raise Exception("Nothing to read, because query parameter is empty")
            return []

    # Method to implement the U in CRUD.
    def update(self, query, updated_data, many=False):
        if query is not None and updated_data is not None:
            if many:
                results = self.collection.update_many(query, updated_data)
            else:
                results = self.collection.update_one(query, updated_data)
            return results.modified_count
        else:
            raise Exception("Please provide query and update data")

    # Method to implement the D in CRUD.
    def delete(self, query, many=False):
        if query is not None:
            if many:
                results = self.collection.delete_many(query)
            else:
                results = self.collection.delete_one(query)
            return results.deleted_count
        else:
            raise Exception("Please provide query and update data")