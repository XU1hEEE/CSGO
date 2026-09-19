
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ... import crud, models, schemas
from ...db import session

router = APIRouter()

# Dependency
def get_db():
    db = session.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.item.Item)
def create_item(item: schemas.item.ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.item.get_item_by_market_hash_name(db, market_hash_name=item.market_hash_name)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already registered")
    return crud.item.create_item(db=db, item=item)


@router.get("/", response_model=List[schemas.item.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.item.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/{item_id}", response_model=schemas.item.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.item.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
