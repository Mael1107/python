#Desafio 017 em CursoemVideo
from math import sqrt

c1 = float(input("What is the length of the leg one?"))
c2 = float(input("What is the length of the leg two?"))

h = sqrt((pow(c1,2)) + (pow(c2,2)))

print(f"The hypotenuse of the right triangle is:{h:.2f}")

