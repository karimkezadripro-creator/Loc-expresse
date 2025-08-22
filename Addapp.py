from flask import Flask, render_template

app = Flask(__name__)

# Page d'accueil
@app.route("/")
def home():
    return render_template("index.html")  # Assure-toi d'avoir un fichier templates/index.html

# Exemple d'autre route
@app.route("/about")
def about():
    return "<h1>À propos</h1><p>Bienvenue sur Loc-expresse 🚗</p>"

if __name__ == "__main__":
    # Render mettra PORT automatiquement dans les variables d'env
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
