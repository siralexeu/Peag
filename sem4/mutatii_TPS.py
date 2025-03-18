import numpy as np
import matplotlib.pyplot as grafic

def f_ob(p,C):
    n=C.shape[0]
    cost=C[p[n-1],p[0]]
    for i in range(n-1):
        cost+=C[p[i],p[i+1]]
    return 1/cost


def generare_pop(dim,C):
    n=C.shape[0]
    populatie=np.zeros([dim,n],dtype="int")
    calitati=np.zeros(dim)
    for i in range(dim):
        populatie[i]=np.random.permutation(n)
        calitati[i]=f_ob(populatie[i],C)
    grafic.plot([i for i in range(dim)],calitati,"ro",markersize=12)
    return populatie,calitati

def mutatie_inversiune(p):
    r=p.copy()
    n=p.size
    i=np.random.randint(0,n-1)
    j=np.random.randint(i+1,n)
    r[i:j+1]=[p[k] for k in range(j,i-1,-1)]
    return r

def mutatie_populatie(pop,cal,C,pm):
    dim=pop.shape[0]
    m_pop=pop.copy()
    m_cal=cal.copy()
    for i in range(dim):
        r=np.random.uniform(0,1)
        if r<=pm:
            individ_mutat=mutatie_inversiune(pop[i])
            m_pop[i]=individ_mutat
            m_cal[i]=f_ob(individ_mutat,C)
    grafic .plot([i for i in range(dim)],m_cal,"ko",markersize=8)
    return m_pop,m_cal


if __name__=="__main__":
    Costuri=np.genfromtxt("costuri.txt")
    dim=20
    pop,cal=generare_pop(dim,Costuri)
    pm=0.2
    pop,cal=mutatie_populatie(pop,cal,Costuri,pm)
    grafic.show()

