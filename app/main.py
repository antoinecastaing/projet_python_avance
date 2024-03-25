import os

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_path = os.path.join(BASE_DIR, 'static')

app.mount("/static", StaticFiles(directory=static_path), name="static")


templates = Jinja2Templates(directory="templates")

def get_all_graphs():
    graphs = []
    for file in os.listdir("static/graphs"):
        if file.endswith(".png"):
            graphs.append(file)
    return graphs


@app.get("/", response_class=HTMLResponse)
async def root(request: Request) -> HTMLResponse:
    graphs = get_all_graphs()
    return templates.TemplateResponse(
        name="index.html", request=request, context={"charts": graphs}
    )