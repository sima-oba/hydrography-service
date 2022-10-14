from .aquifer import AquiferConsumer
from .basin import BasinConsumer
from .flow_rate import FlowRateConsumer
from .hydrography import HydrographyConsumer
from .irrigated_area import IrrigatedAreaConsumer
from .limits import (
    LimitLvl1Consumer,
    LimitLvl2Consumer,
    LimitLvl4Consumer,
    LimitLvl5Consumer
)
from .pivot import PivotConsumer
from .water_availability import WaterAvailabilityConsumer
from .water_security import WaterSecurityConsumer
from .waterbody import WaterbodyConsumer
from .contrib import ContribConsumer


__all__ = [
    'AquiferConsumer',
    'BasinConsumer',
    'FlowRateConsumer',
    'HydrographyConsumer',
    'IrrigatedAreaConsumer',
    'LimitLvl1Consumer',
    'LimitLvl2Consumer',
    'LimitLvl4Consumer',
    'LimitLvl5Consumer',
    'WaterAvailabilityConsumer',
    'WaterSecurityConsumer',
    'WaterbodyConsumer',
    'ContribConsumer',
    'PivotConsumer'
]
