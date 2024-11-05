import html
import json

from flask import Flask,  render_template, redirect, url_for, flash ,request
import sqlite3
from flask_wtf import  FlaskForm
from wtforms import  StringField, FloatField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

con = sqlite3.connect("instance/books.db", check_same_thread=False)
cur = con.cursor()

# cur.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, price FLOAT NOT NULL)")
# list_of_books = [
#     (1,"Learn Enough Python to Be Dangerous","Michael Hartl",31.99),
#     (2,"Flask Web Development with Python","Leire Verdugo",9.99)
# ]
#
# cur.executemany("INSERT INTO 'books' VALUES (?,?,?,?)",list_of_books)
# con.commit()

cur.execute("SELECT * from 'books'")
print( cur.fetchall())

app = Flask(__name__)
app.config["SECRET_KEY"] = "1234567"
class addform(FlaskForm):
    title = StringField("Title", validators=[DataRequired()],render_kw={"class": "form-control", "placeholder": "Enter Book Title"})
    author =  StringField("Author", validators=[DataRequired(),Length(max=50)], render_kw={"class": "form-control", "placeholder": "Enter Book name"})
    prince =  FloatField("Price", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": "Enter Book price"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})

@app.route("/", methods=['GET','POST'])
def index():
    form = addform()
    if form.validate_on_submit():
        print("validated")
        title = form.title.data
        author= form.author.data
        price = form.prince.data
        book={
            "tile": title,
            "author": author,
            "price": price,
        }

        sql_query = 'INSERT INTO books(id, title, author, price) VALUES (?, ?, ?, ?)'
        cur.execute("SELECT MAX(id) FROM 'books'")
        last_id = int(cur.fetchone()[0]) +1
        print(last_id)
        vals = (last_id, title, author, float(price))
        cur.execute(sql_query, vals)
        con.commit()


        return render_template("save.html",book=book)
    return render_template("index.html", form=form)


@app.route("/books")
def books():
    cur.execute("SELECT * FROM 'books'")
    list_of_books = cur.fetchall()
    return render_template("books.html", books = list_of_books)


if __name__ == "__main__":
    app.run(debug=True)