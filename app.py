from flask import Flask, request, render_template, redirect, url_for
from model import TranslateGPTModel

app = Flask(__name__)
model = TranslateGPTModel()

@app.route("/")
def home():
    return render_template("index.html")  # Render the HTML file

@app.route("/describe", methods=["POST"])
def submit():
    # Get the text input from the form
    text = request.form["text"]
    styles = model.describe(text)
    return redirect(url_for("home", text=text, styles=styles))

@app.route("/translate_or_generate", methods=["POST"])
def translate():
    # Translate the given texts based on the adjectives
    text = request.form["input_text"]
    styles = request.form["styles"]
    language = request.form["language1"]
    action = request.form["action"]
    if action == "translate":  
        translation = model.translate(text, styles, language)
        return redirect(url_for("home", text=text, styles=styles, translation=translation))
    elif action == "generate":
        generate = model.generate(styles, language)
        return redirect(url_for("home", text=text, styles=styles, generate=generate))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)