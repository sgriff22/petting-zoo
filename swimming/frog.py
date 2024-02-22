from datetime import date


class Frog:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.swimming = True

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}'
