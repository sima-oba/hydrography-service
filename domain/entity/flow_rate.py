from dataclasses import dataclass
from typing import Optional

from .base import Base


@dataclass
class FlowRate(Base):
    co_basin: str
    domain: str
    river: str
    q90: Optional[str]
    qmld: Optional[str]
    geometry: dict
