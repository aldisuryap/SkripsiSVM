from flask import redirect, render_template, url_for
from app.models import Karakteristik
import bcrypt

def index():
    karakteristik = Karakteristik.get_all()
    return render_template('pages/karakteristik/index.html', karakteristik = karakteristik)

def store(data):
    insert = Karakteristik.store(data)
    return redirect(url_for("karakteristik_index"))

def update(data, id):  
    update = Karakteristik.update(data,id)
    return redirect(url_for("karakteristik_index"))

def delete(id):
    delete = Karakteristik.delete(id)
    return redirect(url_for("karakteristik_index"))