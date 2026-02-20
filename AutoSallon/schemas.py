from pydantic import BaseModel, Field


class CarCreate(BaseModel):
    brand: str = Field(min_length=2, max_length=100)
    model: str = Field(min_length=1, max_length=100)
    year: int = Field(ge=1980, le=2100)
    price: float = Field(gt=0)


class CarRead(CarCreate):
    id: int

    class Config:
        from_attributes = True
