import re

def getData(fileName):
    f = open(fileName, "r")
    content = f.read()
    graph = re.findall(r"^(\d+) (\d+) (\d+)$", content, re.MULTILINE)
    graph = {int(a):(int(b),int(c)) for a,b,c in graph}

    return graph