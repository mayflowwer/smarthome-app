from pydantic import BaseModel, Field, validator
from typing import Optional

class HouseCreate(BaseModel):
    id: int
    user_id: int
    created_at: str
    updated_at: str

class HouseUpdate(BaseModel):
    pass

class HouseResponse(BaseModel):
    id: int
    user_id: int

    