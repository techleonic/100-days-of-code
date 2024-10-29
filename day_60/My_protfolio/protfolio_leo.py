from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/components')
def get_components():
    return render_template('components.html')

@app.route("/estimate")
def get_estimate():
    return render_template("estimate_form.html")

@app.route("/send_estimate", methods=["POST"])
def estimate_proc():
    email =  request.form["email"]
    password = request.form["password"]
    return f"<h1>{email} {password} </h1>"

if __name__ == "__main__":
    app.run(debug=True)