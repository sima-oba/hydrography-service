from flask_restx import Resource, Namespace, fields
from flask_cachecontrol import cache_for

from domain.service import BasinService
from . import utils


def get_namespace(service: BasinService) -> Namespace:
    ns = Namespace('Basins', path='/basins')

    model = utils.geojson_model(ns, ns.model('Basin', {
        '_id': fields.String(description='ID'),
        'created_at': fields.DateTime(description='The creation date'),
        'updated_at': fields.DateTime(description='The update date'),
        'imported_id': fields.Integer(description='Imported id'),
        'name': fields.String(description='Name'),
        'area': fields.Float(description='Area'),
        'level': fields.String(description='Level'),
        'theid': fields.Integer(description='Theid'),
        'code': fields.Integer(description='Code'),
        'slope': fields.Float(description='Slope'),
        'rivers_length': fields.Float(description='Rivers length'),
        'rivers_slope': fields.Float(description='Rivers slope')
    }))

    @ns.route('/')
    class GeoJson(Resource):
        @ns.response(200, 'Returns a GeoJSON object', model)
        @cache_for(days=30)
        def get(self):
            basins = service.find_all()
            return utils.make_geojson_response(basins)

    return ns
