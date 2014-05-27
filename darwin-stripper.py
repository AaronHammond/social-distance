import networkx as net
import matplotlib.pyplot as plt

import json
from pprint import pprint
with open('dataset.json') as data_file:    
    data = json.load(data_file)

def deleteIfPresent(key, node):
	if node.has_key(key):
		del node[key]

for node in data['nodes']:
	deleteIfPresent('betweenness_centrality', node)
	deleteIfPresent('birthplace', node)
	deleteIfPresent('colour', node)
	deleteIfPresent('date-of-birth', node)
	deleteIfPresent('domain', node)
	deleteIfPresent('mid', node)
	deleteIfPresent('nation', node)
	deleteIfPresent('occupation', node)
	deleteIfPresent('profession', node)
	deleteIfPresent('shortest_path_length', node)
	deleteIfPresent('wiki_id', node)
	deleteIfPresent('x', node)
	deleteIfPresent('y', node)
	deleteIfPresent('year_of_birth', node)
	deleteIfPresent('year_of_death', node)

for edge in data['edges']:
	deleteIfPresent('score', edge)

with open('stripped_data.json', 'wt') as out:
    pprint(data, stream=out)

pprint(data)