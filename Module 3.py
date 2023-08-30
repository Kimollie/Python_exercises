# Ex 3.1
length = float(input("Enter length of Zander(cm): "))
limit = 42 - length
if length < 42:
    print(f"This zander is {limit} cm below the size limit. Please release this fish back into the lake.")
else:
    print("Fish OK")

# Ex 3.2
cabin_class = input("Enter the cabin class: ")
if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("Above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck")
else:
    print("Invalid cabin class. Try again with all caps.")

# Ex 3.3
gender = input("Enter biological gender (male or female): ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))
if gender == "female":
    if hemoglobin > 155:
        print("Hemoglobin value is high")
    elif hemoglobin >= 117:
        print("Hemoglobin value is normal")
    else:
        print("Hemoglobin value is low")
elif gender == "male":
    if hemoglobin > 167:
        print("Hemoglobin value is high")
    elif hemoglobin >= 134:
        print("Hemoglobin value is normal")
    else:
        print("Hemoglobin value is low")
else:
    print("Invalid")

# Ex 3.4
year = int(input("Enter year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year")
        else: print("This is not a leap year")
    else: print("This a leap year")
else: print("This is not a leap year")
