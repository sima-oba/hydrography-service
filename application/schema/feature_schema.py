from marshmallow import Schema, fields, validate
from marshmallow_geojson import GeometriesSchema


class FeatureSchema(Schema):
    id = fields.Integer(required=True)
    type = fields.Str(
        required=True,
        validate=validate.OneOf(['Feature'], error='Invalid feature type')
    )
    geometry = fields.Nested(GeometriesSchema, required=True)
    properties = fields.Dict(required=True)
