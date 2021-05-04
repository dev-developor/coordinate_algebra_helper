import math
import fractions

# whole = int(input("Enter integer: "))
# fraction = fractions.Fraction(input("Enter fraction: "))
# decimal = float(fractions.Fraction(fraction))
# print(whole, fraction, decimal)
#print(-1/fractions.Fraction().limit_denominator())
#     diagnols = math.sqrt((x1+y1) ** 2 + (x2+y2) ** 2)
#     print("√(({},{}) ^ 2 + ({},{}) ^ 2) which leads to a diagnol distance of {}".format(x1,y1,x2,y2,diagnols))

class calculater:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0 
        self.y2 = 0
        
    def set_var (self):
        self.x1 = float(input("Enter x1: "))
        self.y1 = float(input("Enter y1: "))
        self.x2 = float(input("Enter x2: "))
        self.y2 = float(input("Enter y2: "))

    def slope(self):
        slope = (self.y2 - self.y1) / (self.x2 - self.x1)
        print("({} - {}) / ({} - {}) = slope of {}".format(self.y2,self.y1,self.x2,self.x1,slope))

    def distance(self):
        distance = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        print("√(({}-{}) ^ 2 + ({}-{}) ^ 2) = distance of {}".format(self.x2 ,self.x1 ,self.y2 ,self.y1 ,distance))
        
    def slopedistance(self):
        self.slope()
        self.distance()
         
    def midpoint(self):
        midpoint = (self.x1 + self.x2)/2, (self.y1 + self.y2)/2
        x = (self.x1 + self.x2)/2
        y = (self.y1 + self.y2)/2
        print("({} + {})/2 = {} ({} + {})/2 = {} midpoint is {}".format(self.x1 ,self.x2 ,x ,self.y1, self.y2 ,y,midpoint))

c = calculater()