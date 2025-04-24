from collections import deque

def check_distribution(cities, storages, pipelines):
    graph = {}

    # Побудова орієнтованого графа за списком активних газопроводів
    for start, end in pipelines:
        if start not in graph:
            graph[start] = []
        graph[start].append(end)

    result = []

    # Функція для визначення міст, до яких неможливо подати газ з поточного сховища
    def unreachable_cities(storage):
        visited = set()  # множина для відстеження відвіданих вузлів
        queue = deque([storage])  # черга для BFS

        while queue:
            node = queue.popleft()
            visited.add(node)  # позначаємо вузол як відвіданий
            # Проходимося по сусідах вузла
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

        # Повертаємо список міст, які не були досяжні з даного сховища
        return [city for city in cities if city not in visited]

    # Перевірка кожного сховища
    for storage in storages:
        unreachable = unreachable_cities(storage)
        if unreachable:
            result.append([storage, unreachable])  # Додаємо до результату, якщо є недосяжні міста

    return result  # Повертаємо список сховищ з недосяжними містами або пустий список

def main():
    # Тестові дані
    cities = ['Львів', 'Стрий', 'Долина']
    storages = ['Сховище_1', 'Сховище_2']
    pipelines = [['Львів', 'Стрий'], ['Долина', 'Львів'], ['Сховище_1', 'Долина']]

    # Виклик функції і виведення результату
    output = check_distribution(cities, storages, pipelines)
    print(output)
    
if __name__ == '__main__':
    main()