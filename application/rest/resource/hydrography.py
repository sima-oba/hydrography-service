from flask import request
from flask_cachecontrol import cache_for
from flask_restx import Resource, Namespace, fields

from application.schema import RiverQuery
from domain.service import HydrographyService
from . import utils


def get_namespace(service: HydrographyService) -> Namespace:
    ns = Namespace('Rivers', path='/hydrography')
    query = RiverQuery()

    summary = ns.model('Hydrography', {
        '_id': fields.String(description='ID'),
        'created_at': fields.DateTime(description='The creation date'),
        'updated_at': fields.DateTime(description='The update date'),
        'co_river': fields.String(description='Co-river'),
        'id_river': fields.String(description='Id-river'),
        'name_river': fields.String(description='Name-river'),
        'river_length': fields.String(description='River-length'),
        'basin_distance': fields.String(description='Basin distance'),
        'ds_version': fields.String(description='DS version')
    })

    geojson = utils.geojson_model(ns, summary)

    @ns.route('/summary')
    class Summary(Resource):
        @ns.response(200, 'Summary of all rivers', summary)
        @cache_for(days=30)
        def get(self):
            return service.summary()

    @ns.route('/geojson')
    class GeoJson(Resource):
        @ns.response(200, 'Returns a GeoJSON object', geojson)
        @cache_for(days=30)
        def get(self):
            results = service.find_all()
            return utils.make_geojson_response(results)

        @ns.response(200, 'Returns a GeoJSON object', geojson)
        @cache_for(days=30)
        def post(self):
            ids = query.load(request.json)['ids']
            results = service.find_by_id(*ids)
            return utils.make_geojson_response(results)

    return ns
