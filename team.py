from engine import *


class Team10:
    def __str__(self):
        return self.name + " " + self.nation

    def __init__(self, name, nation, money, engine):
        self.name = name
        self.nation = nation
        self.money = money
        self.engine = engine


t1 = Team10("McLaren", "GBR", 220, e7)
t2 = Team10("Mercedes", "GER", 185, e7)
t3 = Team10("Red Bull", "AUT", 150, e10)
t4 = Team10("Scuderia Ferrari", "ITA", 240, e4)
t5 = Team10("Williams", "GBR", 90, e7)
t6 = Team10("Renault", "FRA", 105, e10)
t7 = Team10("Force India", "IND", 80, e7)
t8 = Team10("Toro Rosso", "ITA", 105, e4)
t9 = Team10("Lotus", "MYS", 65, e3)
t10 = Team10("HRT", "ESP", 40, e3)
t11 = Team10("Sauber", "CHE", 75, e4)
t12 = Team10("Virgin", "GBR", 45, e3)
