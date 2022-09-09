from pymongo.database import Database

from domain.entity import FlowRate
from domain.repository import FlowRateRepositoryInterface
from .base import BaseRepository


class FlowRateRepository(BaseRepository, FlowRateRepositoryInterface):
    def __init__(self, db: Database):
        super().__init__(FlowRate, db['flow_rate'])

    def find_by_river(self, river_name: str) -> FlowRate:
        doc = self.collection.find_one({'river': river_name})
        return FlowRate(**doc) if doc else None
