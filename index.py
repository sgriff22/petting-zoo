from slithering import Anaconda, BoaConstrictor, Copperhead, GarterSnake, RatSnake
from swimming import Frog, Goldfish, Mallard, Swan, Turtle
from walking import Donkey, Goat, Llama, Pig, Pony


# Petting zoo
eeyore = Donkey("Eeyore", "Sad Donkey", "morning")
print(
    f"{eeyore.name} the {eeyore.species} is available to pet during the {eeyore.shift} shift."
)

miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "midday")
print(
    f"{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift."
)

billy = Goat("Billy", "Playful Goat", "afternoon")
print(
    f"{billy.name} the {billy.species} is available to pet during the {billy.shift} shift."
)

sir_gallop_a_lot = Pony("Sir Gallop-a-Lot", "Miniature Pony", "midday")
print(
    f"{sir_gallop_a_lot.name} the {sir_gallop_a_lot.species} is available to pet during the {sir_gallop_a_lot.shift} shift."
)

hamlet = Pig("Hamlet", "Adorable Pig", "morning")
print(
    f"{hamlet.name} the {hamlet.species} is available to pet during the {hamlet.shift} shift."
)


# Glass Tank
slytherin = Copperhead("Slytherin", "Venomous Snake")
print(f"{slytherin.name} the {slytherin.species}")

sneaky_pete = RatSnake("Sneaky Pete", "Sly Snake")
print(f"{sneaky_pete.name} the {sneaky_pete.species}")

mr_squeeze = BoaConstrictor("Mr. Squeeze", "Gentle Giant")
print(f"{mr_squeeze.name} the {mr_squeeze.species}")

slinky_joe = GarterSnake("Slinky Joe", "Smooth Operator")
print(f"{slinky_joe.name} the {slinky_joe.species}")

monty = Anaconda("Monty", "Big Squeeze")
print(f"{monty.name} the {monty.species}")


# Pond
quacky = Mallard("Quacky", "Cheerful Mallard")
print(f"{quacky.name} the {quacky.species}")

goldie = Goldfish("Goldie", "Shiny Goldfish")
print(f"{goldie.name} the {goldie.species}")

croakster = Frog("Croakster", "Jumping Frog")
print(f"{croakster.name} the {croakster.species}")

shelly = Turtle("Shelly", "Slow Turtle")
print(f"{shelly.name} the {shelly.species}")

gracie = Swan("Gracie", "Elegant Swan")
print(f"{gracie.name} the {gracie.species}")
