import random


class Engine10:
    def __repr__(self):
        return f"{self.name} {self.nation} {self.rating} {self.cost}"

    def __init__(self, name, nation, rating, cost):
        self.name = name
        self.nation = nation
        self.rating = rating
        self.cost = cost + rating


e1 = Engine10("Alfa Romeo", "ITA", 6.90, 3.5)
e2 = Engine10("BMW", "GER", 7.30, 7)
e3 = Engine10("Cosworth", "GBR", 7.10, 6)
e4 = Engine10("Ferrari", "ITA", 8.50, 8)
e5 = Engine10("Ford", "USA", 6.90, 9)
e6 = Engine10("Honda", "JPN", 6.80, 8)
e7 = Engine10("Mercedes", "GER", 9.20, 10.5)
e8 = Engine10("Peugeot", "FRA", 5.90, 4.5)
e9 = Engine10("Porsche", "GER", 6.10, 4.5)
e10 = Engine10("Renault", "FRA", 8.60, 8.5)
e11 = Engine10("Toyota", "JPN", 7.10, 7.5)
e12 = Engine10("Judd", "GBR", 5.50, 1)

engines = [(k, v) for k, v in locals().items() if k.startswith("e")]
engines.sort(reverse=False, key=lambda x: x[1].rating)
for e in engines:
    print(e)
