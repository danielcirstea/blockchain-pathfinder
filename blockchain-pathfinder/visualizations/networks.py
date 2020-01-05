import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('raw_data/graph3.csv')
g = nx.DiGraph()
color_map = []
g.add_edges_from(df[['from', 'to']][:1000].values)
for node in g:
    if node == df['from'][0]:
        color_map.append('red')
    else:
        color_map.append('#00b4d9')
fig = plt.figure()
nx.draw(g, node_color=color_map)
plt.show()
