import numpy as np

def fitness(x):
    return np.sum(x)

def generare_populatie(dim):
    populatie = np.random.randint(2, size=(dim, 7))  # Generăm populația aleatoriu cu valori 0 sau 1
    calitati = np.zeros(dim)
    for i in range(dim):
        calitati[i] = fitness(populatie[i])
    return populatie, calitati

def incrucisare_multipunct(p1, p2):
    dim = len(p1)
    puncte = sorted(np.random.choice(np.arange(1, dim), size=2, replace=False))
    copil = np.zeros(dim)
    copil[:puncte[0]] = p1[:puncte[0]]
    copil[puncte[0]:puncte[1]] = p2[puncte[0]:puncte[1]]
    copil[puncte[1]:] = p1[puncte[1]:]
    return copil


def recombinare_multipunct(populatie, calitati, pc):
    dim = len(populatie)
    popc = populatie.copy()
    calc = calitati.copy()
    for i in range(0, dim, 2):
        if np.random.uniform(0, 1) < pc:
            popc[i] = incrucisare_multipunct(populatie[i], populatie[i+1])
            popc[i+1] = incrucisare_multipunct(populatie[i], populatie[i+1])
            calc[i] = fitness(popc[i])
            calc[i+1] = fitness(popc[i+1])
        else:
            popc[i] = populatie[i]
            popc[i+1] = populatie[i+1]
            calc[i] = calitati[i]
            calc[i+1] = calitati[i+1]
    return popc, calc

if __name__ == "__main__":
    dim = 12
    pc = 0.3
    populatie, calitati = generare_populatie(dim)
    print("Populatia initiala:\n", populatie)
    print("Calitatile initiale:\n", calitati)

    populatie_recombinata, calitati_recombinate = recombinare_multipunct(populatie, calitati, pc)
    print("\nPopulatia dupa recombinare:\n", populatie_recombinata)
    print("Calitatile dupa recombinare:\n", calitati_recombinate)
