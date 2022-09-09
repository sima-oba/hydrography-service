from dataclasses import dataclass
from datetime import datetime


@dataclass
class Contrib:
    _id: str
    created_at: datetime
    updated_at: datetime
    nunivotto5: str
    geometry: dict
