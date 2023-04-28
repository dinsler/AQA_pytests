from typing import Dict, List, Union
from pymongo.collection import Collection
from bson.objectid import ObjectId


class BaseMongoDb:
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert_one(self, input_data: Dict):
        return self.collection.insert_one(input_data)

    def insert_many(self, input_data: List[Dict]):
        return self.collection.insert_many(input_data)

    def find_by_id(self, object_id: Union[str, ObjectId]):
        if isinstance(object_id, str):
            object_id = ObjectId(object_id)
        return self.collection.find_one({"_id": object_id})

    def find_all(self, sort_by_year: bool = False):
        if not sort_by_year:
            return list(self.collection.find())
        return list(self.collection.find().sort('year'))

    def delete_one_by_id(self, object_id: Union[str, ObjectId]):
        if isinstance(object_id, str):
            object_id = ObjectId(object_id)
        return self.collection.delete_one({"_id": object_id})

    def update_one(self, mov_id: Union[str, ObjectId], input_data: Dict):
        if isinstance(mov_id, str):
            mov_id = ObjectId(mov_id)
        input_data = {'$set': input_data}
        query = {'_id': mov_id}
        self.collection.update_one(query, input_data)
