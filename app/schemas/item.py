
from pydantic import BaseModel
from datetime import datetime

class ItemBase(BaseModel):
    name: str
    market_hash_name: str
    price: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    last_updated: datetime

    class Config:
        orm_mode = True
