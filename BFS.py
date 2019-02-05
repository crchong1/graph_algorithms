class BFS:
    def __init__(self, graph):
        self.graph = graph
        self.queue = []
        self.visited = set()

    # perform BFS from a given start node
    def BFSFromNode(self, nodeID):
        self.visited.add(nodeID)    # mark as visited
        self.queue.append(nodeID)   # add first element to queue
        while self.queue != []:     # while queue is not empty
            self.visited.add(self.queue[0]) # mark as visited
            for p in self.graph[self.queue[0]].getNeighbors():
                if p not in self.visited:
                    self.queue.append(p)    # add the rest of the unseen neighbors to the end of the queue
            self.queue.pop(0)       # remove first element from queue
        