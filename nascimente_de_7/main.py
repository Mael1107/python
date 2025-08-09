# Desafio 055 em CursoemVideo

from datetime import datetime

current_year = datetime.now().year
years = []
adults = []
minors = []

for i in range(1, 8):
    year_of_birth = int(input("What year were you born? "))
    years.append(year_of_birth)
    if current_year - year_of_birth >= 18:
        adults.append(year_of_birth)
    else:
        minors.append(year_of_birth)
print(years)
print(f"{len(adults)} peoples are MAJOR age!")
print(f"{len(minors)} people are MINORS age!")

    