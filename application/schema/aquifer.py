from marshmallow import Schema, fields, validate
from marshmallow_geojson import GeometriesSchema


_AQUIFER_TYPES = ['POROSO', 'CARSTICO', 'FRATURADO']


class AquiferSchema(Schema):
    imported_id = fields.String(required=True)
    type = fields.String(
        validate=validate.OneOf(_AQUIFER_TYPES), required=True
    )
    name = fields.String(required=True)
    area = fields.Float(required=True)
    length = fields.Float(required=True)
    geometry = fields.Nested(GeometriesSchema, required=True)
