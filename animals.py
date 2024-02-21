# import the python datetime module to help us create a timestamp
from datetime import date


class Donkey:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


class Llama:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


class Goat:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


class Pony:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


class Pig:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


# Glass Tank
class Copperhead:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


class RatSnake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


class BoaConstrictor:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


class GarterSnake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


class Anaconda:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


# Pond
class Mallard:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Goldfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Frog:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Turtle:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Swan:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


eeyore = Donkey("Eeyore", "Sad Donkey")
miss_fuzz = Llama("Miss Fuzz", "Domestic Llama")
billy = Goat("Billy", "Playful Goat")
sir_gallop_a_lot = Pony("Sir Gallop-a-Lot", "Miniature Pony")
hamlet = Pig("Hamlet", "Adorable Pig")
slytherin = Copperhead("Slytherin", "Venomous Snake")
sneaky_pete = RatSnake("Sneaky Pete", "Sly Snake")
mr_squeeze = BoaConstrictor("Mr. Squeeze", "Gentle Giant")
slinky_joe = GarterSnake("Slinky Joe", "Smooth Operator")
monty = Anaconda("Monty", "Big Squeeze")
quacky = Mallard("Quacky", "Cheerful Mallard")
goldie = Goldfish("Goldie", "Shiny Goldfish")
croakster = Frog("Croakster", "Jumping Frog")
shelly = Turtle("Shelly", "Slow Turtle")
gracie = Swan("Gracie", "Elegant Swan")


print(f"{eeyore.name} the {eeyore.species}")
print(f"{miss_fuzz.name} the {miss_fuzz.species}")
print(f"{billy.name} the {billy.species}")
print(f"{sir_gallop_a_lot.name} the {sir_gallop_a_lot.species}")
print(f"{hamlet.name} the {hamlet.species}")
print(f"{slytherin.name} the {slytherin.species}")
print(f"{sneaky_pete.name} the {sneaky_pete.species}")
print(f"{mr_squeeze.name} the {mr_squeeze.species}")
print(f"{slinky_joe.name} the {slinky_joe.species}")
print(f"{monty.name} the {monty.species}")
print(f"{quacky.name} the {quacky.species}")
print(f"{goldie.name} the {goldie.species}")
print(f"{croakster.name} the {croakster.species}")
print(f"{shelly.name} the {shelly.species}")
print(f"{gracie.name} the {gracie.species}")
