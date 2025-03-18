import numpy as np

def fitness(p,castig):
    return np.dot(p,castig)

def generare_populatie(dim,castig):
    n=len(castig)
    populatie=np.zeros([dim,n],dtype="int")
    calitati=np.zeros(dim)
    for i in range(dim):
        populatie[i]=np.random.permutation(n)
        calitati[i]=fitness(populatie[i],castig)
    return populatie,calitati

def mutatie_inv(p):
    r=p.copy()
    n=len(p)
    i=np.random.randint(0,n-1)
    j=np.random.randint(i+1,n)
    r[i:j+1]=[p[k] for k in range(j,i-1,-1)]
    return r

def mutatie_populatie(populatie,calitati,pm,castig):
    pop_mutat=populatie.copy()
    cal_mutat=calitati.copy()
    for i in range(dim):
        raspuns=np.random.uniform(0,1)
        if raspuns<pm:
            pop_mutat[i]=mutatie_inv(populatie[i])
            cal_mutat[i]=fitness(pop_mutat[i],castig)
    return pop_mutat,cal_mutat

if __name__=="__main__":
    castig=[2,5,12,10,2,3,1]
    dim=12
    populatie,calitati=generare_populatie(dim,castig)
    print("Populatia\n",populatie)
    print("Calitati\n",calitati)
    pm=0.3
    p_mutat,c_mutat=mutatie_populatie(populatie,calitati,pm,castig)
    print("Populatia dupa mutatie\n",p_mutat)
    print("Calitati dupa mutatie\n",c_mutat)
