from hw23_mongo_db.mongo_db.db_interface import BaseMongoDb
from mongo_db.db_collections import ActionMovies

db = BaseMongoDb(ActionMovies.get_collection())


if __name__ == '__main__':
    # db.insert_one({"name": "Avengers:Endgame", "year": 2019})
    # db.insert_many([{"name": "The Bourne Ultimatum", "year": 2007}, {"name": "Gladiator", "year": 2000},
    #                 {"name": "The Dark Knight", "year": 2008}])
    print(db.find_all(True))
    print(db.find_by_id('64458a549a5d55a78845f1cb'))
    # db.delete_one_by_id('64458b72084c377117a47337')
    db.update_one('64458a549a5d55a78845f1cd', {"duration": 127})
    print(db.find_by_id('64458a549a5d55a78845f1cd'))
