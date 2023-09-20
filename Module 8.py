import mysql.connector
from geopy.distance import geodesic as GD, geodesic

try:
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='kim',
        password='pass_word',
    )
except mysql.Error as e:
    print(f"Error Connecting to MariaDB failed: {e}")
    exit(1)

cus = connection.cursor()

# Ex 8.1 Fetch airport and location from ICAO
def fetchairport():
    icao = input("Type a ICAO code: ")
    sql1 = "SELECT airport.name as airport_name, municipality, country.name as country_name FROM airport,country"
    sql1 += " WHERE airport.iso_country = country.iso_country and ident = '" + icao + "'"
    cus.execute(sql1)
    row = cus.fetchall()
    if len(row) == 0:
        print("No result")
    else:
        for airport_name, town, country in row:
            print(f"Airport: {airport_name} \nLocation: {town}, {country}")

# Ex 8.2 List all airports in the area code order by type
def listairport():
    areaCode = input("Enter area code: ")
    sql2 = "SELECT type, airport.name as airport_name FROM airport, country"
    sql2 += " WHERE airport.iso_country = country.iso_country and airport.iso_country = '" + areaCode + "'" + " ORDER BY type desc"
    cus.execute(sql2)
    row = cus.fetchall()
    if len(row) == 0:
        print("No result")
    else:
        for type, airport_name in row:
            print(f"Type: {type} \nAirport: {airport_name}")

# Ex 8.3 Calculation distance between two airport
def distanceairport():
    icaoCodes = []
    for i in range(0,2):
        icao = input(f"Enter area code {i+1}: ")
        icaoCodes.append(icao)
    sql3 = "SELECT latitude_deg, longitude_deg FROM airport"
    sql3 += " WHERE ident = '" + icaoCodes[0] + "' OR ident = '" + icaoCodes[1] + "'"
    cus.execute(sql3)
    row = cus.fetchall()
    if row == 0:
        print("No result")
    else:
        location = []
        for lat, long in row:
            location.append(lat)
            location.append(long)
        distance = geodesic((location[0],location[1]),(location[2],location[3]))
        print(f"Distance between these two airport is: {distance}")

#Main program
while True:
    command = input("Enter command(Fetch/List/Distance): ")
    if command == "Fetch":
        fetchairport()
    elif command == "List":
        listairport()
    elif command == "Distance":
        distanceairport()
    else:
        print("Invalid command. Enter command again")
