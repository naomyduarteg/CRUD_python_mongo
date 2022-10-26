
import uuid
from typing import Optional
from pydantic import BaseModel, Field


class UserAddress(BaseModel):
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    addr_name: str
    user_id: str 
    street: str 
    number: str
    city: str  
    state: str
    code : str 
    
    class Config:
        schema_extra = {
            "example": {
                "addr_name": "House",
                "user_id": "4815162342",
                "street": "Bablabla st",
                "number": "42",
                "city": "Blablacity",
                "state": "Blablastate",
                "code": "14350000"
            }
        }

class UpdateAddress(BaseModel):
    addr_name: Optional[str]
    street: Optional[str]
    number: Optional[str]
    city: Optional[str]  
    state: Optional[str]
    code : Optional[str]