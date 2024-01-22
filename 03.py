import matplotlib.pyplot as plt
import networkx as nx


def print_table(distances, visited):
    # Верхній рядок таблиці
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)

    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)

        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")


def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    unvisited = list(graph.nodes)
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda node: distances[node])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph[current_vertex]:
            distance = distances[current_vertex] + graph[current_vertex][neighbor]["weight"]
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

        # Вивід таблиці після кожного кроку
        print_table(distances, visited)

    return distances


if __name__ == "__main__":

    # Виклик функції для вершини A
    G = nx.Graph()
    G.add_edges_from([(0, 1, {"weight":2}), (0, 2, {"weight":3}), (0, 4, {"weight":10}), (1, 2, {"weight":2}), (1, 3, {"weight":1}), (1, 4, {"weight":6}), (2, 3, {"weight":1}), (3, 4, {"weight":5}), (4, 5, {"weight":3})])

    dijkstra(G, 0)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()