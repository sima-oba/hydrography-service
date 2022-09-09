from flask import request, jsonify
from flask_restx import Resource, Namespace, fields
from flask_cachecontrol import cache_for
from marshmallow.exceptions import ValidationError

from domain.service import AquiferService
from . import utils


def get_namespace(service: AquiferService) -> Namespace:
    ns = Namespace('Aquifers', path='/aquifers')

    summary = ns.model('Aquifer', {
        '_id': fields.String(description='ID'),
        'created_at': fields.DateTime(description='The creation date'),
        'updated_at': fields.DateTime(description='The update date'),
        'imported_id': fields.String(description='Imported id'),
        'type': fields.String(description='Type'),
        'name': fields.String(description='Name'),
        'area': fields.Float(description='Area'),
        'length': fields.Float(description='Length')
    })

    geojson = utils.geojson_model(ns, summary)

    @ns.route('/')
    class Summary(Resource):
        @ns.response(200, 'Summary of all aquifers', summary)
        @cache_for(days=30)
        def get(self):
            return jsonify(service.summary())

    @ns.route('/geojson')
    class GeoJson(Resource):
        @ns.response(200, 'Returns a GeoJSON object', geojson)
        @cache_for(days=30)
        def get(self):
            ids = request.args.get('ids')

            if ids is None:
                raise ValidationError({'ids': 'Must not be null'})

            aquifers = service.find(ids.split(','))
            return utils.make_geojson_response(aquifers)

    return ns
