import numpy as np

def fitness(x):
    return np.sum(x)

def generare_populatie(dim):
    populatie = np.random.randint(2, size=(dim, 7))  # Generăm populația aleatoriu cu valori 0 sau 1
    calitati = np.zeros(dim)
    for i in range(dim):
        calitati[i] = fitness(populatie[i])
    return populatie, calitati

if __name__=="__main__":
    dim=10
    populatie,calitati=generare_populatie(dim)
    print("Populatie\n",populatie)
    print("Populatie\n", calitati)






