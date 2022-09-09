import logging
from typing import List

from ..entity import Aquifer
from ..repository import IAquiferRepository


_log = logging.getLogger(__name__)


class AquiferService:
    def __init__(self, repo: IAquiferRepository):
        self._repo = repo

    def summary(self) -> List[dict]:
        return self._repo.summary()

    def find(self, ids: List[str]) -> List[Aquifer]:
        return self._repo.find_by_ids(ids)

    def save(self, data) -> Aquifer:
        aquifer = self._repo.find_by_imported_id(data['imported_id'])

        if aquifer is not None:
            _log.debug(f'Aquifer {aquifer._id} already exists. Skipping...')
            return aquifer

        aquifer = self._repo.add(Aquifer.new(data))
        _log.debug(f'Added aquifer {aquifer._id}')

        return aquifer
