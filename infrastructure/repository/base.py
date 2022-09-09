from dataclasses import dataclass, asdict, is_dataclass
from pymongo.database import Collection

from domain.entity.base import Base


class BaseRepository:
    def __init__(self, cls: dataclass, collection: Collection):
        if not is_dataclass(cls):
            raise ValueError(f'{cls} must be a dataclass')
        self._cls = cls
        self.collection = collection

    def find_all(self):
        return [self._cls(**doc) for doc in self.collection.find()]

    def find_by_id(self, id: str):
        result = self.collection.find_one({'_id': id})
        return self._cls(**result) if result else None

    def insert(self, obj: dataclass):
        result = self.collection.insert_one(asdict(obj))
        obj._id = result.inserted_id
        return obj

    def update(self, obj: Base):
        result = self.collection.update_one(
            {'_id': obj._id},
            {'$set': obj.asdict()}
        )
        return result.modified_count > 0
