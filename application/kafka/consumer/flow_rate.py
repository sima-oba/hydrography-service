from application.schema import FlowRateSchema
from domain.service import FlowRateService
from .base import BaseConsumer
from ..error import error_handler


class FlowRateConsumer(BaseConsumer):
    def __init__(self, service: FlowRateService):
        super().__init__()
        self._service = service
        self._schema = FlowRateSchema()

    @error_handler
    def process(self, msg: any):
        data = self._schema.loads(msg.value())

        for it in data:
            self._service.save(it)
