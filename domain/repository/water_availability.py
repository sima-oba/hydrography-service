from abc import ABC, abstractmethod

from domain.entity import WaterAvailability


class WaterAvailabilityRepositoryInterface(ABC):
    @abstractmethod
    def find_all() -> list:
        raise NotImplementedError

    @abstractmethod
    def insert(water_availability: WaterAvailability) -> WaterAvailability:
        raise NotImplementedError
