


def converter(lines):
    x = lines.split("\n")
    lines2 = []
    for i in x:
        lines2.append("document.write('" + i + "');")

    return "\n".join(lines2)
