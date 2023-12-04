import networkx as nx
import matplotlib.pyplot as plt
import numpy

class Player:
    def __init__(self, Name, GameCount):
        self.Name = Name
        self.GameCount = GameCount


G = nx.Graph()
G = nx.read_edgelist("List.csv", delimiter=",", data=[("weight", int)]) 



elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]
esize = [(u,v,d) for (u, v, d) in G.edges(data=True)]

NamesList = []
GamesCount = []
PlayerList = []
for item in esize:
    if item[0] not in NamesList:
        NamesList.append(str(item[0]))
    if item[1] not in NamesList:
        NamesList.append(str(item[1]))

for Name in NamesList:
    PlayerList.append(Player(Name, 0))

for item in esize:
    for Person in PlayerList:
        if item[0] == Person.Name:
            Person.GameCount += int(item[2]['weight'])
        if item[1] == Person.Name:
            Person.GameCount += int(item[2]['weight'])

sizes = []
for item in PlayerList:
    sizes.append(item.GameCount)

sizes = [x//10 for x in sizes]
pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=sizes, node_color="c", linewidths=0)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=1)
nx.draw_networkx_edges(G, pos, edgelist=esmall, width=6, alpha=1, edge_color="m", style="solid",)

# node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", font_color="k", font_weight="bold")

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()