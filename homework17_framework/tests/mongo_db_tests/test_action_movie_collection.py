from homework17_framework.utilities.mongo_db.base_mongo_db import BaseMongoDbRepository


def test_insert_one_and_delete_one(get_action_movies_col, env):
    action_movies_collection = get_action_movies_col
    BaseMongoDbRepository(action_movies_collection)._insert_one(env.action_movie_dict)
    print(action_movies_collection)
    BaseMongoDbRepository(action_movies_collection)._insert_many(env.action_movie_list)
    print(action_movies_collection)



    # BaseMongoDbRepository(alternate_col)._find_by({})
    # print('------------------')
    # BaseMongoDbRepository(alternate_col)._insert_many(env.face_list_of_dicts)
    # BaseMongoDbRepository(alternate_col)._find_by({})
    # print('------------------')