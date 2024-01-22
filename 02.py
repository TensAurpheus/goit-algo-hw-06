from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited)

if __name__ == "__main__":
    graph = {
        0: [1, 2, 4],
        1: [0, 2, 3, 4],  # "A", "D", "E"],
        2: [0, 1, 3],
        3: [1, 2, 4],
        4: [0, 1, 3, 5],
        5: [4],
    }

    G = nx.Graph(graph)

    dfs_tree = nx.dfs_tree(G, 0)
    print('DFS:')
    dfs_recursive(graph, 0)
    print("")
    bfs_tree = nx.bfs_tree(G, 0)
    print('BFS:')
    bfs_recursive(graph, deque([0]))

    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw_networkx(G, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=16, font_weight="bold")
    plt.show()