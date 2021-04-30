from flask import redirect, render_template, url_for
from app.models import Dataset, Karakteristik, Spesifik, Jenis_pesawat

def index():
    dataset = Dataset.get_all()
    return render_template('pages/dataset/index.html', dataset = dataset)

def create():
    karakteristik = Karakteristik.get_all()
    spesifik = Spesifik.get_all()
    jenis_pesawat = Jenis_pesawat.get_all()
    return render_template('pages/dataset/create.html', karakteristik = karakteristik, spesifik = spesifik, jenis_pesawat = jenis_pesawat)

def upload(data):
    Dataset.store(data)
    return redirect(url_for("dataset_index"))

def store(data):
     n = len(data["Jenis Sayap"])
     a = data["Jenis Sayap"]
     b = data["Penempatan Sayap"]
     res_a = xor(a,b,n)
     c = data['Jumlah Sayap']
     res_a = xor(res_a,c,n)
     d = data["Arah Sayap"]
     res_a = xor(res_a,d,n)
     e = data["Jenis Mesin"]
     res_a = xor(res_a,e,n)
     f = data["Jumlah Mesin"]
     res_a = xor(res_a,f,n)
     g = data["Posisi Mesin"]
     res_a = xor(res_a,g,n)
     h = data["Badan Pesawat"]
     res_a = xor(res_a,h,n)
     i = data["Bentuk Ekor Pesawat"]
     res_a = xor(res_a,i,n)
     j = data["Jenis Landing Gear"]
     res_a = xor(res_a,j,n)
     k = data["Canard"]
     res_a = xor(res_a,k,n)
     l = data["Persenjataan"]
     res_a = xor(res_a,l,n)
     m = data["Warna"]
     res_a = xor(res_a,m,n)
     data_ = {
         "fusi_informasi": res_a,
         "data": data
     }
    #  return data_['data']['Jenis Sayap']
     insert = Dataset.store(data_)
     return redirect(url_for("dataset_index"))

def xor(a, b, n):
    ans = ""
      
    # Loop to iterate over the
    # Binary Strings
    for i in range(n):
          
        # If the Character matches
        if (a[i] == b[i]): 
            ans += "0"
        else: 
            ans += "1"
    return ans