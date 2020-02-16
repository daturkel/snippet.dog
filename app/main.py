from typing import Optional

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
    line_nos: Optional[str] = False
    line_no_start: int = 1


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    return FileResponse("./static/index.html")


@app.post("/render")
async def render(request: RenderRequest):
    lexer = get_lexer_by_name(request.language)
    formatter = HtmlFormatter(
        style=request.style,
        wrapcode=True,
        linenos=request.line_nos,
        linenostart=request.line_no_start,
    )
    results = highlight(request.code, lexer, formatter)
    styles = formatter.get_style_defs([".highlight"])
    if request.line_nos:
        line_no_rule_raw = formatter.class2style['c'][0].split(";")[0]
        line_no_rule = f".highlight .lineno {{ {line_no_rule_raw}; }} /* line numbers */\n"
        styles = line_no_rule + styles
    return {"results": results, "styles": styles}
