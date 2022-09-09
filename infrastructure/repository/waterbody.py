from pymongo.database import Database

from domain.entity import Waterbody
from domain.repository import WaterbodyRepositoryInterface
from .base import BaseRepository


class WaterBodyRepository(BaseRepository, WaterbodyRepositoryInterface):
    def __init__(self, db: Database):
        super().__init__(Waterbody, db['waterbody'])
