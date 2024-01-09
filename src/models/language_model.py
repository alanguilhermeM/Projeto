from database.db import db
from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict):
        super().__init__(data)

    def to_dict(self):
        dict = {"name": self.data["name"], "acronym": self.data["acronym"]}
        return dict

    @classmethod
    def list_dicts(cls, query={}):
        data = cls._collection.find(query)

        result_list = [cls(entry).to_dict() for entry in data]
        return result_list
