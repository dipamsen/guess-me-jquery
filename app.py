from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

data = [
    {
        "word": "France",
        "category": "Country"
    },
    {
        "word": "Germany",
        "category": "Country"
    },
    {
        "word": "Italy",
        "category": "Country"
    },
    {
        "word": "Japan",
        "category": "Country"
    },
    {
        "word": "Russia",
        "category": "Country"
    },
    {
        "word": "Spain",
        "category": "Country"
    },
    {
        "word": "Sweden",
        "category": "Country"
    },
    {
        "word": "United Kingdom",
        "category": "Country"
    },
    {
        "word": "United States",
        "category": "Country"
    },
    {
        "word": "Australia",
        "category": "Country"
    },
    {
        "word": "Canada",
        "category": "Country"
    },
    {
        "word": "China",
        "category": "Country"
    },
    {
        "word": "India",
        "category": "Country"
    },
    {
        "word": "Mexico",
        "category": "Country"
    },
    {
        "word": "New Zealand",
        "category": "Country"
    },
    {
        "word": "South Africa",
        "category": "Country"
    },
    {
        "word": "Argentina",
        "category": "Country"
    },
    {
        "word": "Brazil",
        "category": "Country"
    },
    {
        "word": "Chile",
        "category": "Country"
    },
    {
        "word": "Colombia",
        "category": "Country"
    },
    {
        "word": "Costa Rica",
        "category": "Country"
    },
    {
        "word": "Cuba",
        "category": "Country"
    },
    {
        "word": "Dominican Republic",
        "category": "Country"
    },
    {
        "word": "Chess",
        "category": "Sports"
    },
    {
        "word": "Cricket",
        "category": "Sports"
    },
    {
        "word": "Football",
        "category": "Sports"
    },
    {
        "word": "Golf",
        "category": "Sports"
    },
    {
        "word": "Hockey",
        "category": "Sports"
    },
    {
        "word": "Rugby",
        "category": "Sports"
    },
    {
        "word": "Tennis",
        "category": "Sports"
    },
    {
        "word": "Baseball",
        "category": "Sports"
    },
    {
        "word": "Basketball",
        "category": "Sports"
    },
    {
        "word": "Boxing",
        "category": "Sports"
    },
    {
        "word": "Cricket",
        "category": "Sports"
    },
    {
        "word": "Cycling",
        "category": "Sports"
    },
    {
        "word": "Darts",
        "category": "Sports"
    },
    {
        "word": "Fencing",
        "category": "Sports"
    },
    {
        "word": "Golf",
        "category": "Sports"
    },
    {
        "word": "JavaScript",
        "category": "Programming Language"
    },
    {
        "word": "Java",
        "category": "Programming Language"
    },
    {
        "word": "Lisp",
        "category": "Programming Language"
    },
    {
        "word": "Perl",
        "category": "Programming Language"
    },
    {
        "word": "PHP",
        "category": "Programming Language"
    },
    {
        "word": "Python",
        "category": "Programming Language"
    },
    {
        "word": "Ruby",
        "category": "Programming Language"
    },
    {
        "word": "Scala",
        "category": "Programming Language"
    },
    {
        "word": "Swift",
        "category": "Programming Language"
    },
    {
        "word": "Assembly",
        "category": "Programming Language"
    },
    {
        "word": "Bash",
        "category": "Programming Language"
    },
    {
        "word": "CoffeeScript",
        "category": "Programming Language"
    },
    {
        "word": "CSS",
        "category": "Programming Language"
    },
    {
        "word": "Dart",
        "category": "Programming Language"
    },
    {
        "word": "Haskell",
        "category": "Programming Language"
    },
    {
        "word": "HTML",
        "category": "Programming Language"
    }
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get-template")
def get_template():
    return jsonify({"status": "success", "word": random.choice(data)})


if __name__ == "__main__":
    app.run(debug=True)
