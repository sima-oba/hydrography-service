import logging

from application.schema import WaterbodySchema
from domain.service import WaterbodyService
from .base import BaseConsumer
from ..error import error_handler


_log = logging.getLogger(__name__)


class WaterbodyConsumer(BaseConsumer):
    def __init__(self, service: WaterbodyService):
        super().__init__()
        self._service = service
        self._schema = WaterbodySchema()

    @error_handler
    def process(self, msg: any):
        data = self._schema.loads(msg.value())
        waterbody = self._service.insert(data)
        _log.debug(f'{msg.key()}: added waterbody {waterbody._id}')
