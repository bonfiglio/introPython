class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Vertici(object):
    def __init__(self, val):
        self.valore = val
        self.inDegree = 0
        self.outDegree = 0
        self.outList = []

    def __str__(self):
        return str(self.valore) + '(in:' + str(self.inDegree) + '/out:' + str(self.outDegree) + '->' + str(
            self.outList) + ' )\n'


class Graph(object):

    def __init__(self):
        self.AdjacencyMatrix = []
        # A two-dimensional matrix, in which the rows represent source vertices
        # and columns represent destination vertices.
        # Data on edges and vertices must be stored externally.
        # Only the cost for one edge can be stored between each pair of vertices.
        v = int(input('Enter the number of vertices:'))
        self.AdjacencyList = {}
        for riga in range(v):
            self.AdjacencyList[riga + 1] = Vertici(riga + 1)
            colonne = []
            for colonna in range(v):
                colonne.append(0)
            self.AdjacencyMatrix.append(colonne)
        e = int(input('Enter the number of edges: '))
        count = 0
        while count < e:
            da = int(input('Enter the edges <from> :'))
            ad = int(input('Enter the edges <to> :'))
            self.makeEdge(da, ad, 1)
            count += 1

    def __str__(self):
        """This method is run when Python tries
        to cast the object to a string. Return
        this string when using print(), etc.
        """
        tmp = 'The adjacency matrix for the given graph is: \n'
        for x in self.AdjacencyMatrix:
            tmp += '\t' + str(x) + '\n'
        tmp = bcolors.OKGREEN + str(tmp) + bcolors.ENDC
        for x in self.AdjacencyList:
            tmp += '\t' + str(self.AdjacencyList[x])
        return tmp

    def makeEdge(self, da, ad, valore):
        self.AdjacencyMatrix[da - 1][ad - 1] = valore
        self.AdjacencyList[da].outDegree += 1
        self.AdjacencyList[ad].inDegree += 1
        self.AdjacencyList[da].outList.append(ad)

    def helper(self, ver, visited, recStack):
        if ver in self.AdjacencyList[ver].outList:
            return True
        if ver in recStack:
            return True
        recStack.append(ver)
        for i in self.AdjacencyList[ver].outList:
            if i not in visited:
                if self.helper(i, visited, recStack):
                    return True
                recStack.pop()
        visited.append(ver)
        return False

    def isCyclic(self):
        visited = []  # array to track vertices already visited
        recStack = []  # array to track vertices in recursion stack of the traversal.
        # for(int i = 0;i<V;i++)
        # visited[i]=false, recStack[i]=false;

        # initialize all vertices as not visited and not recursed
        for u in self.AdjacencyList:  # Iteratively checks if every vertices have been visited
            if u not in visited:
                # checks if the DFS tree from the vertex contains a cycle
                if self.helper(u, visited, recStack):
                    return True
        return False

    def cyclic(self):
        """Return True if the directed graph has a cycle.
        The graph must be represented as a dictionary mapping vertices to
        iterables of neighbouring vertices. For example:

        >>> cyclic({1: (2,), 2: (3,), 3: (1,)})
        True
        >>> cyclic({1: (2,), 2: (3,), 3: (4,)})
        False

        """
        visited = set()
        path = [object()]
        path_set = set(path)
        stack = [iter(self.AdjacencyList)]
        while stack:
            for v in stack[-1]:
                if v in path_set:
                    return True
                elif v not in visited:
                    visited.add(v)
                    path.append(v)
                    path_set.add(v)
                    stack.append(iter(self.AdjacencyList[v].outList))
                    break
            else:
                path_set.remove(path.pop())
                stack.pop()
        return False

grafo = Graph()
# print(grafo.isCyclic())
print(grafo.cyclic() == grafo.isCyclic())
