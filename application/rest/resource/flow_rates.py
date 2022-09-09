from flask_restx import Resource, Namespace, fields
from flask_cachecontrol import cache_for

from domain.service import FlowRateService
from . import utils


def get_namespace(service: FlowRateService) -> Namespace:
    ns = Namespace('Flow Rates', path='/flow_rates')

    model = utils.geojson_model(ns, ns.model('FlowRate', {
        '_id': fields.String(description='ID'),
        'created_at': fields.DateTime(description='The creation date'),
        'updated_at': fields.DateTime(description='The update date'),
        'co_basin': fields.String(description='Co-Basin'),
        'domain': fields.String(description='Domain'),
        'river': fields.String(description='River'),
        'q90': fields.String(description='q90'),
        'qmld': fields.String(description='qmld')
    }))

    @ns.route('/')
    class GeoJson(Resource):
        @ns.response(200, 'Returns a GeoJSON object', model)
        @cache_for(days=30)
        def get(self):
            flow_rates = service.find_all()
            return utils.make_geojson_response(flow_rates)

    return ns
