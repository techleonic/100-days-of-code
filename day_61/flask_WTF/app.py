from flask import Flask, render_template, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, FloatField,
                     BooleanField, DateField, DateTimeField, SelectField,
                     SelectMultipleField, RadioField, PasswordField, EmailField, SubmitField)
from wtforms.validators import DataRequired, Length, Email, NumberRange

app = Flask(__name__)
app.secret_key = 'your_secret_key'


# Define the WTForms form with various field types and validations
class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)], render_kw={"class": "form-control", "placeholder": "Enter your name"})
    bio = TextAreaField('Bio', validators=[Length(max=200)], render_kw={"class": "form-control", "placeholder": "Tell us about yourself"})
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=120)], render_kw={"class": "form-control", "placeholder": "Enter your age"})
    salary = FloatField('Salary', validators=[NumberRange(min=0)], render_kw={"class": "form-control", "placeholder": "Enter your salary"})
    email = EmailField('Email', validators=[DataRequired(), Email()], render_kw={"class": "form-control", "placeholder": "Enter your email"})
    birthday = DateField('Birthday', format='%Y-%m-%d', render_kw={"class": "form-control", "placeholder": "YYYY-MM-DD"})
    remember_me = BooleanField('Remember Me', render_kw={"class": "form-check-input"})
    status = RadioField('Status', choices=[('active', 'Active'), ('inactive', 'Inactive')], render_kw={"class": "form-check-input"})
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female')], render_kw={"class": "form-select"})
    hobbies = SelectMultipleField('Hobbies', choices=[('coding', 'Coding'), ('sports', 'Sports')], render_kw={"class": "form-control"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)], render_kw={"class": "form-control", "placeholder": "Create a password"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ProfileForm()
    if form.validate_on_submit():
        # Store form data in session to display in table
        session['submitted_data'] = {
            'name': form.name.data,
            'bio': form.bio.data,
            'age': form.age.data,
            'salary': form.salary.data,
            'email': form.email.data,
            'birthday': form.birthday.data.strftime('%Y-%m-%d') if form.birthday.data else '',
            'remember_me': form.remember_me.data,
            'status': form.status.data,
            'gender': form.gender.data,
            'hobbies': ', '.join(form.hobbies.data),
        }
        flash("Form submitted successfully!", "success")
        return redirect(url_for('index'))

    # Retrieve submitted data from the session for display
    submitted_data = session.get('submitted_data')
    return render_template('form.html', form=form, submitted_data=submitted_data)


if __name__ == '__main__':
    app.run(debug=True)
