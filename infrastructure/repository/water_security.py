from pymongo.database import Database

from domain.entity import WaterSecurity
from domain.repository import WaterSecurityRepositoryInterface
from .base import BaseRepository


class WaterSecurityRepository(
    BaseRepository, WaterSecurityRepositoryInterface
):
    def __init__(self, db: Database):
        super().__init__(WaterSecurity, db['water_security'])
