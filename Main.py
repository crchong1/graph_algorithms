from Graph import DirectedGraph, UndirectedGraph, Node
from TopoSort import TopoSort
from BFS import BFS


def main():
    g = DirectedGraph()
    g.updateNeighbor(1,2)
    g.updateNeighbor(1,3)
    g.updateNeighbor(1,4)
    g.updateNeighbor(2,5)
    g.updateNeighbor(2,6)

    t = TopoSort(g.getGraph())
    print(t.topologicalSort())

if __name__ == "__main__":
    main()