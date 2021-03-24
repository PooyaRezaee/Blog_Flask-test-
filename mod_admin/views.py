from . import admin
from flask import session,render_template,request,abort,flash,redirect,url_for
from mod_users.forms import Loginform
from mod_users.models import User
from mod_blog.forms import Postform
from mod_blog.models import Post
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
            return "s"
        
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