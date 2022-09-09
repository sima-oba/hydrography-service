from typing import List
from abc import ABC, abstractmethod

from domain.entity import WaterSecurity


class WaterSecurityRepositoryInterface(ABC):
    @abstractmethod
    def find_all(self) -> List[WaterSecurity]:
        raise NotImplementedError

    @abstractmethod
    def insert(self, water_security: WaterSecurity) -> WaterSecurity:
        raise NotImplementedError
