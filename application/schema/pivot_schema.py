from marshmallow import Schema, fields


class PivotSchema(Schema):
    area = fields.Float(required=True)
    geometry = fields.Dict(required=True)
