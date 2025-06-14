from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

@app.post("/developer")
def create_developer(developer: Developer):
    return {"message": "Developer createt successfully","developer":developer}

@app.post("/project")
def create_developer(project: Project):
    return {"message": "Developer createt successfully","Project":project}