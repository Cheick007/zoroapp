from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def Connexion():
    return render_template("Connexion.html")


@app.route('/acceuil')
def acceuil():
    return render_template("acceuil.html")


if __name__ == "__main__":  # Pour que la methode créée puisse s'éxécutée
    app.run(debug=True)
