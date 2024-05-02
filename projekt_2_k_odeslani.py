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

# dva listy - hadani_list - 4-místné číslo hádajícího
# hadane_cislo - číslo, generované systémem  
pocet_pokusu, bulls = 0, 0
pocet_cislic = 1
hadani_list = []
hodnoceni = ["amazing.", "average.", "not so good."]

# 1. náhodná číslice nezačíná 0, pak vytvoření listu s 1. číslicí
cislice_1 = random.randint(1,9)     
hadane_cislo = [cislice_1]

# generování náhodného čísla, cyklus, aby číslice byly jedinečné
while True:
    cislice = random.randint(0,9)
    if cislice not in hadane_cislo:
        hadane_cislo.append(cislice)
        pocet_cislic += 1
    else:
        continue
    if pocet_cislic == 4:
        break

# žádost o zadání 1. čísla hráčem, začíná běžet čas
print("Enter a number:")
print("-" * 47)
start_time = time.time()

# cyklus, který běží, dokud bulls nejsou 4
while bulls != 4:
    hadani_list = []
    duplicita, cows, bulls = 0, 0, 0    
    pocet_pokusu +=1 
    hadani = input()
    print("-" * 47)  

# testování správného zadání čísla
    for a in hadani:
        if hadani.count(a) > 1:
            print("Duplicity.")
            print("-" * 47)
            duplicita = 1
            break
    if duplicita == 1:
        continue
    if hadani[0] == "0":
        print("Don´t start with 0.")
        print("-" * 47)
        continue
    if len(hadani) != 4:
        print("You don´t entered 4 numerals.")
        print("-" * 47)
        continue
    if not hadani.isnumeric():
        print("You entered non-numeric character.") 
        print("-" * 47)
        continue
    
# vytváření listu po kontrolách, z hadani na hadani_list
# počítání cows a bulls 
    for a in hadani:                     
        a = int(a)
        hadani_list.append(a)
        if a in hadane_cislo:
            cows += 1
    for a, b in zip(hadane_cislo, hadani_list):
        if a == b:
            bulls += 1
    cows = cows - bulls
    if cows == 0 and bulls == 4:
        break 
    if cows == 1:
        print("1 cow")
    else:
        print(cows, "cows")    
    if bulls == 1:
        print("1 bull")
    else:
        print(bulls, "bulls")
    print("-" * 47)

# konec hry, spočítání času, závěrečné tisky     
final_time = time.time()
real_time = final_time - start_time
real_time = round(real_time)
minuty = real_time//60
sekundy = real_time % 60
print("Correct, you've guessed the right number in ", pocet_pokusu, "guesses!")
print("Your game took", minuty, "minutes", sekundy, "seconds.")
if pocet_pokusu in range(1,11) and real_time < 121:
    print("That´s", hodnoceni[0])
elif pocet_pokusu in range(1,21) and real_time < 421:
    print("That´s", hodnoceni[1])
else:
    print("That´s", hodnoceni[2])
