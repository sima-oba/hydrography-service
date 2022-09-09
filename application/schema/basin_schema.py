from marshmallow import post_load

from .feature_collection_schema import FeatureCollectionSchema


class BasinSchema(FeatureCollectionSchema):
    def get_one_of(self, data: dict, keys: tuple, default=None) -> any:
        for k in keys:
            value = data.get(k)
            if value is not None:
                return value
        return default

    @post_load
    def create_basins(self, data: dict, **kwargs):
        features = data['features']
        basins = []

        for feat in features:
            props = feat['properties']
            geometry = feat['geometry']
            basin = {
                'name': self.get_one_of(props, ('NOME', 'nome'), 'unknown'),
                'imported_id': props.get('ID'),
                'area': self.get_one_of(props, ('area', 'area_km2')),
                'code': props.get('codigo'),
                'slope': props.get('declive'),
                'rivers_length': props.get('rios_comp'),
                'rivers_slope': props.get('rios_decli'),
                'level': props.get('n\u00edvel_1'),
                'theid': props.get('theid'),
                'geometry': geometry
            }
            basins.append(basin)
        return basins
