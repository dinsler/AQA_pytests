from homework17_framework.session_mongo_db import MongoSession


class Movies(MongoSession):
    __movies_database = MongoSession.get_my_client()["movies"]

    @staticmethod
    def get_movies_database():
        return Movies.__movies_database
    