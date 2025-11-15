from fastapi import FastAPI, Depends, HTTPException
from crud import crud_import_list
from crud import create_item, get_item, update_item, delete_item
from security import get_api_key
from database import init_db
from models import Item

app = FastAPI()

@app.post(path="/items/", response_model=Item)
def create_new_item(item: Item, api_key: str = Depends(get_api_key)):
    return
init_db()

@app.post(path='/items/', response_model=Item)
def create_new_item(item: Item, api_key: str = Depends(get_api_key)):
    create_item = add_item(item)
    return create_item

@app.get(path='/items/', response_model=List[Item])
def read_items(api_key: str = Depends(get_api_key)):
    return get_items()

@app.get(path='/items/{item_id}', response_model=Item)
def read_item(item_id: int, api_key: str = Depends(get_api_key)):
    item = get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return item

@app.put(path='/items/{item_id}', response_model=Item)
def update_existing_item(item_id: int, item: Item, api_key: str = Depends(get_api_key)):
    update_item = update_item(item_id, item)

@app.delete("/items/{item_id}", response_model=dict)
def delete_existing_item(item_id: int, api_key: str = Depends(get_api_key)):
    deleted = delete_item(item_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"message": "Item deleted successfully", "item_id": item_id}
