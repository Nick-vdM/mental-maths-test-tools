import random


def addition(x_lower=100, x_upper=1000, y_lower=1000, y_upper=9000):
    x = random.randint(x_lower, x_upper)
    y = random.randint(y_lower, y_upper)
    print("------")
    print("\t ", x, "\n+\t", y)
    input()
    print(x + y)

def subtraction(x_lower=1000, x_upper=9000, y_lower=100, y_upper=1000):
    x = random.randint(x_lower, x_upper)
    y = random.randint(y_lower, y_upper)
    print("------")
    print("\t", x, "\n-\t ", y)
    input()
    print(x - y)

def multiply(x_lower=15, x_upper=99, y_lower=15, y_upper=99):
    x = random.randint(x_lower, x_upper)
    y = random.randint(y_lower, y_upper)
    print("------")
    print("\t", x, "\n*\t", y)
    input()
    print(x * y)


def square(x_lower=14, x_upper=99):
    x = random.randint(x_lower, x_upper)
    print("------")
    print("\t ", str(x) + "^2")
    input()
    print(x ** 2)

def complement(x_lower=16, x_upper=90, goal=100):
    x = random.randint(x_lower, x_upper)
    print('\t', x, 'distance from', goal)
    input()
    print(goal - x)
