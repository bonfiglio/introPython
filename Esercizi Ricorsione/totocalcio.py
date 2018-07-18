class Risultato():
    UNO = '1'
    DUE = '2'
    ICS = 'X'


class Previsione(object):  # 1 2 x
    def __init__(self, r1=None, r2=None, r3=None):

        self.risultati = set()
        if r1 is not None:
            self.risultati.add(r1)
        if r2 is not None:
            self.risultati.add(r2)
        if r3 is not None:
            self.risultati.add(r3)

    def __str__(self):
        str = 'Risultati -'
        # + str(self.risultati)
        for risultato in self.risultati:
            str += risultato + "-"
        return str


class Pronostico(object):

    def __init__(self, n):
        self.N = n
        self.previsioni = []
        self.colonne = []

    def add(self, p):
        if len(self.previsioni) < self.N:
            self.previsioni.append(p)
        # } else {
        # throw new IllegalStateException("Too many elements in Proonostico") ;

    def __str__(self):
        str = 'Pronostico: \n'
        for previsione in self.previsioni:
            str += previsione.__str__() + "\n"
        return str

    def sviluppoColonna(self):

        # PROBLEMA RICORSIVO
        self.sviluppoRiga('', 0)
        print(self.colonne)
        return
        # Idee per sviluppare un problema che si ripete: immagino di essere a metà soluzione
        # soluzione parziale passo-1 + un passo  -> passo +1 etc fino alla FINE
        # colonna fino a riga i-1 +  riga i  --> svilupporighe successive

    def sviluppoRiga(self, colonna, i):
        if i == self.N:
            self.colonne.append(colonna)
        else:
            # step 1 riga i  =  una delle previsioni fatte + previsioni successive
            for risultato in self.previsioni[i].risultati:
                self.sviluppoRiga(colonna + risultato, i + 1)
        return


p = Pronostico(4)

p.add(Previsione(Risultato.DUE, Risultato.ICS))
p.add(Previsione(Risultato.UNO))
p.add(Previsione(Risultato.UNO, Risultato.ICS, Risultato.DUE))
p.add(Previsione(Risultato.ICS))
p.add(Previsione(Risultato.UNO, Risultato.DUE))
p.add(Previsione(Risultato.UNO))
p.add(Previsione(Risultato.DUE, Risultato.ICS))
p.add(Previsione(Risultato.UNO))
p.add(Previsione(Risultato.UNO, Risultato.ICS, Risultato.DUE))
p.add(Previsione(Risultato.ICS))
p.add(Previsione(Risultato.UNO, Risultato.DUE))
p.add(Previsione(Risultato.UNO))
p.add(Previsione(Risultato.DUE, Risultato.ICS))
print(p)
p.sviluppoColonna()
