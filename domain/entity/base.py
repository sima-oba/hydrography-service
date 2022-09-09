from dataclasses import dataclass, asdict
from datetime import datetime
from dacite.core import from_dict
from uuid import uuid4


@dataclass
class Base:
    _id: str
    created_at: datetime
    updated_at: datetime

    def asdict(self) -> dict:
        return asdict(self)

    def merge(self, data: dict):
        return from_dict(
            self.__class__,
            {
                **self.asdict(),
                'updated_at': datetime.now(),
                **data
            }
        )

    @classmethod
    def new(cls, data: dict):
        return cls(
            _id=str(uuid4()),
            created_at=datetime.now(),
            updated_at=datetime.now(),
            **data
        )

    @classmethod
    def from_dict(cls, data: dict):
        return from_dict(cls, data)
