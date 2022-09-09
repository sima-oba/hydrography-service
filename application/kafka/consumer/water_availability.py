import logging

from application.schema import WaterAvailabilitySchema
from domain.service import WaterAvailabilityService
from .base import BaseConsumer
from ..error import error_handler


_log = logging.getLogger(__name__)


class WaterAvailabilityConsumer(BaseConsumer):
    def __init__(self, service: WaterAvailabilityService):
        super().__init__()
        self._service = service
        self._schema = WaterAvailabilitySchema()

    @error_handler
    def process(self, msg: any):
        data = self._schema.loads(msg.value())
        result = self._service.insert(data)
        _log.debug(f'{msg.key()}: added water availability {result._id}')
