from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('main.html.j2', name="Nieznajomy")

@app.route("/add_user", methods=['POST'])
def add_user():
    return f"Zaraz dodam uzytkownika: {request.form['username']}"

@app.route("/<name>")
def hello_name(name):
    return render_template('main.html.j2', name=name)


# http://flask.pocoo.org/docs/1.0/quickstart/

# ten if potrzebny, zeby nie odpalal zawsze a tylko gdy puszczamy z tego kodu
if __name__ == "__main__":
    app.run()
