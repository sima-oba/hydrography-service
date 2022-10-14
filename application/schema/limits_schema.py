from marshmallow import (
    validates_schema,
    post_load,
    Schema,
    ValidationError,
    fields,
    EXCLUDE
)

from .feature_collection_schema import FeatureCollectionSchema
from . import utils


class LimitLvl1Schema(Schema):
    wts_cd_pfafstetterbasin = fields.String(required=True)
    wts_cd_pfafstetterbasincodelevel = fields.Integer(required=True)
    wts_gm_area = fields.Float(required=True)
    wts_pk = fields.Float(required=True)
    geometry = fields.Dict(required=True)


class LimitLvl2Schema(FeatureCollectionSchema):
    @validates_schema
    def validate(self, data: dict, **kwargs):
        features = data.get('features', [])

        for index in range(len(features)):
            feat = features[index]
            properties = feat['properties']
            errors = utils.check_required_fields(properties, ['nivel02'])
            if errors:
                raise ValidationError({'features': {index: errors}})

    @post_load
    def create_limits_lvl_2(self, data: dict, **kwargs):
        features = data['features']
        limits = []

        for feat in features:
            properties = feat['properties']
            geometry = feat['geometry']
            limit = {
                'level': properties['nivel02'],
                'geometry': geometry
            }
            limits.append(limit)
        return limits


class LimitLvl4Schema(Schema):
    class Meta:
        unknown = EXCLUDE
    geometry = fields.Dict(required=True)


class LimitLvl5Schema(Schema):
    class Meta:
        unknown = EXCLUDE
    geometry = fields.Dict(required=True)
