from datetime import date


class RatSnake:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.slithering = True

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}'

    def __str__(self):
        return f"{self.name} is a {self.species}"
