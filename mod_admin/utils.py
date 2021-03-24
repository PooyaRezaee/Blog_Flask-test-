from flask import session,abort
from functools import wraps

def only_admin_see(func):
    @wraps(func)
    def wrapper(*args,**keywargs):
        if session.get("rol") == "admin":
            return func(*args,**keywargs)
        else:
            abort(403)
    
    return wrapper