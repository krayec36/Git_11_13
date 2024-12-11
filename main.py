import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

name = input("Podaj swoje imię... ")

clear_console()
print(f"Witaj {name}, twoje imię ma {len(name)} liter")