from app import app

@app.route('/')
def Home():
    return "This is Home Page ..."