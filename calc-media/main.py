# Desafio 040 em CursoemVideo

note1 = float(input("Enter your first note: "))
note2 = float(input("Enter your second note: "))

average = (note1 + note2) / 2

print(f" \nIts final average is: {average:.1f} ")

if average < 5:
    print("\033[1;31mFailed\033[m")
elif  5 < average < 6.9:
    print("You are in \033[1;33mrecovery!\033[m")
elif average >=7:
    print("\033[1;32mApproved\033[m")