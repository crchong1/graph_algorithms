from Graph import DirectedGraph, UndirectedGraph, Node

def main():
    g = UndirectedGraph()
    g.updateNeighbor(1,2)
    g.updateNeighbor(1,3)
    g.updateNeighbor(2,3)
    print(g.getGraph())

if __name__ == "__main__":
    main()