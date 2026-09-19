
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import database

app = FastAPI()

# 获取数据库会话
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = db.query(database.Item).offset(skip).limit(limit).all()
    return items

# 这是一个非常简单的数据提取函数，作为示例
# 在实际应用中，您应该使用更健壮的方法，例如 Celery
@app.post("/ingest-data/")
def ingest_data(db: Session = Depends(get_db)):
    import requests

    # 替换为实际的 API 端点
    # 这里我们使用一个示例数据
    sample_data = [
        {"name": "AK-47 | Redline", "price": 10.50},
        {"name": "AWP | Asiimov", "price": 75.20},
    ]

    for item_data in sample_data:
        db_item = database.Item(name=item_data["name"], price=item_data["price"])
        db.add(db_item)
    
    db.commit()
    return {"status": "success"}
