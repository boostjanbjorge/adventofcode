
with open("day12.txt") as f:
    v = {}
    for line in f.readlines():
        s, e = line.rstrip().split("-")
        v.setdefault(s, set()).add(e)
        v.setdefault(e, set()).add(s)

def traverse(root="start", vertices={}, visited=[]):
    if root == "end":
        print("-".join(visited))
        return 1

    routes = 0
    for v in vertices[root]:
        if not v.isupper() and v in visited:
            continue

        path = visited.copy()
        path.append(v)

        routes += traverse(v, vertices, path)
    return routes 

print(traverse(vertices=v, visited=["start"]))
