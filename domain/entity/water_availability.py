from dataclasses import dataclass
from typing import Optional

from .base import Base


@dataclass
class WaterAvailability(Base):
    OBJECTID: int
    cotrecho: int
    cocursodag: str
    cobacia: str
    nuareacont: float
    nuareamont: float
    noriocomp: Optional[str]
    dedominial: str
    dsversao: str
    QmltEsp: float
    Qmltinc: float
    Qmlt: float
    Q95ESP: float
    Q95inc: float
    Q95NAT: float
    COBAR: float
    COLAGO: float
    COOPERA: float
    DSOPERA: Optional[str]
    QDEFLU: float
    QLAGO: float
    NORES: Optional[str]
    saz: float
    DQ95Jan: float
    DQ95Fev: float
    DQ95Mar: float
    DQ95Abr: float
    DQ95Mai: float
    DQ95Jun: float
    DQ95Jul: float
    DQ95Ago: float
    DQ95Set: float
    DQ95Out: float
    DQ95Nov: float
    DQ95Dez: float
    DQano: float
    Fronteira: float
    RelAplicad: float
    FonteQmlt: str
    FONTEQ95: str
    FonteQanua: str
    FonteQsazo: Optional[str]
    FonteQres: Optional[str]
    dsversaoQ: str
    Shape_Leng: float
    geometry: dict
