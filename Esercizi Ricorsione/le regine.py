"""
Esercizi Ricorsione
 Disponi N regine in una scacchiera NxN
"""


class Leregine(object):

    def __init__(self, n):
        self.N = n
        self.colonne = list()
        for i in range(n):
            self.colonne.append(None)
        self.dispozizioni = []  # tutte le possibili disposizioni delle N Regine
        self.disponi()

    def __str__(self):
        stra = '%s Disposizioni possibili %s:\n' % (len(self.dispozizioni), self.N)

        # for colonna in self.dispozizioni:
        #  stra += str(colonna)+'\n'
        return stra

        # Idee per sviluppare un problema che si ripete: immagino di essere a metà soluzione
        # soluzione parziale passo-1 + un passo  -> passo +1 etc fino alla FINE
        # colonna fino a riga i-1 +  riga i  --> svilupporighe successive

    def disponi(self, riga=0):

        def okposition(riga, colonna):
            for nr in range(1, riga + 1):
                if self.colonne[riga - nr] in (colonna - nr, colonna, colonna + nr):
                    return False
            return True

        if riga == self.N:
            self.dispozizioni.append(self.colonne.copy())

        else:
            # step 1 riga i  =  una delle previsioni fatte + previsioni successive
            for colonna in range(self.N):
                if okposition(riga, colonna):
                    self.colonne[riga] = colonna
                    self.disponi(riga + 1)
        return


[print(Leregine(x)) for x in range(3, 9)]
