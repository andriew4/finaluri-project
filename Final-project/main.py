from flask import Flask, render_template

app = Flask(__name__)




@app.route("/")
def home():
    return render_template("home.html")


@app.route("/registration")
def sign_up():
    return render_template("registration.html")


@app.route("/login")
def log_in():
    return render_template("login.html")


@app.route("/info")
def info():
    return render_template("info.html")


if __name__ == '__main__':
    app.run(debug=True)
