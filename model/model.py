import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def buildGraph(self):
        allNodes = DAO.getAllObjects()
        self._grafo.add_nodes_from(allNodes)
        for n in allNodes:
            self._idMap[n.object_id] = n
        self.addEdges()
        return True

    def addEdges(self):
        allConnessioni = DAO.getAllConnessioni(self._idMap)
        for edge in allConnessioni:
            if self._grafo.has_edge(edge.obj1, edge.obj2):
                self._grafo[edge.obj1][edge.obj2]['weight'] += 1
            else:
                self._grafo.add_edge(edge.obj1, edge.obj2, weight=1)

    def checkId(self, idIn):
        for n in self._grafo.nodes:
            if n.object_id == idIn:
                return True
        else:
            return False

    def compConn(self, idIn):
        origine = None
        for n in self._grafo.nodes:
            if n.object_id == idIn:
                origine = n
        if origine is not None:
            compConn = nx.node_connected_component(self._grafo, origine)
            return len(list(compConn))

    def getNodes(self):
        return self._grafo.nodes

    def getEdges(self):
        return self._grafo.edges

    def printGraphDetails(self):
        return f"Il grafo ha {len(self._grafo.nodes)} nodi e {len(self._grafo.edges)}"
