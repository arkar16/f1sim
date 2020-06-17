from team import *


class Chassis10:
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name + self.nation

    def __init__(self, team, rating):
        self.team = team
        self.rating = rating


c1 = Chassis10(t1, 7.75)
c2 = Chassis10(t2, 7.15)

print(c1.team, c1.rating)
print(c2.team, c2.rating)
