# Desafio 032 em CursoemVideo

n1 = int(input("Enter a first number: "))
n2 = int(input("Enter a second number: "))
n3 = int(input("Enter a third number: "))

if n1 > n2 and n1 > n3:
    print(f" \nAmong the numbers entered, the largest is: {n1}")
elif n2 > n1 and n2 > n3:
    print(f" \nAmong the numbers entered, the largest is: {n2}")
elif n3 > n2 and n3 > n1:
    print(f" \nAmong the numbers entered, the largest is: {n3}")
elif n1 == n2 and n1 == n3 and n2 == n3:
    print("The number entered are the same!")


if n1 < n2 and n1 < n3:
    print(f"And the smallest is: {n1}")
elif n2 < n1 and n2 < n3:
    print(f"And the smallest is: {n2}")
elif n3 < n1 and n3 < n2:
    print(f"And the smallest is: {n3}")
    



