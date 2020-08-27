from flask import render_template, request, Blueprint
from bloggen.models import Blogpost, User, Postcategory

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    qty_posts = Blogpost.query.count()
    qty_cats = Postcategory.query.count()
    qty_users = User.query.count()
    # blog_posts = Blogpost.query.order_by(Blogpost.date.desc()).limit(10).paginate(page=page, per_page=5)
    blog_posts = Blogpost.query.order_by(Blogpost.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', blog_posts=blog_posts, qty_posts=qty_posts, qty_cats=qty_cats, qty_users=qty_users)


@core.route('/about')
def about():
    return render_template('about.html')