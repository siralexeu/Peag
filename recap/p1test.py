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

if __name__=="__main__":
    castig=castig=[2,5,12,10,2,3,1]
    dim=10
    populatie,calitati=generare_populatie(dim,castig)
    print("Populatia\n",populatie)
    print("Calitati\n",calitati)















