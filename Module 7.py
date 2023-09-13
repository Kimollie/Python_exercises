
# Ex 7.1
seasons = ()
while True:
    month = int(input("Enter a number of a month: "))
    if month == 12 or month <= 2:
        seasons = seasons + ("winter",)
        print("winter")
    elif month <= 5:
        seasons = seasons + ("spring",)
        print("spring")
    elif month <= 8:
        seasons = seasons + ("summer",)
        print("summer")
    elif month <= 11:
        seasons = seasons + ("autumn",)
        print("autumn")
    else:
        print("Invalid month")

# Ex 7.2
nameList = set()
while True:
    name = input("Enter name, press enter to display existing name: ")
    if name != "":
        if name in nameList:
            print("Existing name")
        else:
            print("New name")
            nameList.add(name)
    elif name == "": break
print("List of entered name: ")
for i in nameList:
    print(i)

# Ex 7.3

airportData = {
    "KJFK": "New York Airport",
    "EFHK": "Helsinki-Vantaa Airport",
    "ESSA": "Stockholm Arlanda Airport"
}


def addairport():
    icao = input("Enter ICAO code: ")
    name = input("Enter airport name: ")
    airportData[icao] = name


def fetchairport():
    icao = input("Enter ICAO code: ")
    while True:
        if icao in airportData:
            print(airportData[icao])
            break
        else:
            print("Invalid ICAO code! Enter again")
            icao = input("Enter ICAO code: ")


while True:
    command = input("Enter command (Add/Fetch/Quit): ")
    if command == "Add":
        addairport()
    elif command == "Fetch":
        fetchairport()
    elif command == "Quit":
        break
    else:
        print("Invalid command")
        command = input("Enter command (Add/Fetch/Quit): ")
