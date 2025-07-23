# Desafio 028 em CursoemVideo
from random import choice
from time import sleep
x = [0,1,2,3,4,5]
pc = choice(x)

player = int(input("What number did I think of?: "))
print("Processing...")
sleep(1.5)
if pc == player:
    print("Congratulations, you got it right!!")
else:
    print("OHH, how bad luck!")


