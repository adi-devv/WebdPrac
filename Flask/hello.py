from flask import Flask

app = Flask(__name__)

def bold(function):
    def wrap():
        return f'<b>{function()}</b>'

    return wrap

@app.route('/')
@bold
def hellow():
    return 'Hellow!'

@app.route('/user/<name>')
def ha(name):
    return '<h1 style="text-align: center">Haha</h1>'\
           '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHM0eGJvOGI2ano4OXlxYWNobjNuZmpnbnY2MGo0bDdmdTZ1aGJ2bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RukXlRREkBRUOJi2uL/giphy.gif" width=200></img>'\

if __name__ == "__main__":
    app.run(debug=True)
