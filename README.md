# FastAPI

## Clone & run 
    

## Installation
    pip install fastapi
    
    pip install "uvicorn[standard]

## Create main.py file
    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}

## For run project 
    uvicorn main:app --reload
    
# Docs 
    Now go to http://127.0.0.1:8000/docs

    Alternative API docs upgrade
    And now, go to http://127.0.0.1:8000/redoc