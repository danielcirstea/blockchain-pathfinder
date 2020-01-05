from graphviz import Digraph
import csv

with open('../input_data/graph3.csv') as f:
    result = [{k: v for k, v in row.items()}
              for row in csv.DictReader(f, skipinitialspace=True)]

dot = Digraph(comment='Transaction graph', node_attr={'color': 'lightblue2', 'style': 'filled'})
for item in result[:40]:
    dot.node(item['from'][-5:], label=item['from'][-5:])
    dot.edge(item['from'][-5:], item['to'][-5:], label=item['to'][-5:])
    dot.attr(ranksep='3')

dot.render('output/graph.gv', view=True)
