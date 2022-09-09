from .aquifer import IAquiferRepository
from .basin import BasinRepositoryInterface
from .flow_rate import FlowRateRepositoryInterface
from .hydrography import HydrographyRepositoryInterface
from .irrigated_area import IIrrigatedAreaRepository
from .contrib import ContribRepositoryInterface
from .pivot import PivotRepositoryInterface
from .water_security import WaterSecurityRepositoryInterface
from .water_availability import WaterAvailabilityRepositoryInterface
from .waterbody import WaterbodyRepositoryInterface
from .limits import LimitsRepositoryInterface

__all__ = [
    'IAquiferRepository',
    'BasinRepositoryInterface',
    'FlowRateRepositoryInterface',
    'HydrographyRepositoryInterface',
    'IIrrigatedAreaRepository',
    'ContribRepositoryInterface',
    'WaterSecurityRepositoryInterface',
    'WaterAvailabilityRepositoryInterface',
    'WaterbodyRepositoryInterface',
    'LimitsRepositoryInterface',
    'PivotRepositoryInterface'
]
