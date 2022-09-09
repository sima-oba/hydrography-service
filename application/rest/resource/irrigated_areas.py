from flask_restx import Resource, Namespace, fields
from flask_cachecontrol import cache_for

from domain.service import IrrigatedAreaService
from . import utils


def get_namespace(service: IrrigatedAreaService) -> Namespace:
    ns = Namespace('Irrigated Areas', path='/irrigated_areas')

    model = utils.geojson_model(ns, ns.model('Irrigated Areas', {
        '_id': fields.String(description='ID'),
        'created_at': fields.DateTime(description='The creation date'),
        'updated_at': fields.DateTime(description='The update date'),
        'imported_id': fields.String(description='Imported id'),
        'length': fields.String(description='Length'),
        'area': fields.String(description='Area')
    }))

    @ns.route('/')
    class GeoJson(Resource):
        @ns.response(200, 'Returns a GeoJSON object', model)
        @cache_for(days=30)
        def get(self):
            irrigated_areas = service.get_all()
            return utils.make_geojson_response(irrigated_areas)

    return ns
