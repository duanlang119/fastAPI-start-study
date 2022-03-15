from fastapi import FastAPI,Header,Body,Form

app= FastAPI()

@app.get("/users/{id}")
def users(id):
    """获取所有用户信息"""
    return {"msg":"Get all users","id":id}

@app.get("/projects")
def projects(id,token=Header(None)):
    """获取信息，问好类型"""
    return {"msg":"Get all users","id":id,"token":token}

@app.post("/body")
def body(data=Body(None)):
    """获取body"""
    return {"msg":"Get all body info","data":data}

@app.post("/login")
def login(username=Form(None),password=Form(None)):
    """获取body"""
    return {"data": {"username":username, "password":password}}
