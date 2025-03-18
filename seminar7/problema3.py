import random
import numpy as np

def fitness(x):
    suma = np.sum(x)
    return suma, suma % 2 == 0

def generare_populatie(dim):
    populatie = np.zeros([dim, 18], dtype="int")
    i = 0
    while i < dim:
        populatie[i, :17] = np.random.randint(0, 2, 17)
        populatie[i, 17], fezabil = fitness(populatie[i, :17])
        if fezabil:
            i += 1
    return populatie

def turneu(populatie, k):
    dim = populatie.shape[0]
    # dim=len(populatie)
    parinti = populatie.copy()
    for i in range(dim):
        pozitii = np.random.randint(0, dim, k)
        val_max = populatie[pozitii[0], 17]
        indice = pozitii[0]
        for j in range(1, k):
            if val_max < populatie[pozitii[j], 17]:
                val_max = populatie[pozitii[j], 17]
                indice = pozitii[j]
        parinti[i] = populatie[indice].copy()
    return parinti

if __name__ == "__main__":
    dim = 10
    populatie = generare_populatie(dim)
    print("Populatia generata\n", populatie)
    k = 3
    parinti = turneu(populatie, k)
    print("\nPopulatiea selectata\n", parinti)
