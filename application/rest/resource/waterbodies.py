from flask_restx import Resource, Namespace, fields
from flask_cachecontrol import cache_for

from domain.service import WaterbodyService
from . import utils


def get_namespace(service: WaterbodyService) -> Namespace:
    ns = Namespace('Waterbodies', path='/waterbodies')

    model = utils.geojson_model(ns, ns.model('waterbody', {
        "_id": fields.String(description='ID'),
        "created_at": fields.DateTime(description='The creation date'),
        "updated_at": fields.DateTime(description='The update date'),
        "name": fields.String(description='Name'),
        "type": fields.String(description='Type')
    }))

    @ns.route('/')
    class GeoJson(Resource):
        @ns.response(200, 'Returns a GeoJSON object', model)
        @cache_for(days=30)
        def get(self):
            waterbodies = service.find_all()
            return utils.make_geojson_response(waterbodies)

    return ns
