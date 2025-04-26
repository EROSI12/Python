from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get('/items/')
def read_items():
    return {"Items":["Item1,""Item2","Item3" ]}

from fastapi import FastAPI

app = FastAPI()

# Sample items data
items = {
    1: {"name": "Book", "price": 12.99},
    2: {"name": "Pen", "price": 1.49}
}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items.get(item_id)
    if item:
        return {"item_id": item_id, "details": item}
    return {"error": "Item not found"}
