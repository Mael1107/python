# Desafio 031 em CursoemVideo

distance = int(input("How many miles have you traveled? "))

if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45

print(f"So, you will pay: R${price:.2f}")