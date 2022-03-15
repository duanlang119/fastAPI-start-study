import pathlib

import pytest
from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

app= FastAPI()
template=Jinja2Templates("pages")

@app.get("/")
def index(req:Request):
    current_dir = pathlib.Path(__file__).resolve().parent
    workspace = current_dir / 'workspace'
    projects = [
        {"name": project_path.name,
         "url":f'http://localhost:8000/projects/{project_path.name}',
         "path":project_path
        }
        for project_path in workspace.iterdir()
    ]
    return template.TemplateResponse("jenkins_home.html",context={"request":req,"projects":projects})

@app.get("/projects/{name}")
def project_run(name):
    pytest.main([f"workspace/{name}"])
    return RedirectResponse("/", status_code=302)
