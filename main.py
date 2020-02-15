from pydantic import BaseModel
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from fastapi import FastAPI
from starlette.responses import FileResponse, JSONResponse
from starlette.staticfiles import StaticFiles


class RenderRequest(BaseModel):
    code: str
    language: str
    style: str = "default"


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    return FileResponse("./static/index.html")


@app.post("/render")
async def render(request: RenderRequest):
    lexer = get_lexer_by_name(request.language)
    formatter = HtmlFormatter(style=request.style, wrapcode=True)
    results = highlight(request.code, lexer, formatter)
    styles = formatter.get_style_defs(['.highlight'])
    return {"results": results, "styles": styles}
