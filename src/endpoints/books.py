from fastapi import APIRouter, Request, status
from typing import List
from src.models.books import Books, UpdateBooks


import src.rules.books as books


router = APIRouter(prefix="/books",
    tags=["Books"])

@router.post("/", response_description="Create a book", status_code=status.HTTP_201_CREATED, response_model=Books)
def create_book(request: Request, book: Books):
    return books.create_book(request, book)


@router.put("/{id}", response_description="Update a book", response_model=Books)
def update_book(request: Request, id: str, book: UpdateBooks):
    return books.update_book(request, id, book)

@router.get("/", response_description="List all books", response_model=List[Books])
def list_books(request: Request):
    return books.list_books(request, 100)


@router.get("/{id}/", response_description="List books by id", response_model=Books)
def list_books_by_id(request: Request, id: str):
    return books.list_books_by_id(request, id)


@router.get("/{id}/{author}/", response_description="List books by authors", response_model=List[Books])
def list_books_by_author(request: Request, author: str):
    return books.list_books_by_author(request, author)


@router.delete("/{id}", response_description="Delete a book")
def delete_book(request: Request, id: str):
    return books.delete_book(request, id)