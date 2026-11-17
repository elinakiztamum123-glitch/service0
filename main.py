from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = {}
next_id = 1


class Item(BaseModel):
    name: str
    price: float


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def post_item(item: Item):
    global next_id
    items[next_id] = item
    next_id += 1
    return {"id": next_id - 1, **item.dict()}


@app.put("/items/{item_id}")
def put_item(item_id: int, item: Item):
    items[item_id] = item
    return {"id": item_id, **item.dict()}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    items.pop(item_id, None)
    return {"ok": True}