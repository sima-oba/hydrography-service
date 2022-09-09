import json
from pymongo.database import Database
from gridfs import GridFS
from typing import List

from domain.entity import Aquifer
from domain.repository import IAquiferRepository


class AquiferRepository(IAquiferRepository):
    def __init__(self, db: Database):
        self._fs = GridFS(db, 'aquifer_fs')
        self._collection = db['aquifer']

    def _from_doc(self, doc: dict) -> Aquifer:
        file = self._fs.find_one({'_id': doc['_id']})
        geometry = json.loads(file.read())
        return Aquifer.from_dict({**doc, 'geometry': geometry})

    def summary(self) -> List[dict]:
        docs = self._collection.find().sort('name')
        return [doc for doc in docs]

    def find_by_imported_id(self, imported_id: str) -> Aquifer:
        doc = self._collection.find_one({'imported_id': imported_id})
        return self._from_doc(doc) if doc else None

    def find_by_ids(self, ids: List[str]) -> List[Aquifer]:
        docs = self._collection.find({'_id': {'$in': ids}})
        return [self._from_doc(doc) for doc in docs]

    def add(self, aquifer: Aquifer) -> Aquifer:
        doc = aquifer.asdict()
        geometry = doc.pop('geometry')
        geometry = json.dumps(geometry, ensure_ascii=False).encode('utf-8')

        self._collection.insert_one(doc)
        self._fs.put(geometry, _id=aquifer._id)

        return aquifer
