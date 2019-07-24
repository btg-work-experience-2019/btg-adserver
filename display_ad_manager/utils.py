"""
1.convert the string into a list
2.every value in the list must start with 'document.write()'
"""


def converter(lines):
    x = lines.split()
    lines2 = []
    for i in x:
        lines2.append("\"document.write(%s)\"" % i)
        
    return lines2
