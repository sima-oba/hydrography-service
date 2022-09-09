from domain.service import PivotService
from .base import BaseConsumer
from ..error import error_handler
from ...schema import PivotSchema


class PivotConsumer(BaseConsumer):
    def __init__(self, service: PivotService):
        super().__init__()
        self._service = service
        self._schema = PivotSchema()

    @error_handler
    def process(self, msg: any):
        data = self._schema.loads(msg.value())
        self._service.insert(data)
