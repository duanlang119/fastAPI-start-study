from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

app= FastAPI()
template=Jinja2Templates("pages")
todos=["写日记","看电影","玩游戏"]
@app.get("/")
def index(req:Request):

    return template.TemplateResponse("index.html",context={"request":req,"todos":todos})

@app.post("/todo")
def todo(todo=Form(None)):
    todos.insert(0,todo)
    return RedirectResponse("/",status_code=302)
