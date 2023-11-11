from flask import Flask, request

app = Flask(__name__)


@app.route('/prime_number/<number>')
def check_prime(number):
    number = int(number)
    check = True

    if number == 1:
        check = False
    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                check = False
                break

    response = {
        "Number": number,
        "isPrime": check
    }

    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
