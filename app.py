from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Render the HTML file

@app.route("/translate", methods=["POST"])
def submit():
    # Get the text input from the form
    translated_text = request.form["textInput"]
    return redirect(url_for("home", translated_text=translated_text))
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)