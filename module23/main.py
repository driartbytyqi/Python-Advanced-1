from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

@app.post("/developer/")
def create_developer(developer: Developer):
    return {"message": "Developer createt successfully","developer": developer}

@app.post("/projects/")
def create_project(project: Project):
    return {"message": "Project created successfylly", "project": project}

@app.get("/projects/")
def get_projects():
    simple_projects = Project(
        title
    )



