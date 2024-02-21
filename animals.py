# import the python datetime module to help us create a timestamp
from datetime import date


# petting area
class Donkey:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True


class Llama:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True


class Goat:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True


class Pony:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True


class Pig:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True


# glass tank
class Copperhead:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True


class RatSnake:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True


class BoaConstrictor:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True


class GarterSnake:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True


class Anaconda:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True


# pond
class Mallard:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True


class Goldfish:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True


class Frog:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True


class Turtle:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True


class Swan:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True


eeyore = Donkey()
miss_fuzz = Llama()
billy = Goat()
sir_gallop_a_lot = Pony()
hamlet = Pig()
slytherin = Copperhead()
sneaky_pete = RatSnake()
mr_squeeze = BoaConstrictor()
slinky_joe = GarterSnake()
monty = Anaconda()
quacky = Mallard()
goldie = Goldfish()
croakster = Frog()
shelly = Turtle()
gracie = Swan()

eeyore.name = "Eeyore"
eeyore.species = "donkey"
print(eeyore.name)

miss_fuzz.name = "Miss Fuzz"
miss_fuzz.species = "domestic llama"
print(miss_fuzz.name)

billy.name = "Billy"
billy.species = "goat"
print(billy.name)

sir_gallop_a_lot.name = "Sir Gallop-A-Lot"
sir_gallop_a_lot.species = "pony"
print(sir_gallop_a_lot.name)

hamlet.name = "Hamlet"
hamlet.species = "pig"
print(hamlet.name)

slytherin.name = "Slytherin"
slytherin.species = "copperhead"
print(slytherin.name)

sneaky_pete.name = "Sneaky Pete"
sneaky_pete.species = "rat snake"
print(sneaky_pete.name)

mr_squeeze.name = "Mr. Squeeze"
mr_squeeze.species = "boa constrictor"
print(mr_squeeze.name)

slinky_joe.name = "Slinky Joe"
slinky_joe.species = "garter snake"
print(slinky_joe.name)

monty.name = "Monty"
monty.species = "anaconda"
print(monty.name)

quacky.name = "Quacky"
quacky.species = "mallard"
print(quacky.name)

goldie.name = "Goldie"
goldie.species = "goldfish"
print(goldie.name)

croakster.name = "Croakster"
croakster.species = "frog"
print(croakster.name)

shelly.name = "Shelly"
shelly.species = "turtle"
print(shelly.name)

gracie.name = "Gracie"
gracie.species = "swan"
print(gracie.name)
