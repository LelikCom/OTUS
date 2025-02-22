from fastapi import APIRouter
from models import Item


router = APIRouter()

items = [{"id": 1, "name": "Книга 1"}, {"id": 2, "name": "Книга 2"}]


@router.get("/items")
def get_items():
    return items


@router.get("/items/{item_id}")
def get_item(item_id: int):
    return next(
        (item for item in items if item["id"] == item_id), {"error": "Item not found"}
    )


@router.post("/items")
def create_item(item: Item):
    new_item = item.dict()
    new_item["id"] = len(items) + 1
    items.append(new_item)
    return new_item
