def add(*args):
    return_value = 0
    for x in args:
        return_value += x
    return return_value


def calculate(n, **kwarg):
    n += kwarg["add"]
    n *= kwarg["multiply"]
    print(n)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get('colour')
        self.seats = kwargs.get('seats')

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)

