# Desafio 022 em CursoemVideo

name = input("Enter your full name : ").strip()

uppercase = name.upper()
lowcase = name.lower()
length = len(name) - name.count(" ")
div = name.split()
first = len(div[0])

print(f"Your name in uppercase is: {uppercase}\n Your name in lowercase is: {lowcase}\n Your name have {length} letters\n and your first name is: {div[0]} and has {first}")
