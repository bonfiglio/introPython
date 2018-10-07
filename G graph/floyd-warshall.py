# https://gist.github.com/mmas/7129128

try:
    import numpy as np
except ImportError:
    print("To use this module you need 'numpy' module")
    t = input('Install numpy? y/n: ')
    if t == 'y':
        import pip._internal

        t = input(pip.__version__)
        pip._internal.main(['install', 'numpy'])
        t = input('Installed numpy ')
        import numpy as np

        t = input(np.__version__)
        pass
    else:
        print('Some functionality can be unavailable.')


class FloydWarshall(object):
    # calcola il cammino minimo per tutte le coppie di un grafo pesato
    # nodes = []
    # edges = {}

    def __init__(self, filename):
        file_ = f = open(filename, "r", encoding="utf8")
        nodes = file_.read().splitlines()
        file_.close()
        self.get_graph(nodes)
        self.len_ = len(self.nodes)
        self.create_fw_matrix()

    def get_graph(self, nodes):
        self.nodes = []
        self.edges = {}
        for node in nodes[:]:
            [k, v] = node.split()
            if k in self.edges.keys():
                self.edges[k].append(int(v))
            else:
                self.edges[k] = int(v)
                [t, c] = k.split('-')
                if t not in self.nodes:
                    self.nodes.append(t)
                if c not in self.nodes:
                    self.nodes.append(c)

    def create_fw_matrix(self):
        dist = [[(float('inf'), -1, " ")] * self.len_ for i in range(self.len_)]
        # pred = [[(-1," ")] * self.len_ for i in range(self.len_)]
        for i, t in enumerate(self.nodes):
            for j, c in enumerate(self.nodes):
                if t == c:
                    dist[i][j] = (0, -1, " ")
                else:
                    if t + '-' + c in self.edges.keys():
                        dist[i][j] = (self.edges[t + '-' + c], i, t + '-' + c)

        self.matrix = dist
        self.print_matrix()

        for k in range(self.len_):
            for i in range(self.len_):
                for j in range(self.len_):
                    if dist[i][j][0] > (dist[i][k][0] + dist[k][j][0]):
                        dist[i][j] = (dist[i][k][0] + dist[k][j][0], dist[k][j][1], dist[i][k][2] + "." + dist[k][j][2])
        self.matrix = dist
        self.print_matrix()
        self.matrix = pred
        self.print_matrix()

    def print_matrix(self):
        r = '   '
        for i, row in enumerate(self.matrix):
            print(self.nodes[i], row)
            r += self.nodes[i] + '  '
        print(r)


if __name__ == '__main__':
    mygrafo = FloydWarshall("grafo.txt")
    # mygrafo.print_matrix()

    # Si comincia col ricavare la matrice di adiacenza del grafo (infinito dove non vi è collegamento)
    graph = np.array(
        [[0, 10, 20, 30, 0, 0], [0, 0, 0, 0, 0, 7], [0, 0, 0, 0, 0, 5], [0, 0, 0, 0, 10, 0], [2, 0, 0, 0, 0, 4],
         [0, 5, 7, 0, 6, 0]])

    v = len(graph)
    # Inizializzazione  int [0..n, 0..n] dist; for i := 1 to n for j := 1 to n dist[i][j] := Weight(i,j) //peso dell'arco da i a j

    # path reconstruction matrix
    p = np.zeros(graph.shape)
    for i in range(0, v):
        for j in range(0, v):
            p[i, j] = i
            if (i != j and graph[i, j] == 0):
                p[i, j] = -30000
                graph[i, j] = 30000  # set zeros to any large number which is bigger then the longest way

    for k in range(0, v):
        for i in range(0, v):
            for j in range(0, v):
                if graph[i, j] > graph[i, k] + graph[k, j]:
                    graph[i, j] = graph[i, k] + graph[k, j]
                    p[i, j] = p[k, j]

    # show p matrix
    print(p)


    def ConstructPath(p, i, j):
        i, j = int(i), int(j)
        if (i == j):
            print(i, )
        elif (p[i, j] == -30000):
            print(i, '-', j)
        else:
            ConstructPath(p, i, p[i, j]);
            print(j, )


    # reconstruct the path from 0 to 4
    ConstructPath(p, 0, 4)
