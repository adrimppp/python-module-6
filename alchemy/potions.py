from .elements import create_earth, create_water, create_air, create_fire

def healing_potion():
    return (f"Healing potion brewed with {create_fire()} and"
            f" {create_water()}")


def strength_potion():
    return (f"Strength potion brewed with {create_earth()}"
            f"and {create_fire()}")


def invisibility_potion():
    return (f"Invisibility potion brewed with {create_air()}"
            f"and {create_water()}")


def wisdom_potion():
    return (f"Wisdom potion brewed with all elements: "
            f"{create_air()} {create_water()} {create_fire()}"
            f" {create_earth()}")
