from .aquifer import AquiferSchema
from .basin_schema import BasinSchema
from .contrib_schema import ContribSchema
from .flow_rate_schema import FlowRateSchema
from .hydrography_schema import HydrographySchema, RiverQuery
from .irrigated_area import IrrigatedAreaSchema
from .limits_schema import (
    LimitLvl1Schema,
    LimitLvl2Schema,
    LimitLvl4Schema,
    LimitLvl5Schema
)
from .pivot_schema import PivotSchema
from .water_availability_schema import WaterAvailabilitySchema
from .water_security_schema import WaterSecuritySchema
from .waterbody_schema import WaterbodySchema

__all__ = [
    'AquiferSchema',
    'BasinSchema',
    'ContribSchema',
    'FlowRateSchema',
    'HydrographySchema',
    'IrrigatedAreaSchema',
    'LimitLvl1Schema',
    'LimitLvl2Schema',
    'LimitLvl4Schema',
    'LimitLvl5Schema',
    'WaterAvailabilitySchema',
    'WaterbodySchema',
    'WaterSecuritySchema',
    'RiverQuery',
    'PivotSchema'
]
