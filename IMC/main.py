# Desafio 043 em CursoemVideo

weight = float(input("What is your weight? (em weight) "))
height = float(input("What is your height? (em m) "))

imc = weight / ( height**2 )

print(f"\nYour body mass index (IMC) is: \033[7;30m{imc:.2f}\033[m")

if imc < 18.5:
    print("\033[1;33mUnderweight\033[m")
elif 18.5 <= imc < 25:
    print("\033[1;32mIdeal Weight\033[m")
elif 25 <= imc < 30:
    print("\033[1;31mOverweight\033[m")
elif 30 <= imc < 40:
    print("\033[1;31mObesity\033[m")
else:
    print("\033[1;31mMorbid Obesity\033[m")