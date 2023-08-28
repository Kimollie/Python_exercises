import math
import random
#Ex1 and 2.1
name = input("What's your name?")
print("Hello, "+name)

#Ex 2.2
radius = input("Enter radius: ")
area = float(math.pi) * float(radius) * float(radius)
print(f"Area of this circle is: {area: .2f}")

#Ex 2.3
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
perimeter = (length+width)*2
rec_area = length * width
print(f"Perimeter of this rectangle: {perimeter: .2f}")
print(f"Area of this rectangle: {rec_area: .2f}")

#Ex 2.4
number1 = int(input("Enter first integer number:"))
number2 = int(input("Enter second integer number:"))
number3 = int(input("Enter third integer number:"))
sum = number1 + number2 + number3
product = number1*number2*number3
average = sum/3
print(f"Sum: {sum}")
print(f"Product: {product}")
print(f"Average: {average}")

#Ex 2.5
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
tal_pnd = talents*20
pnd_lt = (pounds +tal_pnd)*32
lt_gr = (lots+pnd_lt)*13.3
kilograms = int(lt_gr/1000)
grams = (lt_gr/1000 - kilograms)*1000
print(f"The weight in modern units: \n{kilograms} kilograms and {grams:.2f} grams.")

#Ex 2.6
lock3_dig1 = random.randint(0,9)
lock3_dig2 = random.randint(0,9)
lock3_dig3 = random.randint(0,9)
print(f"3-digit code ombination: {lock3_dig1}{lock3_dig2}{lock3_dig3}")
lock4_dig1 = random.randint(1,6)
lock4_dig2 = random.randint(1,6)
lock4_dig3 = random.randint(1,6)
lock4_dig4 = random.randint(1,6)
print(f"4-digit code ombination: {lock4_dig1}{lock4_dig2}{lock4_dig3}{lock4_dig4}")















