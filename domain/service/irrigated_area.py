import logging
from typing import List

from ..entity import IrrigatedArea
from ..repository import IIrrigatedAreaRepository


class IrrigatedAreaService:
    def __init__(self, repo: IIrrigatedAreaRepository):
        self._repo = repo
        self._log = logging.getLogger(self.__class__.__name__)

    def get_all(self) -> List[IrrigatedArea]:
        return self._repo.find_all()

    def save(self, data) -> IrrigatedArea:
        irrigated_area = self._repo.find_by_imported_id(data['imported_id'])

        if irrigated_area is not None:
            self._log.debug(f'Skipped irrigated area {irrigated_area._id}.')
            return irrigated_area

        irrigated_area = self._repo.add(IrrigatedArea.new(data))
        self._log.debug(f'Added irrigated area {irrigated_area._id}')

        return irrigated_area
