from flask import redirect, render_template, url_for
from app.models import User
import bcrypt

def index():
    users = User.get_all()
    return render_template('pages/user/index.html', users = users)

def store(data):
    if data['password'] == data['password1']:
        password = bcrypt.hashpw(data['password'].encode('utf8'), bcrypt.gensalt())
        user = {
            "nama_user": data['name'],
            "username": data['username'],
            "password": password
        }
        insert = User.store(user)
        return redirect(url_for("user_index"))
    else:
        return "Password doesn't match"

def update(data, id):
    user = User.get_one(id)
    old_password = data['old_password']
    if old_password != "" and old_password != None:
        if bcrypt.checkpw(old_password.encode('utf8'), user['password'].encode('utf8')):
            if data['password'] == data['password1']:
                password = bcrypt.hashpw(data['password'].encode('utf8'), bcrypt.gensalt())
                user = {
                    "name": data['name'],
                    "username": data['username'],
                    "password": password,
                    "old_password": old_password
                }
            else:
                return "New password doesn't match"
        else:
            return "Old password doesn't match"
    else:
        user = data
    
    update = User.update(user,id)
    return redirect(url_for("user_index"))

def delete(id):
    delete = User.delete(id)
    return redirect(url_for("user_index"))