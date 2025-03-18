import numpy as np
import matplotlib.pyplot as plt

def fitness(p):
    n = len(p)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if p[i] == j and p[j] == i:
                count += 1
    return count

def generare_populatie(dim, n):
    populatie = np.zeros((dim, n), dtype=int)
    calitati = np.zeros(dim, dtype=int)
    for i in range(dim):
        populatie[i] = np.random.permutation(n)
        calitati[i] = fitness(populatie[i])
    return populatie, calitati

def mutatie_inserare(populatie, pm):
    dim, n = populatie.shape
    popm = populatie.copy()
    for i in range(dim):
        if np.random.uniform(0, 1) < pm:
            index1, index2 = np.random.choice(n, 2, replace=False)
            temp = popm[i, index1]
            if index1 < index2:
                popm[i, index1:index2] = popm[i, index1+1:index2+1]
                popm[i, index2] = temp
            else:
                popm[i, index2+1:index1+1] = popm[i, index2:index1]
                popm[i, index2] = temp
    return popm
if __name__ == "__main__":
    dim = 10
    n = 8
    pm = 0.1
    populatie, calitati = generare_populatie(dim, n)
    print("Populatia initiala:\n", populatie)
    print("Calitatile initiale:\n", calitati)

    populatie_mutata = mutatie_inserare(populatie, pm)
    print("\nPopulatia dupa mutatie:\n", populatie_mutata)
