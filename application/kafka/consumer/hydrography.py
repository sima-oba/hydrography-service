import logging

from application.schema import HydrographySchema
from domain.service import HydrographyService
from .base import BaseConsumer
from ..error import error_handler


_log = logging.getLogger(__name__)


class HydrographyConsumer(BaseConsumer):
    def __init__(self, service: HydrographyService):
        super().__init__()
        self._service = service
        self._schema = HydrographySchema()

    @error_handler
    def process(self, msg: any):
        data = self._schema.loads(msg.value())

        for it in data:
            hydrography = self._service.insert(**it)
            _log.debug(f'{msg.key()}: added hydrography {hydrography._id}')
