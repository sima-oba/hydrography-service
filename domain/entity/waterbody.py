from dataclasses import dataclass
from typing import Optional

from .base import Base


@dataclass
class Waterbody(Base):
    name: str
    type: Optional[str]
    geometry: dict
