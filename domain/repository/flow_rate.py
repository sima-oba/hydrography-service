from typing import List
from abc import ABC, abstractmethod

from domain.entity import FlowRate


class FlowRateRepositoryInterface(ABC):
    @abstractmethod
    def find_all(self) -> List[FlowRate]:
        pass

    @abstractmethod
    def find_by_river(self, river_name: str) -> FlowRate:
        pass

    @abstractmethod
    def insert(self, flow_rate: FlowRate) -> FlowRate:
        pass

    @abstractmethod
    def update(self, flow_rate: FlowRate) -> FlowRate:
        pass
