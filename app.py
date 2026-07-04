from flask import Flask, render_template, request
from youtube import get_channel_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    channel = request.form.get("channel")
    data = get_channel_data(channel)
    return render_template("dashboard.html", data=data)

@app.route("/compare")
def compare():
    return render_template("compare.html")

if __name__ == "__main__":
    app.run(debug=True)
