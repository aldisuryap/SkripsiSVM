from flask import redirect, render_template, url_for
from app.models import Jenis_pesawat

def index():
    jenis_pesawat = Jenis_pesawat.get_all()
    return render_template('pages/jenis_pesawat/index.html', jenis_pesawat = jenis_pesawat)

def store(data):
    insert = Jenis_pesawat.store(data)
    return redirect(url_for("jenis_pesawat_index"))

def update(data, id):  
    update = Jenis_pesawat.update(data,id)
    return redirect(url_for("jenis_pesawat_index"))

def delete(id):
    delete = Jenis_pesawat.delete(id)
    return redirect(url_for("jenis_pesawat_index"))