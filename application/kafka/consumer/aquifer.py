from domain.service import AquiferService
from .base import BaseConsumer
from ..error import error_handler
from ...schema import AquiferSchema


class AquiferConsumer(BaseConsumer):
    def __init__(self, service: AquiferService):
        super().__init__()
        self._service = service
        self._schema = AquiferSchema()

    @error_handler
    def process(self, msg: any):
        data = self._schema.loads(msg.value())
        self._service.save(data)
