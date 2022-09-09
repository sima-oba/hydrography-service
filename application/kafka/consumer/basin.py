import logging

from application.schema import BasinSchema
from domain.service import BasinService
from .base import BaseConsumer
from ..error import error_handler


_log = logging.getLogger(__name__)


class BasinConsumer(BaseConsumer):
    def __init__(self, service: BasinService):
        super().__init__()
        self._service = service
        self._schema = BasinSchema()

    @error_handler
    def process(self, msg: any):
        data = self._schema.loads(msg.value())

        for it in data:
            basin = self._service.insert(it)
            _log.debug(f'{msg.key()}: added basin {basin._id}')
