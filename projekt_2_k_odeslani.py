"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Stanislav Weissmann
email: stana.ws@gmail.com
discord: Standa W.
"""

print("\nHi there!")   
print("-" * 47)
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print("-" * 47)

import random
import time

def generovani_cisla():
    """
    Generuje náhodné 4-místné číslo, první číslice z intervalu 1 až 9,
    další číslice z intervalu 0 až 9. Všechny číslice jsou jedinečné.
    """
    cislice_1 = random.randint(1,9)     
    hadane_cislo = [cislice_1]
    pocet_cislic = 1
    while pocet_cislic != 4 :
        cislice = random.randint(0,9)
        if cislice not in hadane_cislo:
            hadane_cislo.append(cislice)
            pocet_cislic += 1
    return hadane_cislo

def testovani_zadani(hadani):
    """
    Testuje, zda je číslo "řádné" či nikoliv (duplicita, jiný počet znaků
    než čtyři, nenumerické znaky, začíná 0). Pokud není řádné - bude mít
    proměnná radne_cislo hodnotu False.
    """
    duplicita = 0
    radne_cislo = True
    for a in hadani:
        if hadani.count(a) > 1:
            print("Duplicity.")           
            duplicita = 1
            break
    if duplicita == 1:
        radne_cislo = False
    if hadani[0] == "0":
        print("Don´t start with 0.")
        radne_cislo = False
    if len(hadani) != 4:
        print("You don´t entered 4 numerals.")
        radne_cislo = False
    if not hadani.isnumeric():
        print("You entered non-numeric character.") 
        radne_cislo = False
    return radne_cislo

def tisky_cows_bulls(cows, bulls):     
    print("1 cow") if cows == 1 else print(cows, "cows")    
    print("1 bull") if bulls == 1 else print(bulls, "bulls")

def vyhodnoceni():
    hodnoceni = ["amazing.", "average.", "not so good."]
    if pocet_pokusu in range(1,11) and real_time < 121:
        print("That´s", hodnoceni[0])
    elif pocet_pokusu in range(1,21) and real_time < 421:
        print("That´s", hodnoceni[1])
    else:
        print("That´s", hodnoceni[2])

# Následuje program po hlavičce, importu knihoven
# a definici vlastních funkcí.

# dva listy - hadani_list - 4-místné číslo hádajícího
# hadane_cislo - číslo, generované systémem  

hadane_cislo = generovani_cisla()           # fce - generování náhodného čísla

# žádost o zadání 1. čísla hráčem, začíná běžet čas
print("Enter a number:")
start_time = time.time()

# cyklus, který běží, dokud bulls nejsou 4
bulls = 0
pocet_pokusu = 0
while bulls != 4:
    hadani_list = []
    cows, bulls = 0, 0   
    pocet_pokusu +=1 
    print("-" * 47) 
    hadani = input()
    radne_cislo = testovani_zadani(hadani)    # fce - je správně zadané číslo?

# pokud je radne_cislo False, návrat k zadávání čísla jinak:
# vytváření listu z hadani na hadani_list
# a počítání cows a bulls 
    if not radne_cislo:
        continue
    for a in hadani:                     
        a = int(a)
        hadani_list.append(a)
    for a, b in zip(hadane_cislo, hadani_list):
        if a == b:
            bulls += 1
        if b in hadane_cislo:
            cows += 1
    
# testování konce hry, break nyní, aby se netiskly počty cows a bulls
# nutné odečít bulls od cows
    cows = cows - bulls          
    if bulls == 4:
        break 
# pokud není konec hry, tisky cows a bulls
    tisky_cows_bulls(cows, bulls)              # fce - tisk počtu cows a bulls 

# konec hry, spočítání času, závěrečné tisky   
final_time = time.time()
real_time = final_time - start_time
real_time = round(real_time)
minuty = real_time//60
sekundy = real_time % 60
print(f"Correct, you've guessed the right number in {pocet_pokusu} guesses!")
print(f"Your game took {minuty} minutes {sekundy} seconds.")
vyhodnoceni()                                       # fce - vyhodnocení
