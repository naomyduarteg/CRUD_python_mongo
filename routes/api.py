from fastapi import APIRouter
from src.endpoints import books, users, addresses

router = APIRouter()
router.include_router(books.router)
router.include_router(users.router)
router.include_router(addresses.router)
