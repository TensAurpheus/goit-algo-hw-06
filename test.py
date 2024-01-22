import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([(0, 1, {"weight":2}), (0, 2, {"weight":3}), (0, 4, {"weight":10}), (1, 2, {"weight":2}), (1, 3, {"weight":1}), (1, 4, {"weight":6}), (2, 3, {"weight":1}), (3, 4, {"weight":5}), (4, 5, {"weight":3})])

# dijkstra(G, 0)
print(G[1])
pos = nx.spring_layout(G, seed=66)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()