# Why Python is Great: Namedtuples
# Using namedtuple is way shorter than
# defining a class manually:

from collections import namedtuple
Car = namedtuple('Car', 'color mileage')

my_car = Car('red', 3812.4)

print(my_car.color, my_car.mileage)
