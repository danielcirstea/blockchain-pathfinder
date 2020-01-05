import csv

with open('raw_data/graph9.csv') as f:
    a = [(line['from'], line['to']) for line in csv.DictReader(f, skipinitialspace=True)]

collection = {}
stack = []

for i, j in a:
    if i in collection.keys():
        collection[i].append(j)
    else:
        collection[i] = [j]
    if j not in collection.keys():
        collection[j] = []


def find_cycles(g):
    color = {v: 'white' for v in g}
    for v in g:
        if color[v] == 'white':
            dfs(g, v, color)
    return stack


def dfs(g, v, color):
    color[v] = 'gray'
    for w in g[v]:
        if color[w] == 'gray':
            stack.append((v, w))
        elif color[w] == 'white':
            dfs(g, w, color)
    color[v] = 'black'


result = find_cycles(collection)

for i in range(len(a)):
    if a[i] in result:
        x = list(a[i])
        x[1] = x[1] + '$'
        a[i] = tuple(x)

tree = []
for i, j in a:
    if len(j) > 0:
        tree.append({'from': i, 'to': j})

with open('input_data/graph9.csv', 'w', encoding='utf8', newline='') as output_file:
    fc = csv.DictWriter(output_file, fieldnames=tree[0].keys())
    fc.writeheader()
    fc.writerows(filter(all, tree))
