import pymongo

MOVIES_DB = 'movies'


class MongoSession:
    __myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    @staticmethod
    def get_my_client():
        return MongoSession.__myclient


class Movies(MongoSession):
    __movies_db = MongoSession.get_my_client()[MOVIES_DB]

    @staticmethod
    def get_movies_db():
        return Movies.__movies_db
