from typing import List
from abc import ABC, abstractmethod

from domain.entity import Pivot


class PivotRepositoryInterface(ABC):
    @abstractmethod
    def find_all(self) -> List[Pivot]:
        raise NotImplementedError

    @abstractmethod
    def insert(self, contrib: Pivot) -> Pivot:
        raise NotImplementedError
