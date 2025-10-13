# def my_function(a, b=2, c=3): # Here are the args with default values. First positional params, then kw
#     pass
# my_function(2, b=5) # When we call a func we can put another value, otherwise we use default one

# def all_aboard(a, *args, **kw):
#     print(a, args, kw)
#
#
# all_aboard(4, 7, 3, 0, x=10, y=64)
# 4, (7, 3, 0), {"x": 10, "y": 64}

# UNLIMITED POSITIONAL ARGUMENTS - *args (the type is tuple)
# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
# print(add(4,8,31,2))

# MANY KEYWORD ARGUMENTS - **kwargs (the type is dict)
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model") # If we don't input model it won't raise an error. It'll be None.
        self.color = kw.get("color")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
