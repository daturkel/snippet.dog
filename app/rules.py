def get_baseline_rule():
    rule = ".highlight { border-radius: 3.25px; }\n"
    rule += ".highlight pre { font-family: monospace; font-size: 14px; overflow-x: auto; padding: 1.25rem 1.5rem; white-space: pre; word-wrap: normal; line-height: 1.5; "
    rule += "}\n"
    return rule


def get_line_no_rule(comment_rule: str, line_no_type: str, num_lines: int) -> str:
    num_digits = len(str(num_lines))
    line_no_color = _comment_rule_to_color(comment_rule)
    rule = (
        ".highlight { counter-reset: line; }\n"
        "/* from: https://codepen.io/elomatreb/pen/hbgxp */\n"
        ".highlight .highlight-line::before { "
        "counter-increment: line; "
        "content: counter(line); "
        "display: inline-block; "
        "padding: 0 .5em 0 0; "
        f"width: {num_digits}em; "
        f"color: {line_no_color} "
    )
    if num_digits > 1:
        rule += "text-align: right; "
    if line_no_type == "ruled":
        rule += f"border-right: 1px solid {line_no_color}" "margin-right: 0.5em;"
    rule += "}\n"
    return rule


def _comment_rule_to_color(comment_rule: str) -> str:
    words = comment_rule.split(" ")
    for word in words:
        if word[0] == "#":
            if word[-1] == ";":
                return word
            else:
                return word + "; "
    return "currentColor; "
