from pygments.formatters.html import HtmlFormatter

class ModHtmlFormatter(HtmlFormatter):
    """
    Basically the same as HtmlFormatter, except instead of wrapping each line in a span
    with id "{linespans}-{lineno}", it just wraps in a span with class "{linespans}"
    """

    def _wrap_linespans(self, inner):
        s = self.linespans
        for t, line in inner:
            if t:
                yield 1, f'<span class="{s}">{line}</span>'
            else:
                yield 0, line
