from pymongo.database import Database
from typing import List, Optional

from domain.entity import IrrigatedArea
from domain.repository import IIrrigatedAreaRepository


class IrrigatedRepository(IIrrigatedAreaRepository):
    def __init__(self, db: Database):
        self._collection = db.get_collection('irrigated_areas')

    def find_all(self) -> List[IrrigatedArea]:
        docs = self._collection.find()
        return [IrrigatedArea.from_dict(doc) for doc in docs]

    def find_by_imported_id(self, imported_id: str) -> Optional[IrrigatedArea]:
        doc = self._collection.find_one({'imported_id': imported_id})
        return IrrigatedArea.from_dict(doc) if doc else None

    def add(self, irrigated_area: IrrigatedArea) -> IrrigatedArea:
        self._collection.insert_one(irrigated_area.asdict())
        return irrigated_area
