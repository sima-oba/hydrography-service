import logging

from application.schema import WaterSecuritySchema
from domain.service import WaterSecurityService
from .base import BaseConsumer
from ..error import error_handler


_log = logging.getLogger(__name__)


class WaterSecurityConsumer(BaseConsumer):
    def __init__(self, service: WaterSecurityService):
        super().__init__()
        self._service = service
        self._schema = WaterSecuritySchema()

    @error_handler
    def process(self, msg: any):
        data = self._schema.loads(msg.value())
        result = self._service.insert(data)
        _log.debug(f'{msg.key()}: added water security {result._id}')
