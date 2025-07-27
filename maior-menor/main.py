# Desafio 038 em CursoemVideo

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

if num1 > num2:
    print(f"{num1} > {num2}")
elif num1 == num2:
    print("The \033[1;31mvalues\033[m are \033[1;31mequal\033[m!")
else:
    print(f"{num2} > {num1}")
