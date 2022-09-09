import json
from typing import List
from pymongo.database import Database
from gridfs import GridFS

from domain.entity import Limit_L1, Limit_L2
from domain.repository import LimitsRepositoryInterface
from .base import BaseRepository


class _Limit_L1:
    def __init__(self, db: Database):
        self._limits = db['limit_lvl_1']
        self._fs = GridFS(db, collection='geometry')

    def find_all(self) -> List[Limit_L1]:
        docs = self._limits.find()
        limits = []
        for item in docs:
            geometry_id = item.pop('geometry_id')
            geometry_json = self._fs.get(geometry_id).read()
            item['geometry'] = json.loads(geometry_json)
            limit = Limit_L1(**item)
            limits.append(limit)
        return limits

    def insert(self, limit: Limit_L1) -> Limit_L1:
        doc = limit.asdict()
        geometry = doc.pop('geometry')
        geometry_json = json.dumps(geometry).encode('utf8')
        geometry_id = self._fs.put(geometry_json)
        doc['geometry_id'] = geometry_id
        limit._id = self._limits.insert_one(doc).inserted_id
        return limit


class _Limit_L2(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(Limit_L2, db['limit_lvl_2'])


class LimitsRepository(LimitsRepositoryInterface):
    def __init__(self, db: Database):
        self._limit_L1 = _Limit_L1(db)
        self._limit_L2 = _Limit_L2(db)

    def find_limits_L1(self) -> List[Limit_L1]:
        return self._limit_L1.find_all()

    def find_limits_L2(self) -> List[Limit_L2]:
        return self._limit_L2.find_all()

    def insert_limit_L1(self, limit: Limit_L1) -> Limit_L1:
        return self._limit_L1.insert(limit)

    def insert_limit_L2(self, limit: Limit_L2) -> Limit_L2:
        return self._limit_L2.insert(limit)
