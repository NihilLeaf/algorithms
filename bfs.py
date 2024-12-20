from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def isMangoSeller(name):
  return name[-1].lower() == 'm'


def search(name):
  searchQueue = deque()
  searchQueue += graph[name]
  verified = []
  while searchQueue:
    person = searchQueue.popleft()
    if person not in searchQueue:
      if isMangoSeller(person):
        print(f"{person} is a mango seller")
        return True
      else:
        searchQueue += graph[person]
        verified.append(person)
  return False

search('you')