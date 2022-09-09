from marshmallow import Schema, fields


class WaterbodySchema(Schema):
    type = fields.String(required=True)
    name = fields.String(allow_none=True)
    geometry = fields.Dict(required=True)
