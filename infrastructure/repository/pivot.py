from pymongo.database import Database

from domain.entity import Pivot
from domain.repository import PivotRepositoryInterface
from .base import BaseRepository


class PivotRepository(BaseRepository, PivotRepositoryInterface):
    def __init__(self, db: Database):
        super().__init__(Pivot, db['pivots'])
