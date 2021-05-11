from flask import redirect, render_template, url_for, jsonify
from app.models import Dataset, Spesifik
from sklearn import metrics
from sklearn import svm
from sklearn.svm import SVC
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics

sc = MinMaxScaler()


def index():
    spesifik = Spesifik.get_all()
    # a = 15
    # bin_ = '{0:016b}'.format(a)
    # print(bin_)
    return render_template('pages/svm/index.html', spesifik=spesifik)


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


def check(data):
    dataset_jenis = Dataset.get_all_data_jenis()
    dataset_karakter = Dataset.get_all_data_karakter()

    n = len(data["id_arah_sayap"])
    a = data["id_jenis_sayap"]
    b = data["id_penempatan_sayap"]
    res_jenis = xor(a, b, n)
    c = data['id_jumlah_sayap']
    res_jenis = xor(res_jenis, c, n)
    d = data["id_arah_sayap"]
    res_jenis = xor(res_jenis, d, n)
    e = data["id_jenis_mesin"]
    res_jenis = xor(res_jenis, e, n)
    f = data["id_jumlah_mesin"]
    res_jenis = xor(res_jenis, f, n)
    g = data["id_posisi_mesin"]
    res_jenis = xor(res_jenis, g, n)
    h = data["id_badan_pesawat"]
    res_jenis = xor(res_jenis, h, n)
    i = data["id_bentuk_ekor_pesawat"]
    res_jenis = xor(res_jenis, i, n)
    j = data["id_jenis_landing_gear"]
    res_jenis = xor(res_jenis, j, n)

    l = data["id_persenjataan"]
    m = data["id_warna"]
    res_karakter = xor(l, m, n)

    dec_jenis = bin_to_decimal(res_jenis)
    dec_karakter = bin_to_decimal(res_karakter)

    scaled_jenis = scale_decimal(dataset_jenis, dec_jenis)
    scaled_dataset_jenis = scaled_jenis.iloc[:len(dataset_jenis)]
    norm_jenis = scaled_jenis.iloc[-1:]['norm'].values

    scaled_karakter = scale_decimal(dataset_karakter, dec_karakter)
    scaled_dataset_karakter = scaled_karakter.iloc[:len(dataset_karakter)]
    norm_karakter = scaled_karakter.iloc[-1:]['norm'].values

    result_jenis = calculate_svm(scaled_dataset_jenis, norm_jenis)
    result_karakter = calculate_svm(scaled_dataset_karakter, norm_karakter)

    identifikasi_pesawat = Dataset.get_data_pesawat(res_jenis, res_karakter)

    res = {
        "fusi_jenis_pesawat": res_jenis,
        "fusi_karakter_pesawat": res_karakter,
        "jenis_pesawat": result_jenis,
        "karakter_pesawat": result_karakter,
        "identifikasi_pesawat": identifikasi_pesawat
    }
    return jsonify(res)


def bin_to_decimal(binary):
    return int(binary, 2)

# def normalize_decimal(val, max_val, min_val):
#     return ((val - min_val)/(max_val - min_val))

def scale_decimal(data, input_dec):
    pdData = pd.DataFrame.from_dict(data)    
    pdDataInput = pd.DataFrame({
        "dec_fusi": [input_dec]
    })    
    pdData = pdData.append(pdDataInput, ignore_index=True)
    # print(pdData)
    scaled = sc.fit_transform(pdData['dec_fusi'].values.reshape(-1, 1))
    # print(scaled)
    pdData['norm'] = scaled.reshape(1, -1)[0]
    print(pdData['norm'])
    return pdData[['nama', 'norm']]


def calculate_svm(data, inp):
    X = data['norm'].values.reshape(-1, 1)
    y = data['nama'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    classifier = SVC(kernel="rbf")
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    accuracy = metrics.accuracy_score(y_test, y_pred)
    if (accuracy > 0.7):
        y_result = classifier.predict(np.reshape(inp, (-1, 1)))
        return y_result[0]
    else:
        calculate_svm(data, inp)
