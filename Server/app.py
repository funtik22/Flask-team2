import files as files
import secure as secure
from flask import Flask, render_template, request

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
            "name": "Slava",
            "age": 18
        }


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return """
        <form method=post
        enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit
               value=upload>
        </form>"""
    else:
        file = request.files['file']
        file.save(file.filename)
        return ("ок")
