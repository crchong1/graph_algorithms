class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.stack = []
        self.visited = set()

    def DFSFromNode(self, nodeID):
        #mark that nodeID has been visited
        self.visited.add(nodeID)
        # get neighbor of nodeID
        neighbors_of_nodeID=self.graph[nodeID].getNeighbors()
        #make sure neighbors don't contain the node we have visited
        effective_neighbors=neighbors_of_nodeID-self.visited
        #add effective neighbors into the begining of the stack
        for i in effective_neighbors:
            self.stack.insert(0,i)
        while len(self.stack)>0:
            #get the node start next
            start_next=self.stack[0]
            #delete this node from stack
            del self.stack[0]
            #search from node 'start_next'
            self.DFSFromNode(start_next)