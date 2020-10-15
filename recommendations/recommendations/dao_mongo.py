from pymongo import MongoClient
from pymongo.collection import Collection
from config import MONGODB_URI, MONGODB_DATABASE


class MongoDB:
    def __init__(self) -> None:
        client = MongoClient(MONGODB_URI)
        self.database = client[MONGODB_DATABASE]

    def products(self) -> Collection:
        return self.database["products"]

    def recommendations(self) -> Collection:
        return self.database["recommendations"]
