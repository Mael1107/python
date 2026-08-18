# Desafio 044 em CursoemVideo
import os

price_product= float(input("What is the value of the product? "))
new_price_product = ""
installments_value = ""

os.system("cls" if os.name == "nt" else "clear")

payment_method = int(input(
    """What is the payment method? 
    1 - At Sight
    2 - Parcelled in card
    """))

os.system("cls" if os.name == "nt" else "clear")

if payment_method == 1:
    payment_method = int(input(
        """
        1 - With cash
        2 - WIth Debit Card
        """))
    
    os.system("cls" if os.name == "nt" else "clear")

    if payment_method == 1:
        new_price_product = price_product * 0.9
        print(f"At sight, with cash, the value of the product is R${new_price_product:.2f}.")
    elif payment_method == 2:
        new_price_product = price_product * 0.95
        print(f"At sight, with the Debit Card, the value of the product is R${new_price_product:.2f}.")
    else:
        print("Invalid value!")
else:
    payment_method = int(input(
        """
        1 - 2x in Card 
        2 - 3x in Card
        """))
    os.system("cls" if os.name == "nt" else "clear")

    if payment_method == 1:
        installments_value = price_product / 2
        print(f"2 installment on card, the final value of the product remains R${price_product:.2f}, with two equal portions of R${installments_value:.2f}. ")
    elif payment_method == 2:
        new_price_product = price_product * 1.2
        installments_value = new_price_product / 3
        print(f"3 installment on card, the final value of the product is R${new_price_product:.2f}, with three equal portions of R${installments_value:.2f}.")
    else:
        print("Invalid value!")