from typing import List
from abc import ABC, abstractmethod

from domain.entity import Waterbody


class WaterbodyRepositoryInterface(ABC):
    @abstractmethod
    def find_all(self) -> List[Waterbody]:
        raise NotImplementedError

    @abstractmethod
    def insert(self, waterbody: Waterbody) -> Waterbody:
        raise NotImplementedError
