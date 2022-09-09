from pymongo.database import Database

from domain.entity import Contrib
from domain.repository import ContribRepositoryInterface
from .base import BaseRepository


class ContribRepository(BaseRepository, ContribRepositoryInterface):
    def __init__(self, db: Database):
        super().__init__(Contrib, db['contrib'])
