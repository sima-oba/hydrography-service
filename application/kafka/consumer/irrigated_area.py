from domain.service import IrrigatedAreaService
from .base import BaseConsumer
from ..error import error_handler
from ...schema import IrrigatedAreaSchema


class IrrigatedAreaConsumer(BaseConsumer):
    def __init__(self, service: IrrigatedAreaService):
        super().__init__()
        self._service = service
        self._schema = IrrigatedAreaSchema()

    @error_handler
    def process(self, msg: any):
        data = self._schema.loads(msg.value())
        self._service.save(data)
