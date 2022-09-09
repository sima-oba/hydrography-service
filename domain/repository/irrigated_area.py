from abc import ABC, abstractmethod
from typing import List, Optional

from ..entity import IrrigatedArea


class IIrrigatedAreaRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[IrrigatedArea]:
        pass

    @abstractmethod
    def find_by_imported_id(self, imported_id: str) -> Optional[IrrigatedArea]:
        pass

    @abstractmethod
    def add(self, irrigated_area: IrrigatedArea) -> IrrigatedArea:
        pass
