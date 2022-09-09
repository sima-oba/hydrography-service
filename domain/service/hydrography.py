import uuid
from typing import List
from datetime import datetime as dt

from domain.entity.hydrography import Hydrography
from domain.repository import HydrographyRepositoryInterface


class HydrographyService:
    def __init__(self, repo: HydrographyRepositoryInterface):
        self._repo = repo

    def find_all(self) -> List[Hydrography]:
        return self._repo.find_all()

    def summary(self) -> List[dict]:
        return self._repo.summary()

    def find_by_id(self, *ids) -> List[Hydrography]:
        return self._repo.find_by_id(*ids)

    def insert(self, **data) -> Hydrography:
        hydrography = Hydrography(
            _id=str(uuid.uuid4()),
            created_at=dt.now(),
            updated_at=dt.now(),
            **data
        )
        return self._repo.insert(hydrography)
