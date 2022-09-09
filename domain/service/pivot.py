from typing import List

from domain.entity import Pivot
from domain.repository import PivotRepositoryInterface


class PivotService:
    def __init__(self, repo: PivotRepositoryInterface):
        self._repo = repo

    def find_all(self) -> List[Pivot]:
        return self._repo.find_all()

    def insert(self, data: dict) -> Pivot:
        return self._repo.insert(Pivot.new(data))
