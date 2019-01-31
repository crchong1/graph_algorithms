class TopoSort:
    def __init__(self, graph):
        self.graph = graph
        self.topologicalOrdering = []
        self.visited = set()

    def topologicalSort(self):
        for key in self.graph:
            if(key not in self.visited):
                self.topologicalSortFromNode(key)
        self.topologicalOrdering.reverse()
        return self.topologicalOrdering


    def topoRecursiveHelper(self, nodeID):
        neighbors = self.graph[nodeID].getNeighbors()
        for n in neighbors:
            if n not in self.visited:
                self.visited.add(n)
                self.topoRecursiveHelper(n)
        self.topologicalOrdering.append(nodeID)

    def topologicalSortFromNode(self, startID):
        self.visited.add(startID)
        self.topoRecursiveHelper(startID)
        
        

        
