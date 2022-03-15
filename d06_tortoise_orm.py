from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from tortoise.contrib.fastapi import register_tortoise

from dao.models import Todo

app= FastAPI()
template=Jinja2Templates("pages")

register_tortoise(app,db_url="sqlite://fastapi.db",
                  modules={"models":["dao.models"]},
                  generate_schemas=True,
                  add_exception_handlers=True,)


@app.get("/")
async def index(req:Request):
    todos= await Todo.all()
    return template.TemplateResponse("index.html",context={"request":req,"todos":todos})

@app.post("/todo")
async def todo(content=Form(None)):
    await Todo(content=content).save()
    return RedirectResponse("/",status_code=302)

@app.post("/search")
async def search(req:Request,keyword=Form(None)):
    search_results=await Todo.filter(content__icontains=keyword).all()
    return template.TemplateResponse("search_result.html",context={"request":req,"search_results":search_results})

