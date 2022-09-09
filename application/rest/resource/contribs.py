from flask_restx import Resource, Namespace, fields
from flask_cachecontrol import cache_for

from domain.service import ContribService
from . import utils


def get_namespace(service: ContribService) -> Namespace:
    ns = Namespace('Contributions', path='/contribs')

    model = utils.geojson_model(ns, ns.model('Contribs', {
        '_id': fields.String(description='ID'),
        'created_at': fields.DateTime(description='The creation date'),
        'updated_at': fields.DateTime(description='The update date')
    }))

    @ns.route('/')
    class GeoJson(Resource):
        @ns.response(200, 'Returns a GeoJSON object', model)
        @cache_for(days=30)
        def get(self):
            contribs = service.find_all()
            return utils.make_geojson_response(contribs)

    return ns
