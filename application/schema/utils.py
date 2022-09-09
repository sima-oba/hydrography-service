from dataclasses import is_dataclass
from orjson import dumps


def export_feature_collection(data: list, field: str = 'geometry') -> str:
    if not data:
        return dumps({
            'type': 'FeatureCollection',
            'features': []
        })

    features = []

    for index, feat in enumerate(data):
        if is_dataclass(feat):
            feat = feat.__dict__

        field = feat.pop(field, None)

        features.append({
            'id': index,
            'type': 'Feature',
            'properties': {key: value for key, value in feat.items()},
            'geometry': field
        })

    return dumps({
        'type': 'FeatureCollection',
        'features': features
    })


def check_required_fields(data: dict, required_fields: list) -> dict:
    keys = data.keys()
    return {
        field: 'Missing field'
        for field in required_fields if field not in keys
    }
