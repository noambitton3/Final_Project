import consts
import random

def random_volunteer(list):
    random_vol = random.choice(list)
    return random_vol


def remove_volunteer(list, current_vol):
    list.remove(current_vol)
    return list