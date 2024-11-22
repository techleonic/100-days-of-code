import os.path

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed, FileRequired
import requests
from flask import Flask, render_template, redirect,request,url_for
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)
# screate key that protects forms
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress a warning
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///shoes.db'
app.config["UPLOAD_FOLDER"] = "static/uploads"

#wrap
Bootstrap5(app)

#Declare the base for reusing
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# db Models
class Shoe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    filename: Mapped[str] = mapped_column(String(100),nullable=False)

with app.app_context():
    db.create_all()

# WTf forms
class addshoe(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=250)], render_kw={"placeholder":"Title product"})
    description =  StringField("Description", validators=[DataRequired(), Length(max=500)], render_kw={"class" : "Message","placeholder":"Description"})
    price = FloatField("Price", validators=[DataRequired()], render_kw={"placeholder": "Price"})
    image = FileField("image", validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'png'],'images only')])
    submit = SubmitField("Add")

class editshoe(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=250)], render_kw={"placeholder":"Title product"})
    description =  StringField("Description", validators=[DataRequired(), Length(max=500)], render_kw={"class" : "Message","placeholder":"Description"})
    price = FloatField("Price", validators=[DataRequired()], render_kw={"placeholder": "Price"})
    image = FileField("image", validators=[ FileAllowed(['jpg', 'jpeg', 'png'],'images only')])
    submit = SubmitField("Edit")
@app.route("/")
def index():
    result = db.session.execute(db.select(Shoe))
    all_shoes = result.scalars().all()
    return render_template("index.html",shoes = all_shoes)

@app.route("/add", methods = ["GET","POST"])
def add():
    form =  addshoe()
    title =form.title.data
    description = form.description.data
    price = form.price.data
    file = form.image.data
    if form.validate_on_submit():
        if file:
            filename = secure_filename(file.filename)
            filepath =  os.path.join(app.config["UPLOAD_FOLDER"],filename)
            file.save(filepath)

            new_shoe =  Shoe(
                title= title,
                description= description,
                price = price,
                filename = f"{app.config["UPLOAD_FOLDER"]}/{filename}"

            )
            db.session.add(new_shoe)
            db.session.commit()

        # result = db.session.execute(db.select(Shoe))
        # all_shoes = result.scalars().all()
        # db.session.commit()
        redirect("shoe_table")
    return render_template("add.html", form=form)

@app.route("/shoetable")
def shoe_table():
    result = db.session.execute(db.select(Shoe))
    all_shoes = result.scalars().all()
    db.session.commit()
    return  render_template("shoe_table.html", shoes = all_shoes)

@app.route("/delete")
def delete_item():
    if request.method == 'GET':
        shoe_id = request.args.get("id")
        shoe = db.get_or_404(Shoe,shoe_id)
        return render_template ("delete.html", shoe = shoe)
    else:
        request.args.get("id")

@app.route("/delete_complete")
def delete_complete():
    shoe_id = request.args.get("id")
    shoe =  db.get_or_404(Shoe, shoe_id)
    db.session.delete(shoe)
    db.session.commit()
    return redirect(url_for("shoe_table"))

@app.route("/edit", methods=["GET","POST"])
def edit():
    form = editshoe()
    shoe_id = request.args.get("id")
    shoe = db.get_or_404(Shoe, shoe_id)
    if form.validate_on_submit():
        shoe.title = form.title.data
        shoe.description = form.description.data
        shoe.price = form.price.data
        file = form.image.data
        if file:
            filename = secure_filename(file.filename)
            filepath =  os.path.join(app.config["UPLOAD_FOLDER"],filename)
            file.save(filepath)
            shoe.filename = f"{app.config["UPLOAD_FOLDER"]}/{filename}"
        db.session.commit()
        return redirect(url_for("shoe_table"))

    form.title.data = shoe.title
    form.description.data = shoe.description
    form.price.data = shoe.price
    return render_template("edit.html", form=form, img=shoe.filename)




if __name__ == "__main__":
    app.run(debug=True)