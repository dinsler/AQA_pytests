import pymongo


class MongoSession:
    __myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    @staticmethod
    def get_my_client():
        return MongoSession.__myclient
