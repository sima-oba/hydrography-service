from flask_restx import Resource, Namespace, fields
from flask_cachecontrol import cache_for

from domain.service import WaterSecurityService
from . import utils


def get_namespace(service: WaterSecurityService):
    ns = Namespace('Water Security', path='/water_security')

    model = utils.geojson_model(ns, ns.model('Watersec', {
        '_id': fields.String(description='ID'),
        'created_at': fields.DateTime(description='The creation date'),
        'updated_at': fields.DateTime(description='The update date'),
        'brazil': fields.String(description='Brazil'),
        'co_basin': fields.String(description='Co-Basin'),
        'economical': fields.String(description='Economical'),
        'ecosystem': fields.String(description='Ecosystem'),
        'human': fields.String(description='Human'),
        'resilience': fields.String(description='Resilience'),
        'area': fields.Float(description='Area'),
        'length': fields.Float(description='Length')
    }))

    @ns.route('/')
    class GeoJson(Resource):
        @ns.response(200, 'Returns a GeoJSON object', model)
        @cache_for(days=30)
        def get(self):
            water_security = service.find_all()
            return utils.make_geojson_response(water_security)

    return ns
