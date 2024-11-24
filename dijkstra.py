graph = {
    'start': {
        'a': 6,
        'b': 2,
    },
    'a': {
        'end': 1,
    },
    'b': {
        'a': 3,
        'end': 5,
    },
    'end': {}
}

infinity = float('inf')

costs = {
  'a': 6,
  'b': 2,
  'end': infinity
}

parent = {
  'a': 'start',
  'b': 'start',
  'end': None
}

processed = []

def nodeCheaper(costs):
  costCheaper = float('inf')
  nodeCheaper = None
  for node in costs:
    cost = costs[node]
    if cost < costCheaper and node not in processed:
      costCheaper = cost
      nodeCheaper = node
  return nodeCheaper

node = nodeCheaper(costs)
while node is not None:
  cost = costs[node]
  neighbors = graph[node]
  for n in neighbors.keys():
    newCost = cost + neighbors[n]
    if costs[n] > newCost:
      costs[n] = newCost
      parent[n] = node
  processed.append(node)
  node = nodeCheaper(costs)

print({'costs': costs, 'parent': parent})
