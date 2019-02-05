
class UndirectedGraph:
    # Use an adjacency list representation
    # uses a key, which is the node id in an integer value
    # and also has a value, which is a Node object which contains a hashset of neighbors
    def __init__(self):
        self.nodes = {} # dictionary with key as the nodeID and the value as the Node object

    # This function checks if the nodeID is in the dict, and if it is not, then we add a Node Object
    def addNode(self, nodeID):
        if(nodeID not in self.nodes):
            n = Node(nodeID)
            self.nodes[nodeID] = n

    def updateNeighbor(self, nodeID, neighborID):
        self.addNode(nodeID)
        self.addNode(neighborID)
        self.nodes[nodeID].addNeighbor(neighborID)
        self.nodes[neighborID].addNeighbor(nodeID)

    def getGraph(self):
        return self.nodes
    
    def getNode(self, nodeID):
        return self.nodes[nodeID]
    
class DirectedGraph:
    # Use an adjacency list representation
    def __init__(self):
        self.nodes = {} # dictionary with key as the nodeID and the value as the Node object

    def addNode(self, nodeID):
        if(nodeID not in self.nodes):
            n = Node(nodeID)
            self.nodes[nodeID] = n

    def updateNeighbor(self, nodeID, targetID):
        self.addNode(nodeID)
        self.addNode(targetID)
        self.nodes[nodeID].addNeighbor(targetID)

    def getGraph(self):
        return self.nodes
    
    def getNode(self, nodeID):
        return self.nodes[nodeID]

class Node:
    def __init__(self, nodeID):
        self.id = nodeID
        self.neighbors = set()

    def addNeighbor(self, neighborID):
        self.neighbors.add(neighborID)
    
    def getNeighbors(self):
        return self.neighbors
    
    def getID(self):
        return self.id
    