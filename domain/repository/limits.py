from typing import List
from abc import ABC, abstractmethod

from domain.entity import Limit_L1, Limit_L2


class LimitsRepositoryInterface(ABC):
    @abstractmethod
    def find_limits_L1(self) -> List[Limit_L1]:
        raise NotImplementedError

    @abstractmethod
    def find_limits_L2(self) -> List[Limit_L2]:
        raise NotImplementedError

    @abstractmethod
    def insert_limit_L1(self, limit: Limit_L1) -> Limit_L1:
        raise NotImplementedError

    @abstractmethod
    def insert_limit_L2(self, limit: Limit_L2) -> Limit_L2:
        raise NotImplementedError
