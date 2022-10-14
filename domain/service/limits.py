import uuid
from typing import List
from datetime import datetime as dt

from domain.entity import Limit_L1, Limit_L2, Limit_L4, Limit_L5
from domain.repository import LimitsRepositoryInterface


class LimitsService:
    def __init__(self, repo: LimitsRepositoryInterface):
        self._repo = repo

    def find_limits_L1(self) -> List[Limit_L1]:
        return self._repo.find_limits_L1()

    def find_limits_L2(self) -> List[Limit_L2]:
        return self._repo.find_limits_L2()

    def find_limits_L4(self) -> List[Limit_L4]:
        return self._repo.find_limits_L4()

    def find_limits_L5(self) -> List[Limit_L5]:
        return self._repo.find_limits_L5()

    def insert_limit_L1(self, data: dict) -> Limit_L1:
        return self._repo.insert_limit_L1(Limit_L1.new(data))

    def insert_limit_L2(self, **data) -> Limit_L2:
        limit = Limit_L2(
            _id=str(uuid.uuid4()),
            created_at=dt.now(),
            updated_at=dt.now(),
            **data
        )
        return self._repo.insert_limit_L2(limit)

    def insert_limit_L4(self, data: dict) -> Limit_L4:
        limit = Limit_L4(
            _id=str(uuid.uuid4()),
            created_at=dt.now(),
            updated_at=dt.now(),
            **data
        )
        return self._repo.insert_limit_L4(limit)

    def insert_limit_L5(self, data: dict) -> Limit_L4:
        limit = Limit_L5(
            _id=str(uuid.uuid4()),
            created_at=dt.now(),
            updated_at=dt.now(),
            **data
        )
        return self._repo.insert_limit_L5(limit)
