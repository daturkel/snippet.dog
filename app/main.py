from typing import Optional

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from fastapi import FastAPI
from starlette.responses import FileResponse, JSONResponse
from starlette.staticfiles import StaticFiles

from formatters import ModHtmlFormatter
from models import RenderRequest
from rules import get_line_no_rule, get_baseline_rule


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def index():
    return FileResponse("./static/index.html")


@app.post("/render")
async def render(request: RenderRequest):
    lexer = get_lexer_by_name(request.language)
    linespans = "highlight-line" if request.line_no_type else ""
    formatter = ModHtmlFormatter(
        style=request.style, wrapcode=True, linespans=linespans
    )
    results = highlight(request.code, lexer, formatter)
    styles = get_baseline_rule(True, False) + formatter.get_style_defs([".highlight"])
    if request.line_no_type:
        line_no_color = formatter.class2style["c"][0].split(" ")[1]
        line_no_rule = get_line_no_rule(line_no_color, request.line_no_type)
        styles = line_no_rule + styles
    return {"results": results, "styles": styles}
