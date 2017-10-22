# Graphs: set of nodes and set of edges
# write algorith that gives us all the arcs of the graph (one direction pointing to one node)

class MyGraph:
    def __init__(self):
        # directed graph
        self.graph = {'A': ['B', 'C'],
                      'B': ['C', 'D'],
                      'C': ['D'],
                      'D': ['C'],
                      'E': ['F'],
                      'F': ['C']
        }

        # undirected graph 
        # self.graph = = [
        #     {'A', 'B'},
        #     {'A', 'C'}
        # ]
    
    def arcs(self):
        arcs = []
        for key in self.graph:
            for value in self.graph[key]:
                arcs.append((key, value))
        return arcs

g = MyGraph()
print(g.graph)
print(g.arcs())
