from fastapi import FastAPI
# from enum import Enum

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}


# class DirectionName(str, Enum):
#     north = "North"
#     south = "South"
#     west = "West"
#     east = "East"


@app.get("/")
async def read_all_books(skip_book: str | None = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.post("/")
async def create_book(book_title, book_author):
    current_book_id = 0
    if len(BOOKS) > 0:
        for book in BOOKS:
            i = int(book[-1])
            if i > current_book_id:
                current_book_id = i
    BOOKS[f"book_{current_book_id+1}"] = {"title": book_title, "author": book_author}
    return BOOKS[f"book_{current_book_id+1}"]


@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]


@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    book_information = {"title": book_title, "author": book_author}
    BOOKS[book_name] = book_information
    return book_information


@app.delete("/{book_name}")
async def delete_book(book_name: str):
    del BOOKS[book_name]
    return f"{book_name} has been deleted"


@app.get("/assignment/")
async def read_book_assignment(book_name):
    return BOOKS[book_name]


@app.delete("/assignment/")
async def delete_book_assignment(book_name: str):
    del BOOKS[book_name]
    return f"{book_name} has been deleted"


# @app.get("/books/favorite")
# async def read_favorite():
#     return {"favorite": "my favorite books"}
#
#
# @app.get("/books/{book_title}")
# async def read_book(book_title: str):
#     return {"book_title": book_title}
#
#
# @app.get("/directions/{direction_name}")
# async def get_direction(direction_name: DirectionName):
#     if direction_name == DirectionName.north:
#         return {"Direction": direction_name, "sub": "Up"}
#     elif direction_name == DirectionName.south:
#         return {"Direction": direction_name, "sub": "Down"}
#     elif direction_name == DirectionName.west:
#         return {"Direction": direction_name, "sub": "Left"}
#     if direction_name == DirectionName.east:
#         return {"Direction": direction_name, "sub": "Right"}
