from pymongo.database import Database

from domain.entity import WaterAvailability
from domain.repository import WaterAvailabilityRepositoryInterface
from .base import BaseRepository


class WaterAvailabilityRepository(
    BaseRepository, WaterAvailabilityRepositoryInterface
):
    def __init__(self, db: Database):
        super().__init__(WaterAvailability, db['water_availability'])
