from typing import List
from abc import ABC, abstractmethod

from domain.entity import Hydrography


class HydrographyRepositoryInterface(ABC):
    @abstractmethod
    def find_all(self) -> List[Hydrography]:
        pass

    @abstractmethod
    def summary(self) -> List[dict]:
        pass

    @abstractmethod
    def find_by_id(self, *ids: str) -> Hydrography:
        pass

    @abstractmethod
    def insert(self, hydrography: Hydrography) -> Hydrography:
        pass
