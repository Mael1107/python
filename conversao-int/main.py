# Desafio 037 em CursoemVideo

num = int(input("Enter a number: "))
conversion = int(input(
    """Choose wich conversion base: 
    1 - BINARY
    2 - OCTAL
    3 - HEXADECIMAL
    """))

if conversion == 1:
    print(f"The number converted to binary is: {bin(num)[2:]}")
elif conversion == 2:
    print(f"The number converted to OCTAL is: {oct(num)[2:]}")
elif conversion == 3:
    print(f"The number converted to binary is: {hex(num)[2:].upper()}")