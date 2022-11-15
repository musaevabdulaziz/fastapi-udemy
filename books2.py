from fastapi import FastAPI, HTTPException, Request, status, Form, Header
from pydantic import BaseModel, Field
from uuid import UUID
from starlette.responses import JSONResponse


app = FastAPI()


class NegativeNumberException(Exception):
    def __init__(self, books_to_return):
        self.books_to_return = books_to_return


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str | None = Field(title="Description of book",
                                    min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            "example": {
                "id": "71f4c2ea-1340-41f4-89f7-2852347cc0d1",
                "title": "System Design",
                "author": "Alex Xu",
                "description": "A very nice description of a book",
                "rating": 100
            }
        }


class BookNoRating(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str
    description: str | None = Field(None, title="A description of a book", min_length=1, max_length=100)


BOOKS = []


@app.exception_handler(NegativeNumberException)
async def negative_number_exception_handler(request: Request, exception: NegativeNumberException):
    return JSONResponse(status_code=418,
                        content={"message": f"Hey! Why do you want {exception.books_to_return} books?"})


@app.post("/books/login/")
async def book_login(wanted_book: int, username: str | None = Header(None), password: str | None = Header(None)):
    if username == "FastAPIUser" and password == "test1234!":
        return BOOKS[wanted_book]
    return "Invalid User"


@app.get("/header")
async def read_header(random_header: str | None = Header(None)):
    return {"Random-header": random_header}


@app.get("/")
async def read_all_books(books_to_return: int | None = None):
    if books_to_return and books_to_return < 0:
        raise NegativeNumberException(books_to_return=books_to_return)

    if len(BOOKS) < 1:
        create_books_no_api()
    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 0
        new_books = []
        while i < books_to_return:
            new_books.append(BOOKS[i])
            i += 1
        return new_books
    return BOOKS


@app.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    BOOKS.append(book)
    return BOOKS


@app.get("/{book_id}")
async def read_book(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x
    raise raise_item_cannot_be_found_exception()


@app.get("/rating/{book_id}", response_model=BookNoRating)
async def read_book_no_rating(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x
    raise raise_item_cannot_be_found_exception()


@app.put("/{book_id}")
async def update_book(book_id: UUID, book: Book):
    count = 0
    for i in BOOKS:
        count += 1
        if i.id == book_id:
            BOOKS[count-1] = book
            return BOOKS[count-1]
    raise raise_item_cannot_be_found_exception()


@app.delete("/{book_id}")
async def delete_book(book_id: UUID):
    count = 0
    for x in BOOKS:
        count += 1
        if x.id == book_id:
            del BOOKS[count-1]
            return f"UUID: {book_id} has been deleted"
    raise raise_item_cannot_be_found_exception()


def create_books_no_api():
    book_1 = Book(id="71f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 1",
                  author="Author 1",
                  description="Description 1",
                  rating=60)
    book_2 = Book(id="21f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 2",
                  author="Author 2",
                  description="Description 2",
                  rating=70)
    book_3 = Book(id="31f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 3",
                  author="Author 3",
                  description="Description 3",
                  rating=80)
    book_4 = Book(id="41f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 4",
                  author="Author 4",
                  description="Description 4",
                  rating=90)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)


def raise_item_cannot_be_found_exception():
    return HTTPException(status_code=404, detail="Book not found",
                         headers={"X-Header-Error": "Nothing to be seen at the UUID"})