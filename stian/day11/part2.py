
with open("day11.txt") as f:
    v = {}
    for line in f.readlines():
        s, e = line.rstrip().split("-")
        v.setdefault(s, set()).add(e)
        v.setdefault(e, set()).add(s)

def traverse(parent, vertices, visited, revisited):
    if parent == "end":
        print("-".join(visited))
        return 1

    routes = 0
    for v in vertices[parent]:
        if v == "start": continue

        if not v.isupper() and v in visited:
            if len(revisited) == 0:
                routes += traverse(v, vertices, visited + [v], revisited + [v])
            continue

        routes += traverse(v, vertices, visited + [v], revisited)
    return routes 

print(traverse("start", v, ["start"], []))
