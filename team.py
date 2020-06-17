class Team10:
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name + " " + self.nation

    def __init__(self, name, nation, money):
        self.name = name
        self.nation = nation
        self.money = money


t1 = Team10("McLaren", "GBR", 220)
t2 = Team10("Mercedes", "GER", 185)
t3 = Team10("Red Bull", "AUT", 150)
t4 = Team10("Scuderia Ferrari", "ITA", 240)
t5 = Team10("Williams", "GBR", 90)
t6 = Team10("Renault", "FRA", 105)
t7 = Team10("Force India", "IND", 80)
