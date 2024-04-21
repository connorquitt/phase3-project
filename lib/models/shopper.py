from models.__init__ import (con, cur)

class Shopper():
    def __init__(self, username, password, funds=0, id=None):
        self.username = username
        self.password = password
        self.funds = funds
        self.id = id

    
    @property
    def set_username(shopper):
        return shopper._username
    @set_username.setter
    def set_username(shopper, username):
        if isinstance(username, str):
            shopper._username = username
        else:
            print('username must be a string')
    
    @property
    def set_password(shopper):
        return shopper._password
    @set_password.setter
    def set_password(shopper, password):
        if isinstance(password, str) and len(password) > 4:
            shopper._password = password
        else:
            print('password must be a string, and at least 5 characters')

    @property
    def set_funds(shopper):
        return shopper._funds
    @set_funds.setter
    def set_funds(shopper, funds):
        if isinstance(funds, int):
            shopper._funds = funds
        else:
            print('funds must be a number')

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS shoppers (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        funds INTEGER
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
        id, username, password, funds = row 
        return cls(username, password, funds, id,)
    

    @classmethod
    def create_user(cls, username, password, funds=0):
        shopper = cls(username, password, funds)
        sql = """INSERT INTO shoppers (username, password, funds) VALUES (?, ?, ?)"""
        cur.execute(sql, (shopper.username, shopper.password, shopper.funds))
        con.commit()
    
    
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
    def update_funds(cls, funds, id):
        sql = """UPDATE shoppers SET funds = ? WHERE id = ?"""
        cur.execute(sql, (funds, id,))

    @classmethod
    def find_user_by_id(cls, id):
        sql = """SELECT * FROM shoppers WHERE id = ?"""
        row = cur.execute(sql, (id,)).fetchone()

        return row
    
    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM shoppers"""
        rows = cur.execute(sql).fetchall()
        
        return rows