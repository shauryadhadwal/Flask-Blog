from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '45385b37d4fd30237a8f76696fba1bf3'

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


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login',form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register',form=form)


if __name__ == "__main__":
    app.run(debug=True)