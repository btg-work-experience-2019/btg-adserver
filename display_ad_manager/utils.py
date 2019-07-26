


def converter(lines):
    x = lines.split("\n")
    lines2 = []
    for i in x:
        lines2.append('document.write("' + i.strip().replace('"','\\"') + '");')

    return "\n".join(lines2)
