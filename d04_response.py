from fastapi import FastAPI
from fastapi.responses import JSONResponse,HTMLResponse,FileResponse

app= FastAPI()

@app.get("/")
def users():
    html_content="""
    <html>
        <body>
        <p style="color:red">Hello world</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/users")
def users():
    """获取所有用户信息"""
    return JSONResponse(content={"msg":"Get all users"},
                        status_code=202,
                        headers={"a","b"})
@app.get("/avatar")
def users():
    """获取所有用户信息"""
    avatar='static/avantar.jpg'
    return FileResponse(path=avatar,filename='avatar.jpg')