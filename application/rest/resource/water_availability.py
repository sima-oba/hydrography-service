from flask_restx import Resource, Namespace, fields
from flask_cachecontrol import cache_for

from domain.service import WaterAvailabilityService
from . import utils


def get_namespace(service: WaterAvailabilityService) -> Namespace:
    ns = Namespace('Water Availability', path='/water_availability')

    model = utils.geojson_model(ns, ns.model('waterav', {
        "_id": fields.String(description='ID'),
        "created_at": fields.DateTime(description='The creation date'),
        "updated_at": fields.DateTime(description='The update date'),
        "OBJECTID": fields.Integer(),
        "cotrecho": fields.Integer(),
        'cocursodag': fields.String(),
        'cobacia': fields.String(),
        'nuareacont': fields.Float(),
        'nuareamont': fields.Float(),
        'noriocomp': fields.String(),
        'dedominial': fields.String(),
        'dsversao': fields.String(),
        'QmltEsp': fields.Float(),
        'Qmltinc': fields.Float(),
        'Qmlt': fields.Float(),
        'Q95ESP': fields.Float(),
        'Q95inc': fields.Float(),
        'Q95NAT': fields.Float(),
        'COBAR': fields.Float(),
        'COLAGO': fields.Float(),
        'COOPERA': fields.Float(),
        'DSOPERA': fields.String(),
        'QDEFLU': fields.Float(),
        'QLAGO': fields.Float(),
        'NORES': fields.String(),
        'saz': fields.Float(),
        'DQ95Jan': fields.Float(),
        'DQ95Fev': fields.Float(),
        'DQ95Mar': fields.Float(),
        'DQ95Abr': fields.Float(),
        'DQ95Mai': fields.Float(),
        'DQ95Jun': fields.Float(),
        'DQ95Jul': fields.Float(),
        'DQ95Ago': fields.Float(),
        'DQ95Set': fields.Float(),
        'DQ95Out': fields.Float(),
        'DQ95Nov': fields.Float(),
        'DQ95Dez': fields.Float(),
        'DQano': fields.Float(),
        'Fronteira': fields.Float(),
        'RelAplicad': fields.Float(),
        'FonteQmlt': fields.String(),
        'FONTEQ95': fields.String(),
        'FonteQanua': fields.String(),
        'FonteQsazo': fields.String(),
        'FonteQres': fields.String(),
        'dsversaoQ': fields.String(),
        'Shape_Leng': fields.Float()
    }))

    @ns.route('/')
    class GeoJson(Resource):
        @ns.response(200, 'Returns a GeoJSON object', model)
        @cache_for(days=30)
        def get(self):
            items = service.find_all()
            return utils.make_geojson_response(items)

    return ns
