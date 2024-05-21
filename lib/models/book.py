from models.__init__ import (con, cur)

class Book():
    def __init__(self, title, author, genre, shopper_id=1, id=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.shopper_id = shopper_id
        self.id = id
        #use shopper id

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
    
    
    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS Books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        genre TEXT,
        shopper_id INTEGER
        );"""

        cur.execute(sql)
        con.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS Books;"""
        cur.execute(sql)
        con.commit()

    @classmethod
    def db_to_obj(cls, row):
        id, title, author, genre, shopper_id = row 
        return cls(title, author, genre, shopper_id, id,)
    

    @classmethod
    def create_item(cls, title, author, genre, shopper_id=1):
        item = cls(title, author, genre, shopper_id)
        sql = """INSERT INTO Books (title, author, genre, shopper_id) VALUES (?, ?, ?, ?)"""
        cur.execute(sql, (item.title, item.author, item.genre, item.shopper_id,))
        con.commit()
    
    
    @classmethod
    def delete_item(cls, id):
        sql = """DELETE FROM iventory WHERE id = ?"""
        cur.execute(sql, (id,))
        con.commit()
    
    @classmethod
    def find_item_by_id(cls, id):
        sql = """SELECT * FROM Books WHERE id = ?"""
        row = cur.execute(sql, (id,)).fetchone()

        return cls.db_to_obj(row) if row else None
    
    @classmethod
    def update_shopper_id(cls, shopper_id, id):
        sql = """UPDATE Books SET shopper_id = ? WHERE id = ?"""
        cur.execute(sql, (shopper_id, id,))
        con.commit()
    
    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM Books"""
        rows = cur.execute(sql).fetchall()
        
        return rows
    
    @classmethod
    def get_all_available(cls, shopper_id=1):
        sql = """SELECT * FROM Books WHERE shopper_id = ?"""
        rows = cur.execute(sql, (shopper_id,)).fetchall()
        
        return [cls.db_to_obj(row) for row in rows]
    
    @classmethod
    def find_item_by_author(cls, author):
        sql = """SELECT * FROM Books WHERE author = ?"""
        rows = cur.execute(sql, (author,)).fetchall()

        return [cls.db_to_obj(row) for row in rows]
    
    @classmethod
    def find_item_by_title(cls, title):
        sql = """SELECT * FROM Books WHERE title = ?"""
        rows = cur.execute(sql, (title,)).fetchall()

        return [cls.db_to_obj(row) for row in rows]
    
    @classmethod
    def find_item_by_genre(cls, genre):
        sql = """SELECT * FROM Books WHERE genre = ?"""
        rows = cur.execute(sql, (genre,)).fetchall()

        return [cls.db_to_obj(row) for row in rows]