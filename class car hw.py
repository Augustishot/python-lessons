class Car:
    color = ''
    brand = ''
    
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

c = input('What is your favorite color?')
b = input('What is your favorite car brand?')

c1 = Car(c, b)
print('Your favorite car is a car made by', c1.brand, \
      'colored', c1.color + '.')
    
c2 = input('What is your second favorite color?')
b2 = input('What is your second favorite car brand?')

c1 = Car(c2, b2)
print('Your second favorite car is a car made by', c1.brand, \
      'colored', c1.color + '.')