import random
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Guess a number between 0 and  9</h1>"


@app.route("/<int:num>")
def choice(num, choice_number = random.choice(range(0, 10)) ):
    print(choice_number)

    if num == choice_number:
        return "<h1> You get it</h1>"
    elif num > choice_number:
        return "<h1>wrong number keep trying number is lower</h1>"
    else:
        return "<h1><h1>wrong number keep trying number is higher</h1>"


if __name__ == "__main__":
    app.run(debug=True)
