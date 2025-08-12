# Desafio 055 em CursoemVideo
weights = []

for i in range(1,6):
    weight = float(input("Enter your weight: "))
    weights.append(weight)
print(f"The major weight is: {max(weights)}kg")
print(f"The minor weight is: {min(weights)}kg")
print(weights)


