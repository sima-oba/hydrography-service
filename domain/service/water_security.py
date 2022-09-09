from typing import List

from domain.entity.water_security import WaterSecurity
from domain.repository import WaterSecurityRepositoryInterface


class WaterSecurityService:
    def __init__(self, repo: WaterSecurityRepositoryInterface):
        self._repo = repo

    def find_all(self) -> List[WaterSecurity]:
        return self._repo.find_all()

    def insert(self, data: dict) -> WaterSecurity:
        return self._repo.insert(WaterSecurity.new(data))
