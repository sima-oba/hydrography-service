from dataclasses import is_dataclass
from flask import Response, make_response
from flask_restx import Namespace, Model, fields
from orjson import dumps


def export_feature_collection(data: list) -> dict:
    if not data:
        return {
            'type': 'FeatureCollection',
            'features': []
        }

    features = []

    for index, feat in enumerate(data):
        if is_dataclass(feat):
            feat = feat.__dict__

        geometry = feat.pop('geometry', None)

        features.append({
            'id': index,
            'type': 'Feature',
            'properties': {key: value for key, value in feat.items()},
            'geometry': geometry
        })

    return {
        'type': 'FeatureCollection',
        'features': features
    }


def geojson_model(ns: Namespace, properties: Model) -> Model:
    name = properties.name

    geometry = ns.model(name + 'Geometry', {
        'type': fields.String(),
        'coordinates': fields.List(fields.Float())
    })

    feature = ns.model(name + 'Feature', {
        'id': fields.Integer(),
        'properties': fields.Nested(properties),
        'geometry': fields.Nested(geometry)
    })

    return ns.model(name + 'FeatureCollection', {
        'type': fields.String(),
        'features': fields.List(fields.Nested(feature))
    })


def make_geojson_response(content: list) -> Response:
    resp = make_response()
    resp.content_type = 'application/json'
    resp.status_code = 200
    resp.data = dumps(export_feature_collection(content))

    return resp
