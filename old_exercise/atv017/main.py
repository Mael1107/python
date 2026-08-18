n1 = float(input("Enter your first note: "))
n2 = float(input("Enter your second note: "))

average = (n1 + n2) / 2

print(f"Your average is: {average:.1f}")

if average >= 6:
    print("Congratulation, your average was good!!")
else:
    print("What a pit, you need to study more!")
