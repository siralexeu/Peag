# script pentru testul selectiei parintilor - selectia de tip SUS cu distributie fps cu sigma-scalare
import numpy as np
from FunctiiSelectii import *

import generare_init as gi
import matplotlib.pyplot as grafic
#pentru legenda - ajustare
import matplotlib.patches as mpatches

def fps(calitati):
    p=calitati.copy()/sum(calitati)
    # p = np.zeros(calitati.size)
    # suma=sum(calitati)
    # for i in range(calitati.size):
    # p[i]=calitati[i]/suma
    n=len(calitati)
    q=p.copy()
    for i in range(1,n):
        q[i]=q[i-1]+p[i]
    return q

def ruleta(populatie,calitati,dim,probabilitate):
    parinti=populatie.copy()
    calitati_p=calitati.copy()
    q=probabilitate(calitati)
    for i in range(dim):
        raspuns=np.random.uniform(0,1)
        k=0
        while q[k]<raspuns:
            k+=1
        parinti[i]=populatie[k].copy()
        calitati_p[i]=calitati[k]
    return parinti,calitati_p


def sigma_fps(calitati):
    medie=np.mean(calitati)
    variatie=np.std(calitati)
    n=len(calitati)
    sigma=[max(calitati[i]-medie-2*variatie,0) for i in range(n)]
    if sum(sigma)>0:
        q=fps(sigma)
    else:
        q=fps(calitati)
    return q
def sus(populatie,calitati,dim,probabilitate):
    parinti=populatie.copy()
    calitati_p=calitati.copy()
    q=probabilitate(calitati)
    raspuns = np.random.uniform(0, 1/dim)
    i,k=0,0
    while i<dim:
        while raspuns<q[k]:
            parinti[i]=populatie[k].copy()
            calitati_p[i]=calitati[k]
            i+=1
            raspuns+=1/dim
        k+=1
    return parinti,calitati_p

#generarea aleatoare a unei populatii
dim=12
p,v,n=gi.gen("costuri.txt",dim)
# calculul parintilor si calitatii acestora utilizand selectia SUS cu FPS cu sigma-scalare
parinti,valori=ruleta(p,v,dim,fps)


x=range(dim)
grafic.plot(x,v,"go",markersize=16)
grafic.plot(x,valori,"ro",markersize=10)
red_patch = mpatches.Patch(color='red', label='Calitatile parintilor')
green_patch = mpatches.Patch(color='green', label='Calitatile populatiei curente')
grafic.legend(handles=[red_patch,green_patch])
grafic.show()