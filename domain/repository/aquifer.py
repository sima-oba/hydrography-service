from typing import List
from abc import ABC, abstractmethod

from ..entity import Aquifer


class IAquiferRepository(ABC):
    @abstractmethod
    def find_by_imported_id(self, imported_id: str) -> Aquifer:
        pass

    @abstractmethod
    def summary(self) -> List[dict]:
        pass

    @abstractmethod
    def find_by_ids(self, ids: List[str]) -> List[Aquifer]:
        pass

    @abstractmethod
    def add(self, aquifer: Aquifer) -> Aquifer:
        pass
