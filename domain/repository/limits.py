from typing import List
from abc import ABC, abstractmethod

from domain.entity import Limit_L1, Limit_L2, Limit_L4, Limit_L5


class LimitsRepositoryInterface(ABC):
    @abstractmethod
    def find_limits_L1(self) -> List[Limit_L1]:
        raise NotImplementedError

    @abstractmethod
    def find_limits_L2(self) -> List[Limit_L2]:
        raise NotImplementedError

    @abstractmethod
    def find_limits_L4(self) -> List[Limit_L4]:
        raise NotImplementedError

    @abstractmethod
    def find_limits_L5(self) -> List[Limit_L5]:
        raise NotImplementedError

    @abstractmethod
    def insert_limit_L1(self, limit: Limit_L1) -> Limit_L1:
        raise NotImplementedError

    @abstractmethod
    def insert_limit_L2(self, limit: Limit_L2) -> Limit_L2:
        raise NotImplementedError

    @abstractmethod
    def insert_limit_L4(self, limit: Limit_L4) -> Limit_L4:
        raise NotImplementedError

    @abstractmethod
    def insert_limit_L5(self, limit: Limit_L5) -> Limit_L5:
        raise NotImplementedError
