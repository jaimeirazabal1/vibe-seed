from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from src.modules.analyzer.best_price import find_opportunities, get_best_prices

router = APIRouter()
templates = Jinja2Templates(directory="src/web/templates")


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    buy, sell = await get_best_prices(10)
    opps = await find_opportunities(0.3)
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "buy_prices": buy,
        "sell_prices": sell,
        "opportunities": opps,
    })
