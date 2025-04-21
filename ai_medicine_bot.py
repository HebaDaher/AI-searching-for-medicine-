# ai_medicine_bot.py

from pyswip import Prolog
from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)
prolog = Prolog()
prolog.consult("med_knowledge.pl")

# Mock function to simulate buying medicine
def buy_medicine_online(medicine):
    stores = ['Amazon', 'HealthKart', 'LocalPharma']
    return {
        'medicine': medicine,
        'price': f"${random.randint(5, 20)}",
        'store': random.choice(stores),
        'link': f"https://lifepharmacy.com/search?q={medicine}"
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    symptom = request.form['symptom'].lower()
    results = list(prolog.query(f"recommend_medicine({symptom}, Medicine)"))
    if not results:
        return jsonify({'message': 'No medicine found'}), 404

    recommendations = []
    for res in results:
        med = res["Medicine"]
        purchase = buy_medicine_online(med)
        recommendations.append(purchase)

    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True,port=5050)
