from app import app,render_template

@app.route('/')
def Home():
    return render_template("index.html")