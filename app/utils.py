def strip_extra_newlines(text: str) -> str:
    i = 0
    for line in reversed(text.splitlines()):
        if line.isspace() or line == "":
            i += 1
        else:
            break
    if i == 0:
        return text
    else:
        return "\n".join(text.splitlines()[:-i])
