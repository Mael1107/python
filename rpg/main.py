from random import randint

list_npcs = []

def create_npc():
    level = randint(0,50)
    new_npc = {
        "name" : f"Monster {level}",
        "level" : level,
        "damage" : 5 * level,
        "hp" : 100 * level
    }
 
    return new_npc

def generate_npcs(n_npcs):
    for x in range(n_npcs):
        new_npc = create_npc()
        list_npcs.append(new_npc)

def display_npcs():
    for npc in list_npcs:
        print(f"Name: {npc["name"]} | Level: {npc["damage"]} | Damege: {npc["damage"]} | HP: {npc["hp"]}")

generate_npcs(5)
display_npcs()






