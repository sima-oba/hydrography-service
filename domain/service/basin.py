import uuid
from typing import List
from datetime import datetime as dt

from domain.entity import Basin
from domain.repository import BasinRepositoryInterface


class BasinService:
    def __init__(self, repo: BasinRepositoryInterface):
        self._repo = repo

    def find_all(self) -> List[Basin]:
        return self._repo.find_all()

    def insert(self, data: dict) -> Basin:
        basin = Basin(
            _id=str(uuid.uuid4()),
            created_at=dt.now(),
            updated_at=dt.now(),
            imported_id=data.get('imported_id'),
            name=data.get('name', 'unknown'),
            area=data.get('area'),
            level=data.get('level'),
            theid=data.get('theid'),
            code=data.get('code'),
            slope=data.get('slope'),
            rivers_length=data.get('rivers_length'),
            rivers_slope=data.get('rivers_slope'),
            geometry=data.get('geometry')
        )
        return self._repo.insert(basin)
