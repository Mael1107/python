# Desafio 045 em CursoemVideo

from random import choice
import os

jokenpo = ["Rock", "Paper", "Scissors"]
pc_choice = choice(jokenpo)

player_choice = int(input(
    """
    Your options: 
    [0] - Rock
    [1] - Paper
    [2] - Scissors

    What is your move? 
    """))

os.system("cls" if os.name == "nt" else "clear")

print(f"I chose {pc_choice}")

if pc_choice == "Rock" and player_choice == 1:
    print("You \033[1;32mWON\033[m!")
elif pc_choice == "Rock" and player_choice == 0:
    print("We \033[1;33mDRAW\033[m!")
elif pc_choice == "Rock" and player_choice == 2:
    print("You \033[1;31mLOST\033[m!")
elif pc_choice == "Paper" and player_choice == 2:
    print("You \033[1;32mWON\033[m!")
elif pc_choice == "Paper" and player_choice == 1:
    print("We \033[1;33mDRAW\033[m!")
elif pc_choice == "Paper" and player_choice == 0:
    print("You \033[1;31mLOST\033[m!")
elif pc_choice == "Scissors" and player_choice == 0:
    print("You \033[1;32mWON\033[m!")
elif pc_choice == "Scissors" and player_choice == 2:
    print("We \033[1;33mDRAW\033[m!")
elif pc_choice == "Scissors" and player_choice == 1:
    print("You \033[1;31mLOST\033[m!")
else:
    print("Invalid!")
