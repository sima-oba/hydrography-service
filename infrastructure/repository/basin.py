from pymongo.database import Database

from domain.entity import Basin
from domain.repository import BasinRepositoryInterface
from .base import BaseRepository


class BasinRepository(BaseRepository, BasinRepositoryInterface):
    def __init__(self, db: Database):
        super().__init__(Basin, db['basin'])
