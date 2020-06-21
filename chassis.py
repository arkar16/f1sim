from team import *


class Chassis10:
    def __str__(self):
        return self.name + self.nation

    def __init__(self, team, rating):
        self.team = team
        self.rating = rating


c1 = Chassis10(t1, 7.75)
c2 = Chassis10(t2, 7.15)
c3 = Chassis10(t3, 7.90)
c4 = Chassis10(t4, 7.40)
c5 = Chassis10(t5, 5.70)
c6 = Chassis10(t6, 6.80)
c7 = Chassis10(t7, 6.15)
c8 = Chassis10(t8, 5.40)
c9 = Chassis10(t9, 3.70)
c10 = Chassis10(t10, 3.15)
c11 = Chassis10(t11, 5.90)
c12 = Chassis10(t12, 3.25)


