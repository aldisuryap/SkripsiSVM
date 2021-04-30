from app.config import db

def get_all():
    try:
        conn = db.conn()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM tbl_karakteristik ORDER BY id ASC"
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
            sql = "SELECT * FROM tbl_karakteristik WHERE id=%s"
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
            sql = "INSERT INTO tbl_karakteristik (`name`) VALUES (%s)"
            cursor.execute(sql, (data['name']))
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
            sql = "UPDATE tbl_karakteristik SET name=%s WHERE id=%s"
            cursor.execute(sql, (data['name'], id))
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
            sql = "DELETE FROM tbl_karakteristik WHERE id=%s"
            cursor.execute(sql, (id))
        conn.commit()
    except Exception as e:
        print("Exception occured:{}".format(e))
        return False
    finally:
        conn.close()
        return True
        
