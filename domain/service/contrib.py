import uuid
from typing import List
from datetime import datetime as dt

from domain.entity import Contrib
from domain.repository import ContribRepositoryInterface


class ContribService:
    def __init__(self, repo: ContribRepositoryInterface):
        self._repo = repo

    def find_all(self) -> List[Contrib]:
        return self._repo.find_all()

    def insert(self, data: dict) -> Contrib:
        contrib = Contrib(
            _id=str(uuid.uuid4()),
            created_at=dt.now(),
            updated_at=None,
            **data
        )
        return self._repo.insert(contrib)
