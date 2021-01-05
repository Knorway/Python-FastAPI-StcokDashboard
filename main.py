from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

template = Jinja2Templates(directory="templates")

@app.get('/')
def home(request: Request):
    """
    displays the stock screener dashboard / homepage
    """
    return template.TemplateResponse("home.jinja", {
        "request": request,
        "somevar": 2
    })

@app.post('/stock')
def create_stock():
    """
    creates a stock and stores it in the database
    """
    return {
        "code": "success",
        "message": "stock created"
    }

# @app.get('/items/{item_id}')
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}