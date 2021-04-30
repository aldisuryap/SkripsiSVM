from app.config import db

def get_all():
    try:
        conn = db.conn()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM tbl_spesifik a JOIN tbl_karakteristik b ON a.id_karakteristik = b.id ORDER BY id_spesifik ASC"
            cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print("Exception occured:{}".format(e))
        return False
    finally:
        conn.close()
        return cursor.fetchall()

def get_one(id):
    try:
        conn = db.conn()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM tbl_spesifik a JOIN tbl_karakteristik b ON a.id_karakteristik = b.id WHERE id_spesifik=%s"
            cursor.execute(sql, (id))
        conn.commit()
    except Exception as e:
        print("Exception occured:{}".format(e))
        return False
    finally:
        conn.close()
        return cursor.fetchone()

def store(data):
    try:
        conn = db.conn()
        with conn.cursor() as cursor:
            sql = "INSERT INTO tbl_spesifik (`id_karakteristik`,`kode_spesifik`,`spesifik`,`bit_spesifik`) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, (data['id_karakteristik'], data['kode_spesifik'], data['spesifik'], data['bit_spesifik']))
        conn.commit()
    except Exception as e:
        print("Exception occured:{}".format(e))
        return False
    finally:
        conn.close()
        return True

def update(data, id):
    try:
        conn = db.conn()
        with conn.cursor() as cursor:
            sql = "UPDATE tbl_spesifik SET id_karakteristik=%s, kode_spesifik=%s, spesifik=%s, bit_spesifik=%s WHERE id_spesifik=%s"
            cursor.execute(sql, (data['id_karakteristik'], data['kode_spesifik'], data['spesifik'], data['bit_spesifik'], id))
            conn.commit()
    except Exception as e:
        print("Exeception occured:{}".format(e))
        return False
    finally:
        conn.close()
        return True

def delete(id):
    try:
        conn = db.conn()
        with conn.cursor() as cursor:
            sql = "DELETE FROM tbl_spesifik WHERE id_spesifik=%s"
            cursor.execute(sql, (id))
        conn.commit()
    except Exception as e:
        print("Exception occured:{}".format(e))
        return False
    finally:
        conn.close()
        return True
        
