from models.__init__ import (con, cur)

class Book():
    def __init__(self, title, author, genre, price=0, owner_id=None, id=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.owner_id = owner_id
        self.id = id

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            print('title must be a string')
    
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if isinstance(author, str):
            self._author = author
        else:
            print('author must be a string')
    
    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self, genre):
        if isinstance(genre, str):
            self._genre = genre
        else:
            print('genre must be a string')
    
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if isinstance(price, int):
            self._price = price
        else:
            print('price must be an integer')
    
    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        genre TEXT,
        price INTEGER,
        owner_id INTEGER
        );"""

        cur.execute(sql)
        con.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS inventory;"""
        cur.execute(sql)
        con.commit()

    @classmethod
    def db_to_obj(cls, row):
        id, title, author, genre, price, owner_id = row 
        return cls(title, author, genre, price, owner_id, id,)
    

    @classmethod
    def create_item(cls, title, author, genre, price=0, owner_id=None):
        item = cls(title, author, genre, price, owner_id)
        sql = """INSERT INTO inventory (title, author, genre, price, owner_id) VALUES (?, ?, ?, ?, ?)"""
        cur.execute(sql, (item.title, item.author, item.genre, item.price, item.owner_id,))
        con.commit()
    
    
    @classmethod
    def delete_item(cls, id):
        sql = """DELETE FROM iventory WHERE id = ?"""
        cur.execute(sql, (id,))
        con.commit()

    @classmethod
    def update_price(cls, price, id):
        sql = """UPDATE iventory SET price = ? WHERE id = ?"""
        cur.execute(sql, (price, id,))
    
    @classmethod
    def find_item_by_id(cls, id):
        sql = """SELECT * FROM iventory WHERE id = ?"""
        row = cur.execute(sql, (id,)).fetchone()

        return row
    
    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM inventory"""
        rows = cur.execute(sql).fetchall()
        
        return rows