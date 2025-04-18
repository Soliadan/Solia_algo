def find_min_depth_and_path(root, graph):
    queue = [[root, 1, [root]]]  
    head = 0

    while head < len(queue):
        node, depth, path = queue[head]
        head += 1

        if node not in graph:
            return depth, path

        for child in graph.get(node, []):
            queue.append([child, depth + 1, path + [child]])

    return 0, []


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.read().strip().split('\n')

    root = int(lines[0])
    edges = [list(map(int, line.split(','))) for line in lines[1:]]

    graph = {}
    for parent, child in edges:
        if parent not in graph:
            graph[parent] = []
        graph[parent].append(child)

    min_depth, path = find_min_depth_and_path(root, graph)

    print(f"Мінімальна глибина дерева: {min_depth}")
    print(f"Шлях: {' -> '.join(map(str, path))}")

    with open("output.txt", "w") as file:
        file.write(str(min_depth))
