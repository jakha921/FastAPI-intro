from typing import List

from fastapi import FastAPI, Query, Path, Body

from schemas import Book, Author, Genre, BookOut

app = FastAPI()


@app.get("/")
async def root():
    """On decorator set url path & in func enter what this func should do."""
    return {"message": "Hello World"}


@app.post("/book", response_model=BookOut)

# NG value not returned ! response_model_exclude_unset=True
# exclude given models ! response_model_exclude={'data', 'summary'}
# include just return given models  ! response_model_include={'data', 'summary'}

# async def create_book(book: Book, author: Author, quantity: int = Body(...)):
#     return {'book': book, 'author': author, 'quantity': quantity}
async def create_book(book: Book):
    print(book.dict())
    return BookOut(**book.dict(), id=3)


@app.get("/book")
async def get_book(BookName: List[str] = \
                           Query(["Rich dad", "Poor dad"], \
                                 description='Search book', regex=r'[ -~]', \
                                 min_length=2, max_length=5)):
    return BookName


@app.get("/book/{pk}")
async def get_single_book(pk: int = Path(..., gt=1, le=20), \
                          pages: int = Query(None, gt=10, le=500)):
    return {'pk': pk, "pages": pages}


@app.post('/author')
async def create_author(author: Author):
    return {"author": author}
