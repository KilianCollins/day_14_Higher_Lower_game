
import random

data_base = [
    {"Taylor Swift": 54_000_000},
    {"Joe Rogean": 66_000_21},
    {"Bob": 334},
    {"NickelBack": 6_000_300},
    {"Beyonce": 600_700_21},

]

def get_person():
    """should return just the key or the name of the person"""
    rand = random.randint(0, len(data_base) - 1)

    c_name = data_base[rand].keys()
    c_val = data_base[rand].values()
    return [c_name,c_val]




still_playing = True

while still_playing:
    still_going = input("play my game?").lower().strip(" ")
    if still_going == "yes":
        continue

    print(f"A:{get_person()[0]} and B:{get_person()[0]}")
    guess = input("which do you think has a greater following?: type A or B").upper().strip(" ")
