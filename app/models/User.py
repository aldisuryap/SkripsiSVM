from app.config import db

def get_all():
    try:
        conn = db.conn()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM tbl_user ORDER BY username ASC"
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
            sql = "SELECT * FROM tbl_user WHERE id_user=%s"
            cursor.execute(sql, (id))
        conn.commit()
    except Exception as e:
        print("Exception occured:{}".format(e))
        return False
    finally:
        conn.close()
        return cursor.fetchone()

def get_by_username(username):
    try:
        conn = db.conn()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM tbl_user WHERE username=%s"
            cursor.execute(sql, (username))
        conn.commit()
        conn.close()
        return cursor.fetchone()
    except Exception as e:
        print("Exception occured:{}".format(e))
        return False

def store(data):
    try:
        conn = db.conn()
        with conn.cursor() as cursor:
            sql = "INSERT INTO tbl_user (`nama_user`,`username`,`password`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (data['nama_user'], data['username'], data['password']))
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
			old_password = data['old_password']
			if old_password != None and old_password != "":
				sql = "UPDATE tbl_user SET nama_user=%s, username=%s, password=%s WHERE id_user=%s"
				cursor.execute(sql, (data['name'], data['username'], data['password'], id))
			else:
				sql = "UPDATE tbl_user SET nama_user=%s, username=%s WHERE id_user=%s"
				cursor.execute(sql, (data['name'], data['username'], id))
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
            sql = "DELETE FROM tbl_user WHERE id_user=%s"
            cursor.execute(sql, (id))
        conn.commit()
    except Exception as e:
        print("Exception occured:{}".format(e))
        return False
    finally:
        conn.close()
        return True
        
