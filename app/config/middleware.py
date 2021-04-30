from functools import wraps
from flask import session, redirect, url_for

def checkLogin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        else:
            return func(*args, **kwargs)

    return decorated_function