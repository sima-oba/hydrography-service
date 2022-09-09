from marshmallow import validates_schema, post_load, ValidationError

from .feature_collection_schema import FeatureCollectionSchema
from . import utils


class FlowRateSchema(FeatureCollectionSchema):
    @validates_schema
    def validate(self, data: dict, **kwargs):
        features = data.get('features', [])

        for index in range(len(features)):
            feat = features[index]
            properties = feat['properties']
            errors = utils.check_required_fields(
                properties, ['COBACIA', 'Dominio', 'Nome_Rio']
            )
            if errors:
                raise ValidationError({'features': {index: errors}})

    @post_load
    def create_flow_rates(self, data: dict, **kwargs):
        features = data['features']
        flow_rates = []

        for feat in features:
            properties = feat['properties']
            geometry = feat['geometry']
            flow = {
                'co_basin': properties['COBACIA'],
                'domain': properties['Dominio'],
                'river': properties['Nome_Rio'] or 'unknown',
                'q90': properties.get('q90', None),
                'qmld': properties.get('qmld', None),
                'geometry': geometry
            }
            flow_rates.append(flow)
        return flow_rates
