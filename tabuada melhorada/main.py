# Desafio 049 em CursoemVideo

number_chosen = int(input("What number do you want to know the multiplication table? (from one to ten) "))

for t in range(1, 11):
    print(f"{number_chosen} x {t} = {number_chosen * t}")