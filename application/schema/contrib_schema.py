from marshmallow import Schema, fields


class ContribSchema(Schema):
    nunivotto5 = fields.String(required=True)
    geometry = fields.Dict(required=True)
