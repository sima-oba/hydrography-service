from typing import List

from domain.entity import Waterbody
from domain.repository import WaterbodyRepositoryInterface


class WaterbodyService:
    def __init__(self, repo: WaterbodyRepositoryInterface):
        self._repo = repo

    def find_all(self) -> List[Waterbody]:
        return self._repo.find_all()

    def insert(self, data: dict) -> dict:
        return self._repo.insert(Waterbody.new(data))
