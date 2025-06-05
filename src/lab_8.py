import csv

class Graph:
    def __init__(self):
        self.graph = {}
        self.sources = []
        self.sinks = []
    def add_edge(self, u, v, capacity):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}

        if v in self.graph[u]:
            self.graph[u][v] += capacity
        else:
            self.graph[u][v] = capacity

        if u not in self.graph[v]:
            self.graph[v][u] = 0

    def bfs(self, source, sink, parent):
        visited = set()
        queue = [source]
        visited.add(source)

        while queue:
            u = queue.pop(0)
            for v in self.graph.get(u, {}):
                if v not in visited and self.graph[u][v] > 0:
                    parent[v] = u
                    if v == sink:
                        return True
                    visited.add(v)
                    queue.append(v)
        return False

    def edmonds_karp(self, source, sink):
        parent = {}
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

    def max_total_flow(self):
        super_source = "super_source"
        super_sink = "super_sink"

        for f in self.sources:
            self.add_edge(super_source, f, float('inf'))
        for s in self.sinks:
            self.add_edge(s, super_sink, float('inf'))

        return self.edmonds_karp(super_source, super_sink)


def load_graph_from_csv(file_path):
    g = Graph()
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)

        g.sources = [f.strip() for f in next(reader)]
        g.sinks = [s.strip() for s in next(reader)]

        for row in reader:
            if len(row) < 3 or not all(row):  
                continue
            u, v, c = row[0].strip(), row[1].strip(), int(row[2].strip())
            g.add_edge(u, v, c)
           
 
    


    return g


if __name__ == "__main__":
    graph = load_graph_from_csv("src/roads.csv")
    result = graph.max_total_flow()
    print(f"Максимальна кількість автомобілів, які зможуть проїхати протягом дня з ферм до магазинів: {result}")
    
