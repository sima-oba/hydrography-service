from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validates_schema,
    post_load
)

from .feature_collection_schema import FeatureCollectionSchema
from . import utils


class HydrographySchema(FeatureCollectionSchema):
    @validates_schema
    def validate(self, data: dict, **kwargs):
        features = data.get('features', [])

        for index in range(len(features)):
            feat = features[index]
            properties = feat['properties']
            errors = utils.check_required_fields(
                properties,
                [
                    'CORIO',
                    'DSVERSAO',
                    'IDRIO',
                    'NORIOCOMP',
                    'NUCOMPRIO',
                    'NUDISTBACR'
                ]
            )
            if errors:
                raise ValidationError({'features': {index: errors}})

    @post_load
    def create_hidrography(self, data: dict, **kwargs) -> list:
        features = data['features']
        hydrography = []

        for feat in features:
            properties = feat['properties']
            geometry = feat['geometry']
            item = {
                'co_river': properties['CORIO'],
                'id_river': properties['IDRIO'],
                'name_river': properties['NORIOCOMP'],
                'river_length': properties['NUCOMPRIO'],
                'basin_distance': properties['NUDISTBACR'],
                'ds_version': properties['DSVERSAO'],
                'geometry': geometry
            }
            hydrography.append(item)
        return hydrography


class RiverQuery(Schema):
    ids = fields.List(fields.String(), missing=[])
