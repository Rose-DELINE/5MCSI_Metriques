# ===== IMPORTS =====
from flask import Flask, render_template, jsonify
from urllib.request import urlopen
import json
from datetime import datetime
import sqlite3  # si tu en as besoin plus tard

# ===== INITIALISATION DE L'APPLICATION =====
app = Flask(__name__)

# ===== ROUTES =====
@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

@app.route('/')
def hello_world():
    return render_template('hello.html')

# ===== EXERCICE 3 : ROUTE /tawarano/ =====
@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

# ===== BLOC PRINCIPAL =====
if __name__ == "__main__":
    app.run(debug=True)
