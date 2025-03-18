import numpy as np


def gray_code(num):
    """
    Returnează codul Gray al unui număr.

    Args:
    num (int): Numărul întreg de convertit în codul Gray.

    Returns:
    int: Codul Gray corespunzător numărului dat.
    """
    return num ^ (num >> 1)


def generare_populatie(dim):
    """
    Generează aleator o populație folosind codificarea Gray.

    Args:
    dim (int): Dimensiunea populației.

    Returns:
    numpy.ndarray: Un șir numpy care reprezintă populația generată.
    """
    populatie = np.zeros((dim,), dtype=int)
    for i in range(dim):
        populatie[i] = gray_code(
            np.random.randint(1, 351))  # Generăm un număr aleatoriu între 1 și 350 și aplicăm codificarea Gray
    return populatie


def procedura_genitor(pop1, pop2):
    """
    Aplică procedura de tip GENITOR asupra celor două populații.

    Args:
    pop1 (numpy.ndarray): Prima populație.
    pop2 (numpy.ndarray): A doua populație.

    Returns:
    numpy.ndarray: Populația rezultată din procedura GENITOR.
    """
    dim = len(pop1)
    pop_noua = np.zeros_like(pop1)
    for i in range(dim):
        if i % 2 == 0:
            pop_noua[i] = pop1[i]
        else:
            pop_noua[i] = pop2[i]
    return pop_noua


if __name__ == "__main__":
    dim = 10  # Dimensiunea populației
    pop1 = generare_populatie(dim)
    pop2 = generare_populatie(dim)
    print("Populația 1 generată:")
    print(pop1)
    print("\nPopulația 2 generată:")
    print(pop2)

    pop_noua = procedura_genitor(pop1, pop2)
    print("\nPopulația nouă obținută prin procedura GENITOR:")
    print(pop_noua)
