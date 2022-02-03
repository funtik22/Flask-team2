from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/about")
def about():
    return "О сегодняшнем дне"


@app.route("/biba/<name>")
@app.route("/biba/")
def n(name=None):
    return render_template("index.html", name=name)


@app.errorhandler(404)
def error404(e):
    return render_template("404.html"), 404


@app.route("/user/")
def json():
    return \
        {
            "ID": 1,
            "name": "Artem",
            "age": 16
        }
