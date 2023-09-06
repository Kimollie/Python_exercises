import random

# Ex 4.1
count = 1
while count < 1000:
    if count % 3 == 0:
        print(count)
        count += 1
    else: count += 1

# Ex 4.2
inch = float(input("Enter inch input: "))
while inch >= 0:
    cm = inch * 2.54
    print(f"{cm:.2f} cm.")
    inch = float(input("Enter inch input: "))
print("Invalid input")

# Ex 4.3
num = input("Enter number: ")
arr = []
while num != "":
    arr.append(float(num))
    num = input("Enter number: ")
smallest = min(arr)
largest = max(arr)
print(f"Smallest number entered: {smallest}")
print(f"Largest number entered: {largest}")

# Ex 4.4
correct = random.randint(1,10)
guess = int(input("Guess a integer number between 1 to 10: "))
while guess != correct:
    if guess < correct:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Guess a integer number between 1 to 10: "))
print("Correct")

# Ex 4.5
username = input("Enter username: ")
password = input("Enter password: ")
count = 1
while count <= 5:
    if username == "python" and password == "rules":
        print("Welcome")
        break
    elif count == 5:
        print("Access denied!")
    else:
        print("Incorrect. Enter username and password again!")
        username = input("Enter username: ")
        password = input("Enter password: ")
    count += 1

# Ex 4.6
point_N = int(input("How many random points to generate? "))
point_n = 0
point_generated = 0
while point_generated <= point_N:
    random_x = random.uniform(-1,1)
    random_y = random.uniform(-1,1)
    point_generated += 1
    equation_check = random_x*random_x + random_y*random_y
    if equation_check < 1:
        point_n += 1
pi = 4 * point_n / point_N
print(f"Approximate value of Pi: {pi}")





