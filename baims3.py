class Rectangle:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def dien_tich(self):
        return self.dai * self.rong

    def chu_vi(self):
        return (self.dai + self.rong) * 2

    @property
    def area(self):
        return self.dien_tich()

    @property
    def perimeter(self):
        return self.chu_vi()

hcn = Rectangle(5, 3)

print("Diện tích:", hcn.area)        
print("Chu vi:", hcn.perimeter)      
