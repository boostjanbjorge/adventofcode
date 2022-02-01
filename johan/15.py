import heapq
import get

problem_input = get.input(15)

matrix = [list(map(int, line)) for line in problem_input]
xmax = len(matrix)
ymax = len(matrix[0])


def next_nodes(coord):
    x, y = coord
    if x < xmax - 1:
        yield (x + 1, y)
    if y < ymax - 1:
        yield (x, y + 1)
    if x > 0:
        yield (x - 1, y)
    if y > 0:
        yield (x, y - 1)


def shortest(start, end):
    heap = [(0, start)]
    visited = set()

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        visited.add(current_node)
        if current_node == end:
            return current_distance

        for neighbor in next_nodes(current_node):
            if neighbor not in visited:
                x, y = neighbor
                weight = matrix[x][y]
                heapq.heappush(heap, (weight + current_distance, neighbor))
                visited.add(neighbor)


print(shortest((0, 0), (xmax - 1, ymax - 1)))

matrix = [[((matrix[x % xmax][y % ymax] + x // xmax + y // ymax) - 1) % 9 + 1 for y in range(5 * ymax)] for x in range(5 * xmax)]
xmax *= 5
ymax *= 5

print(shortest((0, 0), (xmax - 1, ymax - 1)))