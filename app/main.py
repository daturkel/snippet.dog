import os
from typing import Optional

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from fastapi import FastAPI
from starlette.responses import FileResponse, JSONResponse
from starlette.staticfiles import StaticFiles

from formatters import ModHtmlFormatter
from models import RenderRequest
from rules import get_line_no_rule, get_baseline_rule
from utils import strip_extra_newlines


app = FastAPI()

if os.environ.get("SDENV") == "local":
    # this is a hacky workaround but it works:
    # mounting the whole static directory to "/" interferes with the "/render"
    # endpoint. mounting it to "/static" means that my links which assume
    # "static" is root don't work. so i just manually reroute the few important
    # requests to static files here.

    @app.get("/")
    def index():
        return FileResponse("./static/index.html")

    @app.get("/css/style.css")
    def style():
        return FileResponse("./static/css/style.css")

    @app.get("/js/snippetdog.js")
    def js():
        return FileResponse("./static/js/snippetdog.js")



@app.post("/render")
async def render(request: RenderRequest):
    lexer = get_lexer_by_name(request.language)
    linespans = "highlight-line" if request.line_no_type else ""
    code = strip_extra_newlines(request.code)
    formatter = ModHtmlFormatter(
        style=request.style, wrapcode=True, linespans=linespans
    )
    results = highlight(code, lexer, formatter)
    styles = get_baseline_rule() + formatter.get_style_defs([".highlight"])
    if request.line_no_type:
        comment_rule = formatter.class2style["c"][0]
        line_no_rule = get_line_no_rule(
            comment_rule, request.line_no_type, len(code.splitlines())
        )
        styles = line_no_rule + styles
    return {"results": results, "styles": styles}
