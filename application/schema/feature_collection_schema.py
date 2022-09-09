from marshmallow import Schema, fields, validate

from .feature_schema import FeatureSchema


class FeatureCollectionSchema(Schema):
    type = fields.Str(
        required=True,
        validate=validate.OneOf(
            ['FeatureCollection'],
            error='Invalid feature collection type'
        )
    )
    features = fields.List(fields.Nested(FeatureSchema), required=True)
