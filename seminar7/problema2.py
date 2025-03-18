import random
import numpy as np

def fitness(p, castig):
    return np.dot(p, castig)

def generare_populatie(dim, castig):
    n = len(castig)
    populatie = np.zeros([dim, n], dtype="int")
    calitati = np.zeros(dim)
    for i in range(dim):
        populatie[i] = np.random.permutation(n)
        calitati[i] = fitness(populatie[i], castig)
    return populatie, calitati

def incrucisare_uniforma(parinte1, parinte2):
    dim = len(parinte1)
    punct_de_incrocisare = np.random.randint(0, dim)  # Alegem un punct de încrucișare
    copil1 = np.zeros_like(parinte1)
    copil2 = np.zeros_like(parinte2)
    for i in range(dim):
        if i < punct_de_incrocisare:
            copil1[i] = parinte1[i]
            copil2[i] = parinte2[i]
        else:
            copil1[i] = parinte2[i]
            copil2[i] = parinte1[i]
    return copil1, copil2

def recombinare_uniforma(populatie, pc):
    dim = populatie.shape[0]
    popc = populatie.copy()
    for i in range(0, dim, 2):
        if random.random() < pc:
            popc[i], popc[i + 1] = incrucisare_uniforma(populatie[i], populatie[i + 1])
        else:
            popc[i] = populatie[i]
            popc[i + 1] = populatie[i + 1]
    return popc

if __name__ == "__main__":
    castig = [2, 5, 12, 10, 2, 3, 1]
    dim = 12
    populatie, calitati = generare_populatie(dim, castig)
    print("Populatia\n", populatie)
    print("Calitati\n", calitati)
    pc = 0.8
    popc = recombinare_uniforma(populatie, pc)
    print("\nPopulatia dupa recombinare\n", popc)
    print("Calitati dupa recombinare\n", [fitness(p, castig) for p in popc])