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
from .consumer import (
    AquiferConsumer,
    BasinConsumer,
    FlowRateConsumer,
    HydrographyConsumer,
    IrrigatedAreaConsumer,
    LimitLvl1Consumer,
    LimitLvl2Consumer,
    PivotConsumer,
    WaterAvailabilityConsumer,
    WaterSecurityConsumer,
    WaterbodyConsumer,
    ContribConsumer
)


def start_consumer(config):
    db = get_database(config.MONGODB_SETTINGS)
    kafka_config = {
        'bootstrap.servers': config.KAFKA_SERVER,
        'group.id': 'HYDROGRAPHY',
        'enable.auto.commit': False,
        'auto.offset.reset': 'earliest',
        'fetch.message.max.bytes': 256 * 1024 ** 2
    }

    aquifer_repo = AquiferRepository(db)
    aquifer_service = AquiferService(aquifer_repo)
    aquifer_consumer = AquiferConsumer(aquifer_service)
    aquifer_consumer.start(kafka_config, 'AQUIFER')

    basin_repo = BasinRepository(db)
    basin_service = BasinService(basin_repo)
    basin_consumer = BasinConsumer(basin_service)
    basin_consumer.start(kafka_config, 'BASIN')

    flow_rate_repo = FlowRateRepository(db)
    flow_rate_service = FlowRateService(flow_rate_repo)
    flow_rate_consumer = FlowRateConsumer(flow_rate_service)
    flow_rate_consumer.start(kafka_config, 'FLOW_RATE')

    hydrography_repo = HydrographyRepository(db)
    hydrography_service = HydrographyService(hydrography_repo)
    hydrography_consumer = HydrographyConsumer(hydrography_service)
    hydrography_consumer.start(kafka_config, 'HYDROGRAPHY')

    irrigated_area_repo = IrrigatedRepository(db)
    irrigated_area_service = IrrigatedAreaService(irrigated_area_repo)
    irrigated_area_consumer = IrrigatedAreaConsumer(irrigated_area_service)
    irrigated_area_consumer.start(kafka_config, 'IRRIGATED_AREA')

    limits_repo = LimitsRepository(db)
    limits_service = LimitsService(limits_repo)
    limit_lvl_1_consumer = LimitLvl1Consumer(limits_service)
    limit_lvl_1_consumer.start(kafka_config, 'LIMIT_LVL_1')
    limit_lvl_2_consumer = LimitLvl2Consumer(limits_service)
    limit_lvl_2_consumer.start(kafka_config, 'LIMIT_LVL_2')

    water_avail_repo = WaterAvailabilityRepository(db)
    water_avail_service = WaterAvailabilityService(water_avail_repo)
    water_avail_consumer = WaterAvailabilityConsumer(water_avail_service)
    water_avail_consumer.start(kafka_config, 'WATER_AVAILABILITY')

    water_security_repo = WaterSecurityRepository(db)
    water_security_service = WaterSecurityService(water_security_repo)
    water_security_consumer = WaterSecurityConsumer(water_security_service)
    water_security_consumer.start(kafka_config, 'WATER_SECURITY')

    waterbody_repo = WaterBodyRepository(db)
    waterbody_service = WaterbodyService(waterbody_repo)
    waterbody_consumer = WaterbodyConsumer(waterbody_service)
    waterbody_consumer.start(kafka_config, 'WATERBODY')

    contrib_repo = ContribRepository(db)
    contrib_service = ContribService(contrib_repo)
    contrib_consumer = ContribConsumer(contrib_service)
    contrib_consumer.start(kafka_config, 'CONTRIB')

    pivot_repo = PivotRepository(db)
    pivot_service = PivotService(pivot_repo)
    pivot_consumer = PivotConsumer(pivot_service)
    pivot_consumer.start(kafka_config, 'PIVOT')

    aquifer_consumer.wait()
    basin_consumer.wait()
    flow_rate_consumer.wait()
    hydrography_consumer.wait()
    irrigated_area_consumer.wait()
    limit_lvl_1_consumer.wait()
    limit_lvl_2_consumer.wait()
    pivot_consumer.wait()
    water_avail_consumer.wait()
    water_security_consumer.wait()
    waterbody_consumer.wait()
    contrib_consumer.wait()
