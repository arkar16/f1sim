import random


class Engine10:
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name + self.nation

    def __init__(self, name, nation, rating, cost):
        self.name = name
        self.nation = nation
        self.rating = rating
        self.cost = cost + rating


e1 = Engine10("Alfa Romeo", "ITA", 6.90, random.randint(5, 10))
e2 = Engine10("Audi", "GER", 7.50, random.randint(5, 10))
e3 = Engine10("BMW", "GER", 7.10, random.randint(5, 10))
e4 = Engine10("Cosworth", "GBR", 7.20, random.randint(5, 10))
e5 = Engine10("Ferrari", "ITA", 8.50, random.randint(5, 10))
e6 = Engine10("Ford", "USA", 6.90, random.randint(5, 10))
e7 = Engine10("Honda", "JPN", 6.80, random.randint(5, 10))
e8 = Engine10("Mercedes", "GER", 9.20, random.randint(5, 10))
e9 = Engine10("Peugeot", "FRA", 7.40, random.randint(5, 10))
e10 = Engine10("Porsche", "GER", 7.40, random.randint(5, 10))
e11 = Engine10("Renault", "FRA", 8.60, random.randint(5, 10))
e12 = Engine10("Toyota", "JPN", 7.10, random.randint(5, 10))
e13 = Engine10("Judd", "GBR", 6.70, random.randint(5, 10))
e14 = Engine10("Ilmor", "GBR", 6.70, random.randint(5, 10))

print(e14.name, e14.rating, e14.cost)

