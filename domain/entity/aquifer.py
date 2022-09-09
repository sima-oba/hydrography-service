from dataclasses import dataclass

from .base import Base


@dataclass
class Aquifer(Base):
    imported_id: str
    type: str
    name: str
    area: float
    length: float
    geometry: dict
