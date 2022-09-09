from marshmallow import Schema, fields


class IrrigatedAreaSchema(Schema):
    imported_id = fields.String(required=True)
    length = fields.Float(required=True)
    area = fields.Float(required=True)
    geometry = fields.Dict(required=True)
