# Missio japon impossible
import random
import time

counte = 5000

# Probleme1

print("Probleme numero 1")

num = random.randint(1, 51)
if num % 2 == 0:
    counte += 800
else:
    counte -= 2000
print('Fin du probleme numero 1')

# Probleme 2
print("Probleme numero 2")
liste = []
for i in range(1, 101):
    valeur = random.randint(10, 1001)
    liste.append(valeur)

# Valeurs inferieurs à 100
i = 0
nb_val = 0
while i < len(liste):
    if liste[1] < 100:
        nb_val += 1
    i += 1
if nb_val < 4:
    counte -= 2000
elif nb_val > 4:
    counte += 2500
print('Fin du probleme 2')

# Probleme 3
print("Probleme numero 3")

val_magique = liste[26]

if val_magique % 2 == 0:
    print("True!")
    counte += 1500
else:
    print("False!")
    counte -= 1500

print("Votre verdicte va tomber dans quelques instants")
time.sleep(3)

if counte < 5000:
    print("Saruma tu ne peux pas passer les vaccances d'été au Japon")
else:
    print("Saruma, tu as le visa pour passer les vaccances d'été au Japon avec pour"
          " argent de poche {} euro".format(counte))
