from datetime import date


class Pony:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.date_added = date.today()
        self.walking = True

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}'
