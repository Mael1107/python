# Desafio 043 em CursoemVideo

mass = float(input("What is your mass? (in kg) "))
height = float(input("What is your height? (in m) "))

bmi = mass / ( height ** 2 )

print(f"\nYour body mass index (BMI) is: \033[7;30m{bmi:.2f}\033[m")

if bmi < 18.5:
    print("\033[1;33mUnderweight\033[m")
elif 18.5 <= bmi < 25:
    print("\033[1;32mIdeal Weight\033[m")
elif 25 <= bmi < 30:
    print("\033[1;31mOverweight\033[m")
elif 30 <= bmi < 40:
    print("\033[1;31mObesity\033[m")
else:
    print("\033[1;31mMorbid Obesity\033[m")