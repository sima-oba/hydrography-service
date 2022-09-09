from typing import List
from abc import ABC, abstractmethod

from domain.entity import Basin


class BasinRepositoryInterface(ABC):
    @abstractmethod
    def find_all(self) -> List[Basin]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Basin:
        raise NotImplementedError

    @abstractmethod
    def insert(self, basin: Basin) -> Basin:
        raise NotImplementedError
