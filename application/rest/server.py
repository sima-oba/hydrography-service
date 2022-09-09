from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from domain.service import (
    AquiferService,
    BasinService,
    FlowRateService,
    HydrographyService,
    IrrigatedAreaService,
    ContribService,
    WaterSecurityService,
    LimitsService,
    PivotService,
    WaterAvailabilityService,
    WaterbodyService
)
from infrastructure.repository import (
    AquiferRepository,
    BasinRepository,
    FlowRateRepository,
    HydrographyRepository,
    IrrigatedRepository,
    ContribRepository,
    WaterSecurityRepository,
    WaterAvailabilityRepository,
    LimitsRepository,
    PivotRepository,
    WaterBodyRepository,
    get_database
)
from .resource import (
    aquifers,
    basins,
    contribs,
    flow_rates,
    hydrography,
    irrigated_areas,
    limits,
    pivots,
    water_availability,
    water_security,
    waterbodies
)
from .security import Authorization, Role
from . import error


API_PREFIX = '/api/v1/hydrography'


def create_server(config='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['JSON_SORT_KEYS'] = False
    app.url_map.strict_slashes = False

    error.register(app)
    CORS(app)

    if app.config['FLASK_ENV'] != 'development':
        auth = Authorization(app.config['INTROSPECTION_URI'])
        auth.grant_role_for_any_request(Role.ADMIN, Role.READ_HYDROGRAPHY)
        auth.require_authorization_for_any_request(app)

    api = Api(app, prefix=API_PREFIX, doc=API_PREFIX + '/doc')
    db = get_database(app.config['MONGODB_SETTINGS'])

    aquifer_repo = AquiferRepository(db)
    aquifer_svc = AquiferService(aquifer_repo)
    api.add_namespace(aquifers.get_namespace(aquifer_svc))

    basin_repo = BasinRepository(db)
    basin_svc = BasinService(basin_repo)
    api.add_namespace(basins.get_namespace(basin_svc))

    flow_rate_repo = FlowRateRepository(db)
    flow_rate_svc = FlowRateService(flow_rate_repo)
    api.add_namespace(flow_rates.get_namespace(flow_rate_svc))

    hydrography_repo = HydrographyRepository(db)
    hydrography_svc = HydrographyService(hydrography_repo)
    api.add_namespace(hydrography.get_namespace(hydrography_svc))

    irrigated_areas_repo = IrrigatedRepository(db)
    irrigated_areas_svc = IrrigatedAreaService(irrigated_areas_repo)
    api.add_namespace(irrigated_areas.get_namespace(irrigated_areas_svc))

    contrib_repo = ContribRepository(db)
    contrib_svc = ContribService(contrib_repo)
    api.add_namespace(contribs.get_namespace(contrib_svc))

    water_security_repo = WaterSecurityRepository(db)
    water_security_service = WaterSecurityService(water_security_repo)
    api.add_namespace(water_security.get_namespace(water_security_service))

    water_avail_repo = WaterAvailabilityRepository(db)
    water_avail_svc = WaterAvailabilityService(water_avail_repo)
    api.add_namespace(water_availability.get_namespace(water_avail_svc))

    limits_repo = LimitsRepository(db)
    limits_svc = LimitsService(limits_repo)
    api.add_namespace(limits.get_namespace(limits_svc))

    pivots_repo = PivotRepository(db)
    pivots_svc = PivotService(pivots_repo)
    api.add_namespace(pivots.get_namespace(pivots_svc))

    waterbody_repo = WaterBodyRepository(db)
    waterbody_svc = WaterbodyService(waterbody_repo)
    api.add_namespace(waterbodies.get_namespace(waterbody_svc))

    return app
