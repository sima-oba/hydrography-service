from typing import List
from abc import ABC, abstractmethod

from domain.entity import Contrib


class ContribRepositoryInterface(ABC):
    @abstractmethod
    def find_all(self) -> List[Contrib]:
        raise NotImplementedError

    @abstractmethod
    def insert(self, contrib: Contrib) -> Contrib:
        raise NotImplementedError
