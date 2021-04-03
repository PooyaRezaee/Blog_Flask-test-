from . import admin
from flask import session,render_template,request,abort,flash,redirect,url_for
from mod_users.forms import Loginform
from mod_users.models import User
from mod_blog.forms import Postform,Categoryform
from mod_blog.models import Post,Category
from .utils import only_admin_see
from app import db


@admin.route("/")
@only_admin_see
def index():
    return render_template("admin/index.html",name=session.get('name'))

@admin.route("/login/",methods=["GET","POST"])
def login():
    # session['name'] = "pooya"
    login_form = Loginform(request.form)

    if request.method == "POST":
        if not login_form.validate_on_submit():
            abort(400)
        user = User.query.filter(User.Email.ilike(f"{login_form.email.data}")).first()
        if not user:
            flash("Email is Wrong",category="error")
            return render_template("admin/login.html",login_form=login_form) 
        if not user.check_password(login_form.password.data):
            flash("Passowrd is Wrong",category="error")
            return render_template("admin/login.html",login_form=login_form)
        if not user.is_admin():
            flash("You not admin",category="error")
            return render_template("admin/login.html",login_form=login_form)
        session["email"] = user.Email
        session["id"] = user.Id
        session["rol"] = user.rol
        session["name"] = user.full_name
        return redirect(url_for("admin.index"))
    
    if session.get('rol') == "admin":
        return redirect(url_for("admin.index"))

    return render_template("admin/login.html",login_form=login_form)


@admin.route("/logout/",methods=["GET"])
def log_out():
    session.clear()
    flash("Logout Done","warning")
    return redirect(url_for("admin.login"))

@admin.route('/posts/new/',methods=["GET","POST"])
@only_admin_see
def new_post():
    form = Postform(request.form)

    if request.method == "POST":
        if not form.validate_on_submit():
            flash("Write on all Filed")
            return render_template('admin/create_post.html',form=form)
        
        new_post = Post()
        new_post.title = form.title.data
        new_post.summary = form.summary.data
        new_post.content = form.content.data
        new_post.slug = form.slug.data

        try:
            db.session.add(new_post)
            db.session.commit()
            flash("Created Post")
            return redirect(url_for('admin.index'))
        except:
            flash("has a error","error")
            return render_template('admin/create_post.html',form=form)

    elif request.method == "GET":
        return render_template('admin/create_post.html',form=form)

@admin.route('/users/')
@only_admin_see
def list_users():
    users = User.query.order_by(User.Id.desc()).all()

    return render_template('admin/list_users.html',users=users)

@admin.route('/posts/')
@only_admin_see
def list_posts():
    posts = Post.query.order_by(Post.id.desc()).all()

    return render_template('admin/list_posts.html',posts=posts)

@admin.route('/posts/delete/<int:post_id>/')
@only_admin_see
def delate_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    flash('Post delated')
    return redirect(url_for('admin.list_posts'))

@admin.route('/posts/modify/<int:post_id>/',methods=["GET","POST"])
@only_admin_see
def modify_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = Postform(obj=post)

    if request.method == "POST":
        if not form.validate_on_submit():
            flash("Form not Validate")

        post.title = form.title.data
        post.summary = form.summary.data
        post.content = form.content.data
        post.slug = form.slug.data

        try:
            db.session.commit()
            flash("post Modifided")
            return redirect(url_for('admin.index'))
    
        except:
            flash("has a error","error")
    
    return render_template('admin/modify_post.html',form=form ,post=post)

@admin.route('/categories/new/',methods=["GET","POST"])
@only_admin_see
def new_category():
    form = Categoryform(request.form)

    if request.method == "POST":
        if not form.validate_on_submit():
            flash("Write on all Filed")
            return render_template('admin/create_category.html',form=form)
        
        new_category = Category()
        new_category.name = form.name.data
        new_category.slug = form.slug.data
        new_category.description = form.description.data

        try:
            db.session.add(new_category)
            db.session.commit()
            flash("Created Category")
            return redirect(url_for('admin.index'))
        except:
            flash("has a error","error")
            return render_template('admin/create_category.html',form=form)
    
    elif request.method == "GET":
        return render_template('admin/create_category.html',form=form)

@admin.route('/categories/')
@only_admin_see
def list_categories():
    categories = Category.query.order_by(Category.id.desc()).all()

    return render_template('admin/list_categories.html',categories=categories)

@admin.route('/categories/delete/<int:category_id>/')
@only_admin_see
def delate_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()

    flash('category delated')
    return redirect(url_for('admin.list_categories'))

@admin.route('/posts/categories/<int:category_id>/',methods=["GET","POST"])
@only_admin_see
def modify_category(category_id):
    category = Category.query.get_or_404(category_id)
    form = Categoryform(obj=category)

    if request.method == "POST":
        if not form.validate_on_submit():
            flash("Form not Validate")

        category.name = form.name.data
        category.description = form.description.data
        category.slug = form.slug.data

        try:
            db.session.commit()
            flash("category Modifided")
            return redirect(url_for('admin.list_categories'))
    
        except:
            flash("has a error","error")
    
    return render_template('admin/modify_category.html',form=form ,category=category)
