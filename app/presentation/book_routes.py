from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import SessionLocal
from app.domain.entities.book_entity import BookEntity
from app.data.repositories.book_repository_impl import BookRepositoryImpl
from app.application.book_usecases import BookUseCases

router = APIRouter(prefix="/books", tags=["Books"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_usecase(db: Session = Depends(get_db)):
    repository = BookRepositoryImpl(db)
    return BookUseCases(repository)

@router.get("/", response_model=List[BookEntity])
def get_books(usecase: BookUseCases = Depends(get_usecase)):
    return usecase.get_books()

@router.get("/{book_id}", response_model=BookEntity)
def get_book(book_id: int, usecase: BookUseCases = Depends(get_usecase)):
    book = usecase.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=BookEntity)
def create_book(book: BookEntity, usecase: BookUseCases = Depends(get_usecase)):
    return usecase.create_book(book)

@router.put("/{book_id}", response_model=BookEntity)
def update_book(book_id: int, book: BookEntity, usecase: BookUseCases = Depends(get_usecase)):
    updated = usecase.update_book(book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@router.delete("/{book_id}")
def delete_book(book_id: int, usecase: BookUseCases = Depends(get_usecase)):
    success = usecase.delete_book(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"deleted": True}


### revisar