from flask import render_template,request
from . import blog
from .models import Post,Category
from sqlalchemy import or_
from .forms import searchform

@blog.route('/')
def index():
    page = request.args.get('q',1,int)
    search_form = searchform()
    posts = Post.query.paginate(page,5).items
    num_pages = Post.query.paginate(page,5).pages

    return render_template('blog/index.html',posts=posts,search_form=search_form,num_pages=num_pages)


@blog.route('/<string:slug>')
def single_post(slug):
    search_form = searchform()
    post = Post.query.filter(Post.slug == slug).first_or_404()

    return render_template('blog/post.html',post=post,search_form=search_form)

@blog.route('/search/')
def search():
    search_form = searchform()
    search_query = request.args.get('search','')

    title_cond = Post.title.ilike(f"%{search_query}%")
    summary_cond = Post.summary.ilike(f"%{search_query}%")
    content_cond = Post.content.ilike(f"%{search_query}%")

    found_posts = Post.query.filter(or_(title_cond,summary_cond,content_cond)).all()

    print(found_posts)

    return render_template('blog/search.html',posts=found_posts,search_form=search_form,search_query=search_query)

@blog.route('/category/<string:slug>')
def single_category(slug):
    search_form = searchform()
    category = Category.query.filter(Category.slug == slug).first_or_404()

    return render_template('blog/single_category.html',posts=category.posts,search_form=search_form,category_name=category.name)

@blog.route('/category/')
def categories():
    search_form = searchform()
    categories = Category.query.all()

    return render_template('blog/categories.html',categories=categories,search_form=search_form)