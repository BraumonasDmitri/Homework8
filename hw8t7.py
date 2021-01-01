class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.с = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма с1 и с2 равна')
        return f'с = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение с1 и с2 равно')
        return f'с = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'с = {self.a} + {self.b} * i'


с_1 = ComplexNumber(10, -2)
с_2 = ComplexNumber(-5, 4)
print(с_1)
print(с_1 + с_2)
print(с_1 * с_2)