import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key="AIzaSyDtYLQcJaHmZNJZlEQdXK5NCUeG_BVSiRQ")

app = Flask(_name_)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            f"Check this information: '{user_input}'. "
            "Tell me if it's true, false, or misleading, and explain clearly."
        )
        result = response.text
    return render_template("index.html", result=result)

if _name_ == "_main_":
    app.run(debug=True, port=9000)
from flask_ngrok import run_with_ngrok
run_with_ngrok(app) 
app.run()