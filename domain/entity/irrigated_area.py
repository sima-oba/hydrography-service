from dataclasses import dataclass

from .base import Base


@dataclass
class IrrigatedArea(Base):
    imported_id: str
    length: float
    area: float
    geometry: dict
