# Desafio 050 em CursoemVideo
soma = 0

for x in range(1,7):
    integer = int(input("Enter a number: "))
    if integer % 2 == 0:
        soma += integer
print(f"The sum of the values, wich are even, typed is: {soma}")