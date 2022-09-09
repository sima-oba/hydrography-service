from dataclasses import dataclass

from .base import Base


@dataclass
class Limit_L1(Base):
    wts_cd_pfafstetterbasin: str
    wts_cd_pfafstetterbasincodelevel: int
    wts_gm_area: float
    wts_pk: float
    geometry: dict


@dataclass
class Limit_L2(Base):
    level: str
    geometry: dict
