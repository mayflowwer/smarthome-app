from sqlmodel import SQLModel, Field

    
class Location(SQLModel):
    __tablename__ = "locations"

    id: int = Field(primary_key=True)
    name: str = Field(max_digits=100)