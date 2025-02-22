from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Главная страница.

    Args:
        request (Request): Запрос от клиента.

    Returns:
        TemplateResponse: HTML-шаблон index.html.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/about/", response_class=HTMLResponse)
async def about(request: Request):
    """
    Страница "О сайте".

    Args:
        request (Request): Запрос от клиента.

    Returns:
        TemplateResponse: HTML-шаблон about.html.
    """
    return templates.TemplateResponse("about.html", {"request": request})
