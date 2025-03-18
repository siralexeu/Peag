import numpy as np

def fitness(x, y):
    return y * (np.sin(x - 2)) ** 2

def generare_populatie(dim):
    populatie = np.zeros((dim, 2), dtype=int)
    calitati = np.zeros(dim)
    for i in range(dim):
        populatie[i, 0] = np.random.randint(1, 1501)  # Generăm un x aleatoriu între 1 și 1500
        populatie[i, 1] = np.random.randint(-1, 2501)  # Generăm un y aleatoriu între -1 și 2500
        calitati[i] = fitness(populatie[i, 0], populatie[i, 1])
    return populatie, calitati

def incrucisare_multipunct(parinte1, parinte2):
    dim = len(parinte1)
    puncte_de_incrocisare = sorted(np.random.choice(np.arange(1, dim), size=3, replace=True))
    copil1 = np.zeros_like(parinte1)
    copil2 = np.zeros_like(parinte2)
    copil1[0:puncte_de_incrocisare[0]] = parinte1[0:puncte_de_incrocisare[0]]
    copil2[0:puncte_de_incrocisare[0]] = parinte2[0:puncte_de_incrocisare[0]]
    for j in range(1, 3):
        if j % 2 == 1:
            copil1[puncte_de_incrocisare[j-1]:puncte_de_incrocisare[j]] = parinte2[puncte_de_incrocisare[j-1]:puncte_de_incrocisare[j]]
            copil2[puncte_de_incrocisare[j-1]:puncte_de_incrocisare[j]] = parinte1[puncte_de_incrocisare[j-1]:puncte_de_incrocisare[j]]
        else:
            copil1[puncte_de_incrocisare[j-1]:puncte_de_incrocisare[j]] = parinte1[puncte_de_incrocisare[j-1]:puncte_de_incrocisare[j]]
            copil2[puncte_de_incrocisare[j-1]:puncte_de_incrocisare[j]] = parinte2[puncte_de_incrocisare[j-1]:puncte_de_incrocisare[j]]
    copil1[puncte_de_incrocisare[2]:] = parinte1[puncte_de_incrocisare[2]:]
    copil2[puncte_de_incrocisare[2]:] = parinte2[puncte_de_incrocisare[2]:]
    return copil1, copil2

def recombinare_multipunct(populatie, pc):
    dim, _ = populatie.shape
    popc = np.zeros_like(populatie)
    for i in range(0, dim, 2):
        if np.random.uniform(0, 1) < pc:
            popc[i], popc[i + 1] = incrucisare_multipunct(populatie[i], populatie[i + 1])
        else:
            popc[i] = populatie[i]
            popc[i + 1] = populatie[i + 1]
    return popc

if __name__ == "__main__":
    dim = 10
    pc = 0.8
    populatie, calitati = generare_populatie(dim)
    print("Populatia initiala:\n", populatie)
    print("Calitatile initiale:\n", calitati)

    populatie_recombinata = recombinare_multipunct(populatie, pc)
    print("\nPopulatia dupa recombinare:\n", populatie_recombinata)
