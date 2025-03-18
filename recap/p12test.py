import numpy as np

def fitness(p):
    calitate = 0
    for i in range(len(p) - 1):
        if p[i] == i + 1 and p[i + 1] == i + 2:
            calitate += 1
    return calitate

def generare_populatie(dim, k):
    populatie = np.zeros((dim, k), dtype=int)
    calitati = np.zeros(dim)
    for i in range(dim):
        permutare = np.random.permutation(k) + 1  # Generăm o permutare aleatoare de la 1 la k
        populatie[i] = permutare
        calitati[i] = fitness(permutare)
    return populatie, calitati



if __name__=="__main__":
    dim = 10
    p = 5
    populatie, calitati = generare_populatie(dim, p)
    print("Populație generată:\n", populatie)
    print("Calități corespunzătoare:\n", calitati)

