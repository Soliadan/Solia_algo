def find_min_depth_and_path(root, graph):
    queue = [[root, 1, [root]]]  # [вузол, глибина, шлях]
    head = 0

    while head < len(queue):
        node, depth, path = queue[head]
        head += 1

        # Якщо вузол — лист
        if node not in graph:
            return depth, path

        # Додаємо дітей у чергу з оновленим шляхом
        for child in graph[node]:
            queue.append([child, depth + 1, path + [child]])

    return 0, []


if __name__ == "main":
    # Зчитування з файлу
    with open("input.txt", "r") as file:
        lines = file.read().strip().split('\n')

    root = int(lines[0])
    edges = [list(map(int, line.split(','))) for line in lines[1:]]

    # Побудова графа
    graph = {}
    for parent, child in edges:
        if parent not in graph:
            graph[parent] = []
        graph[parent].append(child)

    # Пошук мінімальної глибини та шляху
    min_depth, path = find_min_depth_and_path(root, graph)

    # Виведення в консоль
    print(f"Мінімальна глибина дерева: {min_depth}")
    print(f"Шлях до першого знайденого листа: {path}")

    # Запис тільки глибини у файл
    with open("output.txt", "w") as file:
        file.write(str(min_depth))