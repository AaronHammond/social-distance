import networkx as net
import matplotlib.pyplot as plt

import json


def trim_degrees(g, degree=1):
	g2 = g.copy()
	d = net.degree(g2)
	for n in g2.nodes():
		if d[n]<=degree: 
			g2.remove_node(n)
			del node_labels[n]
	return g2

def bogardusWeight(relationship):
	if relationship == "parent" or relationship == "child":
		return 6.0
	if relationship == "spouse":
		return 5.0
	if relationship == "sibling":
		return 4.0
	if relationship == "family":
		return 3.5
	if relationship == "advisor" or relationship == "advisee":
		return 3.0
	if relationship == "peer":
		return 2.0
	if relationship == "correspondence":
		return 1.0


with open('dataset.json') as data_file:    
    data = json.load(data_file)

g = net.Graph()

node_labels = {}
for node in data['nodes']:
	g.add_node(node['individual_id'])
	node_labels[node['individual_id']] = node['name']
for edge in data['edges']:
	g.add_edge(edge['source'], edge['target'], weight=bogardusWeight(edge['relationship']))

core = trim_degrees(g, 5)
#core = trim_degrees(core, 5)
#core = trim_degrees(core, 5)
print len(core.nodes())
print max(net.degree(core).values())
print min(net.degree(core).values())
#print "laying out"
pos=net.spring_layout(core, scale=5.0)
print "done laying out"
net.draw(core, pos=pos, with_labels=False)
net.draw_networkx_labels(core, pos=pos,labels=node_labels, font_color='blue')

#plt.savefig('graph.pdf')
plt.show()
