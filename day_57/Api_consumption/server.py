from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return  render_template("index.html")

@app.route("/guess/<name>")
def guess(name):
    gender_json=requests.get(url=f"https://api.genderize.io?name={name}").json()
    age_json=  requests.get(url=f"https://api.agify.io?name={name}").json()
    return render_template("guess.html",person_name = name, age = age_json['age'], gender = gender_json['gender'])
@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    data = requests.get(url='https://api.npoint.io/77ce78574df762eb727e#').json()
    return render_template("blog.html", posts = data)

if __name__ == "__main__":
    app.run(debug=True)