from dataclasses import dataclass
from datetime import datetime


@dataclass
class Hydrography:
    _id: str
    created_at: datetime
    updated_at: datetime
    co_river: str
    id_river: int
    name_river: str
    river_length: float
    basin_distance: float
    ds_version: str
    geometry: dict
