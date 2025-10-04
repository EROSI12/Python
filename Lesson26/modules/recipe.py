from pydantic import BaseModel
from Typing import Optional

class RecipeBase(BaseModel):
    name: str
    description: Optional[str] = None
    ingredients: str
    instruction: str
    cuisine: str
    difficulty: str
    category_id: Optinal[int] = None

    class RecipeCreate(RecipeBase):
        pass

    class Recipe(RecipeBase):
        id: int
