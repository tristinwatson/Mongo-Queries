#Python AAC File
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collections in MongoDB"""
    
    def __init__(self):
        #self.client = MongoClient('mongodb://localhost:30224')
        self.client = MongoClient('mongodb://%s:%s@localhost:30224' % ('aacuser', 'password1'))
        self.database = self.client['project']
    
    # C method
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
    # R method
    def read(self, data):
        if data is not None:
            cursor = self.database.animals.find(data, {'_id' :False})
            return cursor
        else:
            raise Exception("Nothing to read, because data parameter is empty")
        
    # U method
    def update(self, data, change):
        if data is not None:
            result = self.database.animals.updateOne(data, change, {'_id' :False})
            return result
        else:
            raise Exception("Nothing to update, because data parameter is empty")
        
    # D method
    def delete(self, data):
        if data is not None:
            result = self.database.animals.deleteOne(data, {'_id' :False})
            return result
        else:
            raise Exception("Nothing to delete, because data parameter is empty")