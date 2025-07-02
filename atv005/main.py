salario = float(input("Write your salary:"))

if salario <= 3000:
    print("Junior Dev")
elif salario >3000 and salario <=6000:
    print("Full Dev")
elif salario >6000 and salario <=15000:
    print("Senior Dev")
else:
    print("too good daddy")