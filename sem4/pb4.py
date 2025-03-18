import numpy as np

def fitness(x1, x2, x3):
    return 1 + np.sin(2*x1 - x3) + np.cos(x2)

def generare_populatie(dim):
    populatie = np.random.uniform(low=[-1, 0, -2], high=[1, 1, 1], size=(dim, 3))
    merite = np.zeros(dim)
    for i in range(dim):
        merite[i] = fitness(*populatie[i])
    return populatie, merite

def recombinare_aritmetica_totala(parinte1, parinte2):
    alpha = np.random.uniform(low=0, high=1)
    copil = alpha * parinte1 + (1 - alpha) * parinte2
    return copil

def recombinare_populatie(populatie, pc):
    dim = len(populatie)
    popc = np.zeros_like(populatie)
    for i in range(0, dim, 2):
        if np.random.uniform(0, 1) < pc:
            popc[i] = recombinare_aritmetica_totala(populatie[i], populatie[i+1])
            popc[i+1] = recombinare_aritmetica_totala(populatie[i], populatie[i+1])
        else:
            popc[i] = populatie[i]
            popc[i+1] = populatie[i+1]
    return popc

if __name__ == "__main__":
    dim = 10
    pc = 0.8
    populatie, merite = generare_populatie(dim)
    print("Populatia initiala:\n", populatie)
    print("Meritele initiale:\n", merite)

    populatie_recombinata = recombinare_populatie(populatie, pc)
    print("\nPopulatia dupa recombinare:\n", populatie_recombinata)
    print("Meritele dupa recombinare:\n", np.array([fitness(*populatie_recombinata[i]) for i in range(dim)]))