class Circle:
    def __init__(self, r):
        self.r = r

    def calc_circum(self):
        return 2 * 22/7 * self.r
    
    def calc_area(self):
        return 22/7 * self.r * self.r
    
c1 = Circle(7)
print(c1.calc_area(), c1.calc_circum())