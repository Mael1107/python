# Desafio 035 em CursoemVideo

r1 = float(input("Enter the length of the first line: "))
r2 = float(input("Enter the length of the second line: "))
r3 = float(input("Enter the length of the third line: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("The typed lines form a triangle!")
else:
    print("The typed lines NOT form a triangle!")