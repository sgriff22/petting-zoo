from slithering import Anaconda, BoaConstrictor, Copperhead, GarterSnake, RatSnake
from swimming import Frog, Goldfish, Mallard, Swan, Turtle
from walking import Donkey, Goat, Llama, Pig, Pony


# Petting zoo
eeyore = Donkey("Eeyore", "Sad Donkey", "morning", "hay")
print(
    f"{eeyore.name} the {eeyore.species} is available to pet during the {eeyore.shift} shift."
)
print(eeyore.feed())

miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "midday", "Llama Chow")
print(
    f"{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift."
)
print(miss_fuzz.feed())

billy = Goat("Billy", "Playful Goat", "afternoon", "grass")
print(
    f"{billy.name} the {billy.species} is available to pet during the {billy.shift} shift."
)
print(billy.feed())

sir_gallop_a_lot = Pony("Sir Gallop-a-Lot", "Miniature Pony", "midday", "oats")
print(
    f"{sir_gallop_a_lot.name} the {sir_gallop_a_lot.species} is available to pet during the {sir_gallop_a_lot.shift} shift."
)
print(sir_gallop_a_lot.feed())

hamlet = Pig("Hamlet", "Adorable Pig", "morning", "slop")
print(
    f"{hamlet.name} the {hamlet.species} is available to pet during the {hamlet.shift} shift."
)
print(hamlet.feed())


# Glass Tank
slytherin = Copperhead("Slytherin", "Venomous Snake", "a rat")
print(f"{slytherin.name} the {slytherin.species}")
print(slytherin.feed())

sneaky_pete = RatSnake("Sneaky Pete", "Sly Snake", "a mouse")
print(f"{sneaky_pete.name} the {sneaky_pete.species}")
print(sneaky_pete.feed())

mr_squeeze = BoaConstrictor("Mr. Squeeze", "Gentle Giant", "squirrel")
print(f"{mr_squeeze.name} the {mr_squeeze.species}")
print(mr_squeeze.feed())

slinky_joe = GarterSnake("Slinky Joe", "Smooth Operator", "a mouse")
print(f"{slinky_joe.name} the {slinky_joe.species}")
print(slinky_joe.feed())

monty = Anaconda("Monty", "Big Squeeze", "a whole chicken")
print(f"{monty.name} the {monty.species}")
print(monty.feed())


# Pond
quacky = Mallard("Quacky", "Cheerful Mallard", "duck pellets")
print(f"{quacky.name} the {quacky.species}")
print(quacky.feed())

goldie = Goldfish("Goldie", "Shiny Goldfish", "fish flakes")
print(f"{goldie.name} the {goldie.species}")
print(goldie.feed())

croakster = Frog("Croakster", "Jumping Frog", "insects")
print(f"{croakster.name} the {croakster.species}")
print(croakster.feed())

shelly = Turtle("Shelly", "Slow Turtle", "lettuce")
print(f"{shelly.name} the {shelly.species}")
print(shelly.feed())

gracie = Swan("Gracie", "Elegant Swan", "potatoes")
print(f"{gracie.name} the {gracie.species}")
print(gracie.feed())
