import random
import math
# Ex 6.1
def roll():
    dice = random.randint(1,6)
    return dice
dice = 0
while dice != 6:
    dice = roll()
    print(dice)

# Ex 6.2
side =int(input("Maximum number on the dice: "))
def roll(side):
    dice = random.randint(1,side)
    return dice
dice = 0
while dice != side:
    dice = roll(side)
    print(dice)

# Ex 6.3
def convert(gallon):
    litre = gallon*3.785
    return litre

gal = float(input("Enter gallons: "))
while gal >= 0:
    lit = convert(gal)
    print(f"{gal} gallons = {lit:.2f} litres")
    gal = float(input("Enter gallons: "))
print("Invalid")

# Ex 6.4
def sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum

li = [5, 7, 8, 9, 10, 6]
print(sum(li))

# Ex 6.5
def even(list):
    evenList = []
    for i in list:
        if i % 2 == 0:
            evenList.append(i)
    return evenList

numbers = [5,8,3,4,5,6,2,3,2,9,7]
print(f"Original list: {numbers}")
print(f"New list with only even numbers: {even(numbers)}")


# Ex 6.6
def pizzavalue(diameter, price):
    area = math.pi * math.sqrt(diameter/2*0.01)
    value = price/area
    return value

dia1 = float(input("Enter diameter of pizza 1 (cm): "))
pr1 = float(input("Enter price of pizza 1 (euro): "))
dia2 = float(input("Enter diameter of pizza 2 (cm): "))
pr2 = float(input("Enter price of pizza 2 (euro): "))
value1 = pizzavalue(dia1, pr1)
value2 = pizzavalue(dia2, pr2)

if value1 < value2:
    print("Pizza 1 has better value for money")
else:
    print("Pizza 2 has better value for money")