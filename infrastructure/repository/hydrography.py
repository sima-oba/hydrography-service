from typing import List
from pymongo.database import Database

from domain.entity import Hydrography
from domain.repository import HydrographyRepositoryInterface
from .base import BaseRepository


class HydrographyRepository(BaseRepository, HydrographyRepositoryInterface):
    def __init__(self, db: Database):
        super().__init__(Hydrography, db['hydrography'])

    def find_by_id(self, *ids: str) -> List[Hydrography]:
        results = self.collection.find({'_id': {'$in': ids}})
        return [Hydrography(**doc) for doc in results]

    def summary(self) -> List[dict]:
        pipeline = [
            {'$project': {'name_river': True}},
            {'$sort': {'name_river': 1}}
        ]
        results = self.collection.aggregate(pipeline)
        return list(results)
