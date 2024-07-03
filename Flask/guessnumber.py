import random

from flask import Flask

app = Flask(__name__)
r = random.randint(0, 9)


@app.route('/')
def hellow():
    return '<h1 style="text-align: center">Guess A Number (0-9)</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200></img>'

@ app.route('/<int:guess>')
def ha(guess):
    if guess > r:
        return '<h1 style="text-align: center">Too High!</h1>' \
               '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHM0eGJvOGI2ano4OXlxYWNobjNuZmpnbnY2MGo0bDdmdTZ1aGJ2bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RukXlRREkBRUOJi2uL/giphy.gif" width=200></img>'
    elif guess < r:
        return '<h1 style="text-align: center">Too Low!</h1>' \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return '<h1 style="text-align: center">Hurrah!</h1>' \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
