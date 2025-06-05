from lab_8 import load_graph_from_csv

graph = load_graph_from_csv("roads.csv")
result = graph.max_total_flow()
print(f"Мак к-сть автомо, які зможуть проїхати протягом дня з ферм до магазинів: {result}")