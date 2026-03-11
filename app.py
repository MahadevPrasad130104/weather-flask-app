from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "0970fb81e6b11977abdb6dba107de85e"

@app.route("/", methods=["GET","POST"])
def home():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        # Check if city exists
        if data["cod"] == 200:

            weather = {
                "city": city,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"]
            }

        else:
            error = "❌ No city found"

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)