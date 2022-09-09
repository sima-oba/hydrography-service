from flask_restx import Resource, Namespace, fields
from flask_cachecontrol import cache_for

from domain.service import LimitsService
from . import utils


def get_namespace(service: LimitsService) -> Namespace:
    ns = Namespace('Limits', path='/')

    limits_lvl_1_model = utils.geojson_model(ns, ns.model('Limit1', {
        '_id': fields.String(description='ID'),
        'created_at': fields.DateTime(description='The creation date'),
        'updated_at': fields.DateTime(description='The update date'),
        'wts_cd_pfafstetterbasin': fields.String(),
        'wts_cd_pfafstetterbasincodelevel': fields.String(),
        'wts_gm_area': fields.String(description='wts_gm_area'),
        'wts_pk': fields.String(description='wts_pk')
    }))

    limits_lvl_2_model = utils.geojson_model(ns, ns.model('Limit2', {
        '_id': fields.String(description='ID'),
        'created_at': fields.DateTime(description='The creation date'),
        'updated_at': fields.DateTime(description='The update date'),
        'level': fields.String(description='Level')
    }))

    @ns.route('/limits_lvl_1')
    class LimitsLvl1GeoJson(Resource):
        @ns.response(200, 'Returns a GeoJSON object', limits_lvl_1_model)
        @cache_for(days=30)
        def get(self):
            limits = service.find_limits_L1()
            return utils.make_geojson_response(limits)

    @ns.route('/limits_lvl_2')
    class LimitsLv2GeoJson(Resource):
        @ns.response(200, 'Returns a GeoJSON object', limits_lvl_2_model)
        @cache_for(days=30)
        def get(self):
            limits = service.find_limits_L2()
            return utils.make_geojson_response(limits)

    return ns
