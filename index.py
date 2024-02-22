from slithering import Anaconda, BoaConstrictor, Copperhead, GarterSnake, RatSnake
from swimming import Frog, Goldfish, Mallard, Swan, Turtle
from walking import Donkey, Goat, Llama, Pig, Pony


# Petting zoo
eeyore = Donkey("Eeyore", "Sad Donkey", "morning", "hay")
print(eeyore)
print(eeyore.feed())

miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "midday", "Llama Chow")
print(miss_fuzz)
print(miss_fuzz.feed())

billy = Goat("Billy", "Playful Goat", "afternoon", "grass")
print(billy)
print(billy.feed())

sir_gallop_a_lot = Pony("Sir Gallop-a-Lot", "Miniature Pony", "midday", "oats")
print(sir_gallop_a_lot)
print(sir_gallop_a_lot.feed())

hamlet = Pig("Hamlet", "Adorable Pig", "morning", "slop")
print(hamlet)
print(hamlet.feed())


# Glass Tank
slytherin = Copperhead("Slytherin", "Venomous Snake", "a rat")
print(slytherin)
print(slytherin.feed())

sneaky_pete = RatSnake("Sneaky Pete", "Sly Snake", "a mouse")
print(sneaky_pete)
print(sneaky_pete.feed())

mr_squeeze = BoaConstrictor("Mr. Squeeze", "Gentle Giant", "squirrel")
print(mr_squeeze)
print(mr_squeeze.feed())

slinky_joe = GarterSnake("Slinky Joe", "Smooth Operator", "a mouse")
print(slinky_joe)
print(slinky_joe.feed())

monty = Anaconda("Monty", "Big Squeeze", "a whole chicken")
print(monty)
print(monty.feed())


# Pond
quacky = Mallard("Quacky", "Cheerful Mallard", "duck pellets")
print(quacky)
print(quacky.feed())

goldie = Goldfish("Goldie", "Shiny Goldfish", "fish flakes")
print(goldie)
print(goldie.feed())

croakster = Frog("Croakster", "Jumping Frog", "insects")
print(croakster)
print(croakster.feed())

shelly = Turtle("Shelly", "Slow Turtle", "lettuce")
print(shelly)
print(shelly.feed())

gracie = Swan("Gracie", "Elegant Swan", "potatoes")
print(gracie)
print(gracie.feed())
