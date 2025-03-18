import numpy as np
from FunctiiCrossoverIndivizi import crossover_PMX
import matplotlib.pyplot as grafic


#f. obiectiv
def foTSP(p,c):
    n=p.size
    val = 0
    for i in range(n - 1):
        val = val + c[p[i]][p[i+1]]
    val = val+c[p[0]][p[n-1]]
    return 100/val


#genereaza populatia initiala
#I:
# fc - numele fisierului costurilor
# dim - numarul de indivizi din populatie
#E: pop,val - populatia initiala si vectorul valorilor
#  pentru testul crossover si matricea c
def gen(fc,dim):
    #citeste datele din fisierul nxn al costurilor
    c=np.genfromtxt(fc)
    #n=dimensiunea problemei
    n = len(c)
    #defineste o variabila ndarray dimx(n+1) cu toate elementele 0
    pop=np.zeros((dim,n),dtype=int)
    val=np.zeros(dim,dtype=float)
    for i in range(dim):
        #genereaza candidatul permutare cu n elemente
        pop[i] = np.random.permutation(n)
        # evalueaza candidat
        val[i] = foTSP(pop[i,:n],c)
    return pop, val,c


#crossover pe populatia de parinti pop, de dimensiune dimxn
# I:   pop,valori, ca in functia de generare
#     c - datele problemei
#     pc- probabilitatea de crossover
#E: po,val - populatia copiilor, insotita de calitati
# este implementata recombinarea asexuata
def crossover_populatie(pop,valori,c,pc):
    # initializeaza populatia de copii, po, cu matricea cu elementele 0
    dim=pop.shape[0]
    n=pop.shape[1]
    po=np.zeros((dim,n),dtype=int)
    # initializeaza valorile populatiei de copii, val, cu matricea cu elementele 0
    val=np.zeros(dim,dtype=float)
    #populatia este parcursa astfel incat sunt selectati aleator cate 2 indivizi - matricea este accesata dupa o permutare a multimii de linii 0,2,...,dim-1
    poz=np.random.permutation(dim)
    #sau populatia este parcursa astfel incat sunt selectati 2 indivizi consecutivi
    #poz=range(dim) #- pentru pastrarea ordinii
    for i in range(0,dim-1,2):
        #selecteaza parintii
        x = pop[poz[i]]
        y = pop[poz[i+1]]
        r = np.random.uniform(0,1)
        if r<=pc:
            # crossover x cu y - PMX - potrivit pentru probleme cu dependenta de adiacenta
            c1,c2 = crossover_PMX(x,y,n)
            v1=foTSP(c1,c)
            v2=foTSP(c2,c)
        else:
            # recombinare asexuata
            c1 = x.copy()
            c2 = y.copy()
            v1=valori[poz[i]]
            v2=valori[poz[i+1]]
        #copiaza rezultatul in populatia urmasilor
        po[i] = c1.copy()
        po[i+1] = c2.copy()
        val[i]=v1
        val[i+1]=v2
    valori=[valori[poz[i]] for i in range(dim)]
    figureaza(valori,val,dim)
    return po, val

def figureaza(valori,val,dim):
    x = range(dim)
    grafic.plot(x, valori, "go", markersize=14,label="Calitate parinti")
    grafic.plot(x, val, "ro", markersize=10,label="Calitate copii")
    grafic.legend(loc="upper left")
    grafic.xlabel("Indicii indivizilor")
    grafic.ylabel("Calitatile indivizilor")
    grafic.show()

if __name__=="__main__":
    p,v,c=gen("costuri.txt",20)
    o,vo=crossover_populatie(p,v,c,0.8)

