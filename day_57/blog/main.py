from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    data  = requests.get(url='https://api.npoint.io/77ce78574df762eb727e#').json()
    return render_template("index.html",posts=data)

@app.route("/post/<num>")
def get_post(num):
    print(num)
    data = requests.get(url='https://api.npoint.io/77ce78574df762eb727e#').json()
    blog_data = data[int(num)-1]
    return render_template("post.html", blog = blog_data)

if __name__ == "__main__":
    app.run(debug=True)
