# Desafio 019 em CursoemVideo
from random import choice

a1 = input("Enter the first student name: ")
a2 = input("Enter the secind student name: ")
a3 = input("Enter the third student name: ")
a4 = input("Enter the fourth student name: ")

s = [a1, a2, a3, a4]

c = choice(s)

print(f"The luck student was: {c}")