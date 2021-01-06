# import models
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import Stock


app = FastAPI()
models.Base.metadata.create_all(bind=engine)
template = Jinja2Templates(directory="templates")


class StockRequest(BaseModel):
    symbol: str


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/')
def home(request: Request):
    """
    displays the stock screener dashboard / homepage
    """
    return template.TemplateResponse("home.html", {
        "request": request,
    })


@app.post('/stock')
def create_stock(stock_request: StockRequest, db: Session = Depends(get_db)):
    """
    creates a stock and stores it in the database
    """
    stock = Stock()
    stock.symbol = stock_request.symbol

    db.add(stock)
    db.commit()

    return {
        "code": "success",
        "message": "stock created"
    }

# @app.get('/items/{item_id}')
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}
