# Desafio 048 em CursoemVideo
soma = 0

for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        print(i, end=" ..")
        soma += i


print(f" \n\nThe sum of multiples of 3 between 1 and 500 is: {soma:,}".replace(",", "."))

