class TopoSort:
    def __init__(self, graph):
        self.graph = graph
        self.topologicalOrdering = []
        self.visited = set()

    # run a topological sort on the entire graph
    def topologicalSort(self):
        # make sure we see every node in the graph
        for key in self.graph:
            if(key not in self.visited):
                self.topologicalSortFromNode(key)
        # reverse the list and return it
        self.topologicalOrdering.reverse()
        return self.topologicalOrdering

    def topologicalSortFromNode(self, startID):
        self.visited.add(startID)
        self.topoRecursiveHelper(startID)

    # recursive helper function
    def topoRecursiveHelper(self, nodeID):
        neighbors = self.graph[nodeID].getNeighbors()
        for n in neighbors:
            if n not in self.visited:
                self.visited.add(n) # add to visited set
                self.topoRecursiveHelper(n)
        # when we pop back up the recursion stack, add to topological sorting
        self.topologicalOrdering.append(nodeID)

        

        
