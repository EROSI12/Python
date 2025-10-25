from fastapi import APIRouter, HTTPException, status
from typing import List
from models.recipe import Recipe, RecipeCreate
from database import get_db_connection


router = APIRouter()

def category_exists(category_id: int) -> bool:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM category WHERE id = ?", (category_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

@router.get("/recipes/", response_model=List[Recipe])
def get_recipes():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, description, category_id FROM recipe")
    recipes = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row["id"],
            "title": row["title"],
            "description": row["description"],
            "category_id": row["category_id"]
        }
        for row in recipes
    ]

@router.get("/recipes/{recipe_id}", response_model=Recipe)
def get_recipe(recipe_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, description, category_id FROM recipe WHERE id = ?", (recipe_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Recipe not found")

    return {
        "id": row["id"],
        "title": row["title"],
        "description": row["description"],
        "category_id": row["category_id"]
    }

@router.post("/recipes/", response_model=Recipe)
def create_recipe(recipe: RecipeCreate):
    if recipe.category_id and not category_exists(recipe.category_id):
        raise HTTPException(status_code=400, detail="Category does not exist")

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO recipe (title, description, category_id) VALUES (?, ?, ?)",
            (recipe.title, recipe.description, recipe.category_id)
        )
        conn.commit()
        recipe_id = cursor.lastrowid
        return Recipe(id=recipe_id, **recipe.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Recipe creation failed: {e}")
    finally:
        conn.close()

@router.put("/recipes/{recipe_id}", response_model=Recipe)
def update_recipe(recipe_id: int, recipe: RecipeCreate):
    if recipe.category_id and not category_exists(recipe.category_id):
        raise HTTPException(status_code=400, detail="Category does not exist")
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE recipe SET title = ?, description = ?, category_id = ? WHERE id = ? ingredients=? , instructions=?, cuisine=?, difficulty=?,    ",
        (recipe.name, recipe.diescription, recipe.ingredients, recipe.instrutions, recipe.cuisine, recipe.difficulty,
         recipe.category_id)
    )
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Recipe not found")
    conn.commit()
    conn.close()
    return Recipe(id=recipe_id, **recipe.dict())

@router.post("/recipes/", response_model=dict)
def create_recipes(recipe: RecipeCreate):
    if not category_exists(recipe.category_id):
        raise  HTTPException(status_code=400, detail="Category does not exits")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO recipes (name, description, ingredients, instructions, cuisine ,difficulty, category_id) VALUES (?,?,?,?,?,?,?)",(recipe.name, recipe.diescription, recipe.ingredients, recipe.instrutions, recipe.cuisine, recipe.difficulty, recipe.category_id)
    )

    conn.commit()
    recipe_id= cursor.lastrowid
    conn.close()
    return Recipe(id=recipe_id, name=recipe_name, description=recipe_description, ingredients=recipe.ingredients,
                  instrutions=recipe.instrutions, cuisine=recipe.cuisine, difficulty=recipe.difficulty, category_id=recipe.category_id)


@router.delete("/recipes/{recipe_id}", response_model=dict)
def delete_recipe(recipe_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.exec()
