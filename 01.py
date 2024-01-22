import matplotlib.pyplot as plt
import networkx as nx

graph = {
    0: [1, 2, 4],
    1: [0, 2, 3, 4],  # "A", "D", "E"],
    2: [0, 1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3, 5],
    5: [4],
}

G = nx.Graph(graph)

def print_degrees(graph):
    print('Node degrees:')
    for node in graph:
        print(f"{node}: {len(graph[node])}")


if __name__ == '__main__':
    print('Nodes: ', G.number_of_nodes())
    print('Edges: ', G.number_of_edges())
    print('Degree of centrality: ', nx.degree_centrality(G))
    print('Closeness centrality: ', nx.closeness_centrality(G))
    print('Betweenness centrality: ', nx.degree_centrality(G))

    degrees = G.degree
    print('Node degrees:')
    for node in degrees:
        print(f"{node[0]}: {node[1]}")

    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G, seed=66)
    nx.draw_networkx(G, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=16, font_weight="bold")
    plt.show()