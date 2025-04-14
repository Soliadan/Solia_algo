import heapq

class Node:
    def __init__(self, value, priority):
        self.value = value  # IP address
        self.priority = priority  # number of visits

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"{self.value} ({self.priority} visits)"

class PriorityQueue:
    def __init__(self, max_size=10):
        self.heap = []  
        self.max_size = max_size
        self.nodes = {}  

    def insert_or_update(self, value, priority):
        
        if value in self.nodes:
            node = self.nodes[value]
            node.priority += priority
            heapq.heapify(self.heap)  
        else:
            node = Node(value, priority)
            self.nodes[value] = node
            heapq.heappush(self.heap, node)

        
        if len(self.heap) > self.max_size:
            self.delete_min()

    def delete_min(self):
        
        if not self.heap:
            return None
        min_node = heapq.heappop(self.heap)
        del self.nodes[min_node.value]
        return min_node

    def get_sorted_list(self):
   
        return sorted(self.heap, key=lambda node: node.priority)

def main():
    pq = PriorityQueue()

    while True:
        print("\nМенюшечка:")
        print("Додати новий IP")
        print("Збільшити кількість відвідувань")
        print("Видалити IP з найменшою кількістю")
        print("Показати всі IP")
        print("Вийти")

        choice = input("Ваш вибір: ").strip().lower()

        if choice in ["додати", "додати новий ip"]:
            ip = input("Введіть IP адресу: ")
            count = int(input("Кількість відвідувань: "))
            pq.insert_or_update(ip, count)
            print(f"{ip} оновлено.")
        elif choice in ["збільшити", "збільшити кількість відвідувань"]:
            ip = input("Введіть IP адресу: ")
            add = int(input("Збільшити на: "))
            pq.insert_or_update(ip, add)
            print(f"{ip} оновлено")
        elif choice in ["видалити", "видалити ip"]:
            removed = pq.delete_min()
            if removed:
                print(f"Видалено: {removed}")
            else:
                print("Список пустий")
        elif choice in ["показати", "показати всі ip"]:
            sorted_list = pq.get_sorted_list()
            if sorted_list:
                print("\nСписок IP за кількістю відвідувань (зростаємо):")
                for node in sorted_list:
                    print(node)
            else:
                print("Список пустий")
        elif choice in ["вийти"]:
            print("Папа")
            break
        else:
            print("Все погано ,давай вася по новій")

if __name__ == "__main__":
    main()
