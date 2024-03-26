import os

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from func import get_graphs
app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_path = os.path.join(BASE_DIR, 'static')
templates_path = os.path.join(BASE_DIR, 'templates')
app.mount("/static", StaticFiles(directory=static_path), name="static")


templates = Jinja2Templates(directory=templates_path)



@app.get("/", response_class=HTMLResponse)
async def root(request: Request) -> HTMLResponse:
    graphs = get_graphs()
    return templates.TemplateResponse(
        name="index.html", request=request, context={"graphs": graphs}
    )