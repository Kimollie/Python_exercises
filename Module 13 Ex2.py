from flask import Flask
import mysql.connector

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

app = Flask(__name__)


@app.route('/airport/<icao>')
def fetchairport(icao):
    sql = "SELECT airport.name as airport_name, municipality FROM airport"
    sql += " WHERE ident = '" + icao + "'"
    cus.execute(sql)
    row = cus.fetchall()
    name = None
    location = None
    if len(row) == 0:
        response = {
            "message": "invalid ICAO"
        }
    else:
        for airport_name, city in row:
            name = airport_name
            location = city

        response = {
            "ICAO": icao,
            "Name": name,
            "Location": location
        }

    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)