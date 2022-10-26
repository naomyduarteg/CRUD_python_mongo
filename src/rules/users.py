from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.users import User
from bson import ObjectId


def get_collection_users(request: Request):
  return request.app.database["users"]

def create_user(request: Request, user: User = Body(...)):
    user = jsonable_encoder(user)
    new_user = get_collection_users(request).insert_one(user)
    created_user = get_collection_users(request).find_one({"_id": new_user.inserted_id})
    return created_user


def list_users(request: Request, limit: int):
    users = list(get_collection_users(request).find(limit = limit))
    return users


def find_user(request: Request, id: str):
    if (user := get_collection_users(request).find_one({"_id": ObjectId(id)})):
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found!")


def delete_user(request: Request, id: str):
    deleted_user = get_collection_users(request).delete_one({"_id": ObjectId(id)})

    if deleted_user.deleted_count == 1:
        return f"User with id {id} deleted sucessfully"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found!")