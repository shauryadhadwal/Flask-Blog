from flask import render_template, url_for, flash, redirect
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app

posts = [
    {
        'author': 'Shaurya Dhadwal',
        'title': 'Blog Post 1',
        'content' : 'First post Ever',
        'date_posted': 'April 20, 2018'
    },
     {
        'author': 'Shaurya Dhadwal',
        'title': 'Blog Post 1',
        'content' : 'First post Ever',
        'date_posted': 'April 20, 2018'
    },
     {
        'author': 'Shaurya Dhadwal',
        'title': 'Blog Post 1',
        'content' : 'First post Ever',
        'date_posted': 'April 20, 2018'
    }
]

@app.route("/")
def home():
    return render_template('home.html', title='Home', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'shauryadhadwal@gmail.com' and form.password.data == 'qwerty':
            flash(f'You have successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Either Password or Emailid is incorrect!', 'danger')

    return render_template('login.html', title='Login',form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register',form=form)
