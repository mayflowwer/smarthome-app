# models/location_model.py
from pydantic import BaseModel, Field
from typing import Optional

class LocationBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    description: Optional[str] = None

class LocationCreate(LocationBase):
    house_id: int = Field(..., gt=0)  # Обязательная связь с домом

class LocationUpdate(BaseModel):
    """Для обновления локации (PATCH) - все поля опциональны"""
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    latitude: Optional[float] = Field(None, ge=-90, le=90)
    longitude: Optional[float] = Field(None, ge=-180, le=180)
    description: Optional[str] = None
    house_id: Optional[int] = Field(None, gt=0)

class LocationResponse(LocationBase):
    """Для ответа клиенту"""
    id: int
    house_id: int
    
    class Config:
        from_attributes = True  # Для работы с ORM