from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app  = FastAPI()

@app.get("/" , response_class=HTMLResponse)
def index():
        return "<h1>Hello world</h1>"

@app.get("/piaic/")
def piaic():
    return {"organization": "piaic"}

@app.get("/ijlal/")
def ijlal():
    return {"Muhammad": "Khanzada"}