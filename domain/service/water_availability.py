from domain.entity.water_availability import WaterAvailability
from domain.repository import WaterAvailabilityRepositoryInterface


class WaterAvailabilityService:
    def __init__(self, repo: WaterAvailabilityRepositoryInterface):
        self._repo = repo

    def find_all(self) -> list:
        return self._repo.find_all()

    def insert(self, data: dict) -> WaterAvailability:
        return self._repo.insert(WaterAvailability.new(data))
