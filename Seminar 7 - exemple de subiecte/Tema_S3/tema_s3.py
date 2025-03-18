import numpy as np

def fitness(x):
    return sum(x), sum(x)%2==0

def cerinta_a(dim):
    populatie=np.zeros([dim,18])
    i=0
    while i<dim:
        populatie[i, :17]=np.random.randint(0,2,17)
        populatie[i,17],ok=fitness(populatie[i,:17])
        if ok:
            i+=1
    return populatie


def cerinta_b(populatie,k):
    dim=populatie.shape[0]
    parinti=populatie.copy()
    for i in range(dim):
        poz=np.random.randint(0,dim,k)
        #print(poz+1)
        ales=np.argmax(np.array([populatie[poz[j],17] for j in range(k)]))
        #print(populatie[poz[ales],17])
        # linia in care este calculat ales este echivalenta cu
        # ales=0
        # maxim=populatie[poz[0],17]
        # for j in range(1,k):
        #     if maxim<populatie[poz[j],17]:
        #         maxim=populatie[poz[j],17]
        #         ales=j
        parinti[i,:17]=populatie[poz[ales],:17].copy()
        parinti[i,17]=populatie[poz[ales],17]
    return parinti

if __name__=="__main__":
    dim=10
    populatie=cerinta_a(dim)
    print("Populatia initiala\n",populatie)
    parinti=cerinta_b(populatie,k=3)
    print("Populatia dupa turneu\n",parinti)
