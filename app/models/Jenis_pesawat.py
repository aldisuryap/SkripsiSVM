from app.config import db

def get_all():
    try:
        conn = db.conn()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM tbl_jenis_pesawat ORDER BY id_jenis_pesawat ASC"
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
            sql = "SELECT * FROM tbl_jenis_pesawat WHERE id_jenis_pesawat=%s"
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
            sql = "INSERT INTO tbl_jenis_pesawat (`nama_jenis_pesawat`) VALUES (%s)"
            cursor.execute(sql, (data['nama_jenis_pesawat']))
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
            sql = "UPDATE tbl_jenis_pesawat SET nama_jenis_pesawat=%s WHERE id_jenis_pesawat=%s"
            cursor.execute(sql, (data['nama_jenis_pesawat'], id))
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
            sql = "DELETE FROM tbl_jenis_pesawat WHERE id_jenis_pesawat=%s"
            cursor.execute(sql, (id))
        conn.commit()
    except Exception as e:
        print("Exception occured:{}".format(e))
        return False
    finally:
        conn.close()
        return True
        
