from flask import Flask, render_template, request

app = Flask(__name__, static_folder="public", static_url_path="/public")

liste_voitures = [
  {"marque": "Buggati", "photo": "/public/images/car1.jpg"},
  {"marque": "Maybach", "photo": "/public/images/car2.jpg"},
  {"marque": "Mazeratti", "photo": "/public/images/car2.jpg"}
]

@app.route("/")
def home():
    return render_template("index.html", liste=liste_voitures)

@app.route("/form", methods=["POST"])
def form():
    print(request.form.get("marque"))
    liste_voitures.append({
      "marque": request.form.get("marque"),
      "photo": "/public/images/car2.jpg"
    })
    return render_template("index.html", liste=liste_voitures)


app.run(port=5000, debug=True)
