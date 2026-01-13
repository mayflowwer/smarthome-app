from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class House(SQLModel, table=True):
    __tablename__ = "houses"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    created_at: str
    updated_at: str
    
    locations: List["Location"] = Relationship(back_populates="house")

class Location(SQLModel, table=True):
    __tablename__ = "locations"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    house_id: int = Field(foreign_key="houses.id")
    
    house: Optional[House] = Relationship(back_populates="locations")