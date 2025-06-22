from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def serve_index():
    with open("index.html", "r") as f:
        return f.read()

# You should also have:
# - /upload to receive image from ESP32
# - /latest to serve latest image
