from dataclasses import dataclass
from .base import Base


@dataclass
class Pivot(Base):
    area: float
    geometry: dict
