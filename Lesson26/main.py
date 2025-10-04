from fasapi import FastApi
from routers import recipe, category
import os
from dotenv import load_dotenv
from database import get_db_connection

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI()

app.incloude_router(category.router)
app.incloude_router(recipe.router)

@app.on_event("startup")
def startup():
    conn - get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXIST categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT
    NAME TEXT UNIQUE NOT NULL 
    )
    ''')

    cursor.execute('''
      CREATE TABLE IF NOT EXIST categories(
      id INTEGER PRIMARY KEY AUTOINCREMENT
      NAME TEXT UNIQUE NOT NULL 
      description TEXT,
      ingredients TEXT,
      instruction TEXT,
      cuisine TEXT,
      difficulty TEXT,
      category_id INTEGER,
      FOREIGN KEY(category_id)  REFERENCES category (id)
      )
      ''')
    conn.commit()
    conn.close()

    @app.get('/')
    def read_root():
        return {"message": "FastAPI with SQLite project"}

