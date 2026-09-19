
from sqlalchemy.orm import Session
from .. import models, schemas

def get_item(db: Session, item_id: int):
    return db.query(models.item.Item).filter(models.item.Item.id == item_id).first()

def get_item_by_market_hash_name(db: Session, market_hash_name: str):
    return db.query(models.item.Item).filter(models.item.Item.market_hash_name == market_hash_name).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.item.Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.item.ItemCreate):
    db_item = models.item.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
