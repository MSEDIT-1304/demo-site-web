from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def accueil():
    return render_template("index.html")


@app.route("/fonctionnalites")
def fonctionnalites():
    return render_template("fonctionnalites.html")


@app.route("/realisations")
def realisations():
    return render_template("realisations.html")


@app.route("/projet")
def projet():
    return render_template("projet.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
