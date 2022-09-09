from marshmallow import Schema, fields


class WaterSecuritySchema(Schema):
    brazil = fields.String(required=True)
    co_basin = fields.String(required=True)
    economical = fields.String(allow_none=True)
    ecosystem = fields.String(allow_none=True)
    human = fields.String(allow_none=True)
    resilience = fields.String(required=True)
    area = fields.Float(required=True)
    length = fields.Float(required=True)
    geometry = fields.Dict(required=True)
