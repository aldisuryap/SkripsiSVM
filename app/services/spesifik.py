from flask import redirect, render_template, url_for
from app.models import Karakteristik, Spesifik

def index():
    karakteristik = Karakteristik.get_all()
    spesifik = Spesifik.get_all()
    return render_template('pages/spesifik/index.html', spesifik = spesifik, karakteristik = karakteristik)

def store(data):
    insert = Spesifik.store(data)
    return redirect(url_for("spesifik_index"))

def update(data, id):  
    update = Spesifik.update(data,id)
    return redirect(url_for("spesifik_index"))

def delete(id):
    delete = Spesifik.delete(id)
    return redirect(url_for("spesifik_index"))