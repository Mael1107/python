# # Desafio 051 em CursoemVideo
import os

first_term = int(input("What is the first term of Arithmetic Progression? "))
os.system("cls" if os.name == "nt" else "clear")
reason = int(input("What is the reason of Arithmetic Progression? "))
os.system("cls" if os.name == "nt" else "clear")

print("The first ten numbers of arithmetic progression are: \n ")
for i in range(1, 11):
    term = first_term + ( i - 1) * reason
    print(term, end=" ")