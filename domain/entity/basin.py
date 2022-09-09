from dataclasses import dataclass
from datetime import datetime


@dataclass
class Basin:
    _id: str
    created_at: datetime
    updated_at: datetime
    imported_id: int
    name: str
    area: float
    level: str
    theid: int
    code: int
    slope: float
    rivers_length: float
    rivers_slope: float
    geometry: dict
