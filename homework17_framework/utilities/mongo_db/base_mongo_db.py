class BaseMongoDbRepository:
    def __init__(self, collection):
        self.collection = collection

    def _insert_one(self, input_data):
        return self.collection.insert_one(input_data)

    def _insert_many(self, input_data):
        return self.collection.insert_many(input_data)

    def _find_one(self, input_data):
        return self.collection.find_one(input_data)

    def _find_all(self, input_data):
        for mov in self.collection.find(input_data):
            return mov





