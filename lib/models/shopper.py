from models.__init__ import (con, cur)

class Shopper():
    def __init__(self, username, password, id=None):
        self.username = username
        self.password = password
        self.id = id

    
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if isinstance(username, str):
            self._username = username
        else:
            print('username must be a string')
    
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        if isinstance(password, str) and len(password) > 4:
            self._password = password
        else:
            print('password must be a string, and at least 5 characters')


    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS shoppers (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
        );"""

        cur.execute(sql)
        con.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS shoppers;"""
        cur.execute(sql)
        con.commit()

    @classmethod
    def db_to_obj(cls, row):
        id, username, password = row 
        return cls(username, password, id)
    

    @classmethod
    def create_user(cls, username, password):
        shopper = cls(username, password)
        sql = """INSERT INTO shoppers (username, password) VALUES (?, ?)"""
        cur.execute(sql, (shopper.username, shopper.password))
        con.commit()

        return shopper
    
    @classmethod
    def delete_user(cls, id):
        sql = """DELETE FROM shoppers WHERE id = ?"""
        cur.execute(sql, (id,))
        con.commit()

    @classmethod
    def update_username(cls, username, id):
        sql = """UPDATE shoppers SET username = ? WHERE id = ?"""
        cur.execute(sql, (username, id,))
    
    @classmethod
    def update_password(cls, password, id):
        sql = """UPDATE shoppers SET password = ? WHERE id = ?"""
        cur.execute(sql, (password, id,))


    @classmethod
    def find_user_by_id(cls, id):
        sql = """SELECT * FROM shoppers WHERE id = ?"""
        row = cur.execute(sql, (id,)).fetchone()

        return row
    
    @classmethod
    def find_user_by_username(cls, username):
        sql = """SELECT * FROM shoppers WHERE username = ?"""
        row = cur.execute(sql, (username,)).fetchone()

        return cls.db_to_obj(row) if row else None
    
    @classmethod
    def check_username(cls, username):
        user = Shopper.find_user_by_username(username)
        if user == None:
            return False
        else:
            return True
    
    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM shoppers"""
        rows = cur.execute(sql).fetchall()
        
        return [cls.db_to_obj(row) for row in rows]

    def books(self):
        from models.book import Book
        sql = """SELECT * FROM books WHERE shopper_id = ?"""
        rows = cur.execute(sql, (self.id,),).fetchall()

        return [Book.db_to_obj(row) for row in rows]
    
    