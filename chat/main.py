import os

mensages = []

name = input("Name:")

while True:
    os.system("cls")

    if len(mensages) > 0:
        for m in mensages:
            print(m["name"], "-", m["text"])
    
    print("____________________")

    text = input("mensagem:")
    if text == "fim":
        break
    mensages.append({
        "name": name,
        "text": text
    })
