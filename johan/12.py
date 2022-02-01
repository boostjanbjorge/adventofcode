from collections import defaultdict
import get

problem_input = get.input(12)

edges = defaultdict(set)

for line in problem_input:
    endpoints = set(line.split("-"))
    for node in endpoints:
        edges[node] |= endpoints - {node}


def paths(start, end, visited=set(), allow_twice=False):
    if start == "end":
        yield "end"
    elif start == end:
        yield end

    else:
        for next_node in edges[start].difference(
            {"start"}.union(visited if not allow_twice else set())
        ):
            next_allow_twice = allow_twice
            if next_node.islower():
                next_visited = visited.union({next_node})
                if next_node in visited:
                    next_allow_twice = False
            else:
                next_visited = visited

            yield from (
                f"{start},{tail}"
                for tail in paths(next_node, end, next_visited, next_allow_twice)
            )


print(len(list(paths("start", "end", allow_twice=False))))
print(len(list(paths("start", "end", allow_twice=True))))
