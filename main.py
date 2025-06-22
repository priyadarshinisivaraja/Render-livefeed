from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def serve_index():
    with open("index.html", "r") as f:
        return f.read()
