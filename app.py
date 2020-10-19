from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class GetItem(BaseModel):
    id:int
    baseValue:str
    compName:Optional[str] = None
    totalRevenue: float

get_Item = GetItem(
        id = 1234,
        baseValue = "test value",
        totalRevenue = 12345.909

)


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/")
def read_root():
    return get_Item


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="info")
    
