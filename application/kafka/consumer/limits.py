import logging

from application.schema import (
    LimitLvl1Schema,
    LimitLvl2Schema,
    LimitLvl4Schema,
    LimitLvl5Schema
)
from domain.service import LimitsService
from .base import BaseConsumer
from ..error import error_handler


_log = logging.getLogger(__name__)


class LimitLvl1Consumer(BaseConsumer):
    def __init__(self, service: LimitsService):
        super().__init__()
        self._service = service
        self._schema = LimitLvl1Schema()

    @error_handler
    def process(self, msg: any):
        data = self._schema.loads(msg.value())
        limit = self._service.insert_limit_L1(data)
        _log.debug(f'{msg.key()}: added limit level 1 {limit._id}')


class LimitLvl2Consumer(BaseConsumer):
    def __init__(self, service: LimitsService):
        super().__init__()
        self._service = service
        self._schema = LimitLvl2Schema()

    @error_handler
    def process(self, msg: any):
        data = self._schema.loads(msg.value())

        for it in data:
            limit = self._service.insert_limit_L2(**it)
            _log.debug(f'{msg.key()}: added limit level 2 {limit._id}')


class LimitLvl4Consumer(BaseConsumer):
    def __init__(self, service: LimitsService):
        super().__init__()
        self._service = service
        self._schema = LimitLvl4Schema()

    @error_handler
    def process(self, msg: any):
        data = self._schema.loads(msg.value())
        limit = self._service.insert_limit_L4(data)
        _log.debug(f'{msg.key()}: added limit level 4 {limit._id}')


class LimitLvl5Consumer(BaseConsumer):
    def __init__(self, service: LimitsService):
        super().__init__()
        self._service = service
        self._schema = LimitLvl5Schema()

    @error_handler
    def process(self, msg: any):
        data = self._schema.loads(msg.value())
        limit = self._service.insert_limit_L5(data)
        _log.debug(f'{msg.key()}: added limit level 5 {limit._id}')
