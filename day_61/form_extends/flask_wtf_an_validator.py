from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, Request



app =  Flask(__name__)

@app.route("/")
def get_form():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)