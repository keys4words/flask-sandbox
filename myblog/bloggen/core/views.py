from flask import render_template, redirect, url_for, request, Blueprint, flash, jsonify
from bloggen.models import Blogpost, User, Postcategory
from flask_login import current_user, login_required
from .forms import CreatepostForm
from bloggen import db


core = Blueprint('core', __name__)

@core.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    qty_posts = Blogpost.query.count()
    qty_cats = Postcategory.query.count()
    all_cats = Postcategory.query.all()
    qty_users = User.query.count()
    # blog_posts = Blogpost.query.order_by(Blogpost.date.desc()).limit(10).paginate(page=page, per_page=5)
    blog_posts = Blogpost.query.order_by(Blogpost.date.desc()).paginate(page=page, per_page=5)
    form = CreatepostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            blog_post = Blogpost(title=form.title.data,
                            text=form.text.data,
                            user_id=current_user.id)
            db.session.add(blog_post)
            db.session.commit()
            flash('Blog post has created!')
            return jsonify(status='ok')
        return redirect(url_for('blog_posts.posts'))
    return render_template('index.html', blog_posts=blog_posts, qty_posts=qty_posts, qty_cats=qty_cats, qty_users=qty_users, form=form, all_cats=all_cats)


@core.route('/about')
def about():
    return render_template('about.html')