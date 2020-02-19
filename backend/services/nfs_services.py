from pymongo import MongoClient

class NfsServices:
    def __init__(self):
        self.client = MongoClient(port=27017)
        self.db = self.client.business

    def GetAllNfs(self):
        return list(self.db.collection.find({}))

    def GetById(self, guid):
        return self.db.nfs.find_one({'id': guid})

    def GetSingle(self, id):
        return self.db.nfs.find_one({'id': id})

    def Add(self, obj):
        return self.db.nfs.insert_one(obj)
    
    def GetValue(self):
        return self.db.settings.find_one()['value']
