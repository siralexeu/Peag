import random
import time
import keyboard

# Definirea simbolurilor și a câștigurilor corespunzătoare
symbols = ['Cireasa', 'Lamaie', 'Portocala', 'Strugure', 'Clopot', 'Bar', '7']
winning_combinations = {
    ('Cireasa', 'Cireasa', 'Cireasa'): 50,
    ('Lamaie', 'Lamaie', 'Lamaie'): 20,
    ('Portocala', 'Portocala', 'Portocala'): 30,
    ('Strugure', 'Strugure', 'Strugure'): 40,
    ('Clopot', 'Clopot', 'Clopot'): 100,
    ('Bar', 'Bar', 'Bar'): 200,
    ('7', '7', '7'): 777
}

def spin_wheel():
    """Funcție pentru generarea unei combinații de simboluri."""
    return [random.choice(symbols) for _ in range(3)]

def display_slot_machine(combination):
    """Funcție pentru afișarea combinației de simboluri."""
    print("\n-------------------")
    print("|   {}   |   {}   |   {}   |".format(*combination))
    print("-------------------")

def check_winning(combination):
    """Funcție pentru verificarea dacă combinația este câștigătoare și calcularea câștigului."""
    combination_tuple = tuple(combination)
    if combination_tuple in winning_combinations:
        return winning_combinations[combination_tuple]
    else:
        return 0

def main():
    print("Bine ai venit la jocul de pacanele!")
    print("Apasă bara de spațiu pentru a începe jocul...")

    while True:
        # Așteptarea apăsării barei de spațiu pentru a începe jocul
        keyboard.wait('space')

        # Generare combinație de simboluri
        combination = spin_wheel()

        # Afisare combinație
        display_slot_machine(combination)

        # Verificare câștig și afișare mesaj corespunzător
        winnings = check_winning(combination)
        if winnings > 0:
            print("Felicitări! Ai câștigat {} puncte!".format(winnings))
        else:
            print("Nu ai câștigat nimic. Mai încearcă o dată!")

        print("\nApasă SPACE pentru a juca din nou...")

if __name__ == "__main__":
    main()
