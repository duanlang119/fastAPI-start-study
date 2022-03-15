from fastapi import FastAPI

app= FastAPI()

# @app.post("/login")
# def login():
#     return {"msg":"login success! "}

@app.api_route("/login",methods=("GET","POST","PUT"))
def login():
    return {"msg":"login success! "}