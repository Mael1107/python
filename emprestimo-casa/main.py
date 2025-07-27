# Desafio 036 em CursoemVideo

house = float(input("What is the value of the house? "))
salary = float(input("What is your monthly salary? "))
time = float(input("In how many years will you pay? "))


installment = house / ( time * 12 )

if installment <= ( 0.3 * salary ):
    print(f"You can \033[1;32mrealize\033[m the loan! The amount of the monthly installment will be \033[31mR${installment:.2f}\033[m")
else:
    print("Unfortunately you can not make this loan, \033[1;31myour salary is very low!\033[m")