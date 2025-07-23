# Desafio 028 em CursoemVideo
from random import choice
x = [0,1,2,3,4,5]
choice = choice(x)

number = int(input("Enter a number: "))

if choice == number:
    print("Congratulations, you got it right!!")
else:
    print("OHH, how bad luck!")


