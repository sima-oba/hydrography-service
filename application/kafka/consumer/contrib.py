import logging

from application.schema import ContribSchema
from domain.service import ContribService
from .base import BaseConsumer
from ..error import error_handler


_log = logging.getLogger(__name__)


class ContribConsumer(BaseConsumer):
    def __init__(self, service: ContribService):
        super().__init__()
        self._service = service
        self._schema = ContribSchema()

    @error_handler
    def process(self, msg: any):
        data = self._schema.loads(msg.value())
        contrib = self._service.insert(data)
        _log.debug(f'{msg.key()}: added contribution {contrib._id}')
