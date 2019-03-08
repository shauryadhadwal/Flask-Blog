from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
def home():
    """ Home Page Route for the application. Also serves as the dashboard """
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(per_page=2, page=page)
    return render_template('home.html', title='Home', posts=posts)


@main.route("/about")
def about():
    """ About Page Route for the applcation."""
    return render_template('about.html', title='About')

