def get_baseline_rule(round: bool, shadow: bool):
    rule = ""
    round_rule = "border-radius: 3.25px; "
    shadow_rule = "box-shadow: 0 2px 1px #777;"
    if round or shadow:
        rule = ".highlight { "
        if round:
            rule += round_rule
        if shadow:
            rule += shadow_rule
        rule += "}\n"
    rule += ".highlight pre { font-family: monospace; font-size: 14px; overflow-x: auto; padding: 1.25rem 1.5rem; white-space: pre; word-wrap: normal; line-height: 1.5; "
    rule += "}\n"
    return rule


def get_line_no_rule(line_no_color: str, line_no_type: str) -> str:
    rule = (
        ".highlight { counter-reset: line; }\n"
        "/* from: https://codepen.io/elomatreb/pen/hbgxp */\n"
        ".highlight .highlight-line::before { "
        "counter-increment: line; "
        "content: counter(line); "
        "display: inline-block; "
        "padding: 0 .5em 0 0; "
        f"color: {line_no_color}"
    )
    if line_no_type == "ruled":
        rule += f"border-right: 1px solid {line_no_color}" "margin-right: 0.5em;"
    rule += "}\n"
    return rule
