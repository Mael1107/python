# Desafio 039 em CursoemVideo

from datetime import date

current_year = date.today().year
year_of_birth = int(input("What year were you born? "))
age = current_year - year_of_birth

if age == 18:
    print("It is time to \033[1;32menlist\033[m!")
elif age == 18 + 1:
    print(f"Your time of the enlist has \033[1;31mpassed\033[m. Should have enlisted there \033[1;31m{age - 18} year ago\033[m!")    
elif age > 18:
    print(f"Your time of the enlist has \033[1;31mpassed\033[m. Should have enlisted there \033[1;31m{age - 18} years ago\033[m!")

elif age == 18 - 1:
    print(f"You are very young, \033[1;31mthere are still {18 - age } year left\033[m!")
else:
    print(f"You are very young, \033[1;31mthere are still {18 - age } years left\033[m!")