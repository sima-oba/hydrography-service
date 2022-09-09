from .aquifer import AquiferService
from .basin import BasinService
from .contrib import ContribService
from .flow_rate import FlowRateService
from .hydrography import HydrographyService
from .irrigated_area import IrrigatedAreaService
from .limits import LimitsService
from .pivot import PivotService
from .water_availability import WaterAvailabilityService
from .water_security import WaterSecurityService
from .waterbody import WaterbodyService

__all__ = [
    'AquiferService',
    'BasinService',
    'ContribService',
    'FlowRateService',
    'HydrographyService',
    'IrrigatedAreaService',
    'LimitsService',
    'PivotService',
    'WaterAvailabilityService',
    'WaterbodyService',
    'WaterSecurityService'
]
