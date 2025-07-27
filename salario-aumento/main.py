# Desafio 034 em CursoemVideo

salary = float(input("Enter your current salary to calculate your increase: "))

if salary <= 1250:
    new_salary = salary * 1.15
else:
    new_salary = salary * 1.1

print(f"Your new salary is: R${new_salary:.2f}")