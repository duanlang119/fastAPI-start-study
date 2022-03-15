import uvicorn
from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def index():
    """这是首页"""
    return "This is HomePage."

@app.get("/users")
def users():
    """获取所有用户信息"""
    return {"msg":"Get all users","code":201}

@app.get("/projects")
def projects():
    return ["项目1","项目11","项目11"]

if __name__ == '__main__':
    uvicorn.run(app)