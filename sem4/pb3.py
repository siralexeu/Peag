import numpy as np

def fitness(x):
    return 1 + np.sin(2*x[0] - x[2]) + (x[1] * x[3])**(1/3)

def generare_populatie(dim):
    populatie = np.zeros((dim, 4))
    for i in range(dim):
        populatie[i] = np.random.uniform([-1, 0, 0, 0], [1, 0.2, 1, 5])
    return populatie

def mutatie_fluaj(populatie, pm):
    t = 0.6
    sigma = t ** (1/3)
    dim, _ = populatie.shape
    pop_mutata = np.zeros_like(populatie)
    for i in range(dim):
        for j in range(4):
            if np.random.uniform(0, 1) < pm:
                pop_mutata[i, j] = populatie[i, j] + np.random.normal(0, sigma)
            else:
                pop_mutata[i, j] = populatie[i, j]
    return pop_mutata

if __name__ == "__main__":
    dim = 10
    pm = 0.1

    populatie = generare_populatie(dim)
    print("Populatia initiala:\n", populatie)

    populatie_mutata = mutatie_fluaj(populatie, pm)
    print("Populatia dupa mutatie:\n", populatie_mutata)
