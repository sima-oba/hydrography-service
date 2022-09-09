from dataclasses import dataclass
from typing import Optional

from .base import Base


@dataclass
class WaterSecurity(Base):
    brazil: str
    co_basin: str
    economical: Optional[str]
    ecosystem: Optional[str]
    human: Optional[str]
    resilience: str
    area: float
    length: float
    geometry: dict
