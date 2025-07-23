# Desafio 032 em CursoemVideo
from datetime import date

ano = int(input("What year do you want to analyze? Enter 0 to analyse the current year. "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"The year {ano} is LEAP YEAR" )
else:
    print(F"The year {ano} NOT is leap year")