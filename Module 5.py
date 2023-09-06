import random

# Ex 5.1
dice_amount = int(input("How many dice to roll? "))
dice = []
sum = 0
while len(dice) < dice_amount:
    num = random.randint(1,6)
    dice.append(num)
for i in dice:
    sum = sum + i
print(f"Rolled dice are {dice}.\nSum of these dice: {sum}")

# Ex 5.2
numbers = []
num = input("Enter number, or press enter to quit: ")
while num != "":
    numbers.append(int(num))
    num = input("Enter number, or press enter to quit: ")
numbers.sort(reverse=True)
print(f"Five greatest entered number: {numbers[0:5]}")

# Ex 5.3
num = int(input("Enter a number: "))
prime = True
if num == 1:
    print("This is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("This is not a prime number")
            prime = False
            break
    if prime == True:
        print("This is a prime number")

# Ex 5.4
cities = []
for i in range(1,6):
    city = input(f"Enter city {i}: ")
    cities.append(city)
for index, city in enumerate (cities, start=1):
    print(f"City {index}: {city}")

