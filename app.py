from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def welcome():
    if request.method == "POST":
        return render_template("welcome.html")
    else:
        return render_template("welcome.html")
