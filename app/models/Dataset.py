from app.config import db


def get_all():
    try:
        conn = db.conn()
        with conn.cursor() as cursor:
            # sql = "SELECT a.nama_pesawat as z_nama_pesawat, b.nama_jenis_pesawat as z_nama_jenis_pesawat, c.spesifik as jenis_sayap, d.spesifik as jenis_penempatan_sayap, e.spesifik as jumlah_sayap, f.spesifik as arah_sayap, g.spesifik as jenis_mesin, h.spesifik as jumlah_mesin, i.spesifik as posisi_mesin, j.spesifik as badan_pesawat, k.spesifik as jenis_ekor, l.spesifik as jenis_landing_gear, m.spesifik as canard, n.spesifik as persenjataan, o.spesifik as warna, a.fusi_informasi FROM tbl_pesawat a JOIN tbl_jenis_pesawat b ON a.id_jenis_pesawat = b.id_jenis_pesawat JOIN tbl_spesifik c ON a.id_jenis_sayap = c.bit_spesifik JOIN tbl_spesifik d ON a.id_jenis_penempatan_sayap = d.bit_spesifik JOIN tbl_spesifik e ON a.id_jumlah_sayap = e.bit_spesifik JOIN tbl_spesifik f ON a.id_arah_sayap = f.bit_spesifik JOIN tbl_spesifik g ON a.id_jenis_mesin = g.bit_spesifik JOIN tbl_spesifik h ON a.id_jumlah_mesin = h.bit_spesifik JOIN tbl_spesifik i ON a.id_posisi_mesin = i.bit_spesifik JOIN tbl_spesifik j ON a.id_badan_pesawat = j.bit_spesifik JOIN tbl_spesifik k ON a.id_jenis_ekor = k.bit_spesifik JOIN tbl_spesifik l ON a.id_jenis_landing_gear = l.bit_spesifik JOIN tbl_spesifik m ON a.id_canard = m.bit_spesifik JOIN tbl_spesifik n ON a.id_persenjataan = n.bit_spesifik JOIN tbl_spesifik o ON a.id_warna = o.bit_spesifik"
            sql = "SELECT * FROM tbl_pesawat a JOIN tbl_jenis_pesawat b ON a.id_jenis_pesawat = b.id_jenis_pesawat JOIN tbl_karakter_pesawat c ON a.id_karakter_pesawat = c.id_karakter_pesawat"
            cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print("Exception occured:{}".format(e))
        return False
    finally:
        conn.close()
        return cursor.fetchall()


def get_all_data_jenis():
    try:
        conn = db.conn()
        with conn.cursor() as cursor:
            sql = "SELECT nama_jenis_pesawat nama, dec_jenis_pesawat dec_fusi FROM tbl_pesawat a JOIN tbl_jenis_pesawat b ON a.id_jenis_pesawat = b.id_jenis_pesawat"
            cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print("Exception occured:{}".format(e))
        return False
    finally:
        conn.close()
        return cursor.fetchall()


def get_all_data_karakter():
    try:
        conn = db.conn()
        with conn.cursor() as cursor:
            sql = "SELECT nama_karakter_pesawat nama, dec_karakter_pesawat dec_fusi FROM tbl_pesawat a JOIN tbl_karakter_pesawat b ON a.id_karakter_pesawat = b.id_karakter_pesawat"
            cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print("Exception occured:{}".format(e))
        return False
    finally:
        conn.close()
        return cursor.fetchall()


def store(data):
    try:
        conn = db.conn()
        cursor = conn.cursor()
        sql = "INSERT INTO tbl_pesawat (`nama_pesawat`,`id_jenis_pesawat`,`id_karakter_pesawat`,`id_jenis_sayap`,`id_jenis_penempatan_sayap`,`id_jumlah_sayap`,`id_arah_sayap`,`id_jenis_mesin`,`id_jumlah_mesin`,`id_posisi_mesin`,`id_badan_pesawat`,`id_jenis_ekor`,`id_jenis_landing_gear`,`id_persenjataan`,`id_warna`,`fusi_jenis_pesawat`, `fusi_karakter_pesawat`, `dec_jenis_pesawat`, `dec_karakter_pesawat`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        for i in data.itertuples():
            nama_pesawat = i[1]
            jenis_pesawat = 1 if i[2] == "Pesawat" else 2
            karakter_pesawat = 1 if i[3] == "Sipil" else 2
            id_jenis_sayap = i[4]
            id_jenis_penempatan_sayap = i[5]
            id_jumlah_sayap = i[6]
            id_arah_sayap = i[7]
            id_jenis_mesin = i[8]
            id_jumlah_mesin = i[9]
            id_posisi_mesin = i[10]
            id_badan_pesawat = i[11]
            id_jenis_ekor = i[12]
            id_jenis_landing_gear = i[13]
            id_persenjataan = i[14]
            id_warna = i[15]
            fusi_jenis_pesawat = i[16]
            fusi_karakter_pesawat = i[17]
            dec_jenis_pesawat = i[18]
            dec_karakter_pesawat = i[19]

            values = (nama_pesawat, jenis_pesawat, karakter_pesawat, id_jenis_sayap, id_jenis_penempatan_sayap, id_jumlah_sayap, id_arah_sayap, id_jenis_mesin, id_jumlah_mesin, id_posisi_mesin,
                      id_badan_pesawat, id_jenis_ekor, id_jenis_landing_gear, id_persenjataan, id_warna, fusi_jenis_pesawat, fusi_karakter_pesawat, dec_jenis_pesawat, dec_karakter_pesawat)

            cursor.execute(sql, values)

        conn.commit()
    except Exception as e:
        print("Exception occured:{}".format(e))
        return False
    finally:
        conn.close()
        return True


def get_data_pesawat(fusi_jenis_pesawat, fusi_karakter_pesawat):
    try:
        conn = db.conn()
        with conn.cursor() as cursor:
            sql = "SELECT nama_pesawat nama FROM tbl_pesawat WHERE fusi_jenis_pesawat = %s AND fusi_karakter_pesawat = %s"
            cursor.execute(sql, (fusi_jenis_pesawat, fusi_karakter_pesawat))
        conn.commit()
    except Exception as e:
        print("Exception occured:{}".format(e))
        return False
    finally:
        conn.close()
        return cursor.fetchall()
