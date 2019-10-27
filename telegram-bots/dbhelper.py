import sqlite3

class DBHelper():
    def __init__(self, name="todo.sqlite"):
        self.name = name
        self.conn = sqlite3.connect(name)

    def create(self):
        query = 'CREATE TABLE IF NOT EXISTS items (user text, description text)'
        user_index = 'CREATE INDEX IF NOT EXISTS userIndex ON items (user ASC)'
        item_index = 'CREATE INDEX IF NOT EXISTS itemIndex ON items (description ASC)'
        self.conn.execute(query)
        self.conn.execute(user_index)
        self.conn.execute(item_index)
        self.conn.commit()
    
    def add_item(self, user, item):
        query = 'INSERT INTO items (user, description) VALUES (?,?)'
        args = (user, item)
        self.conn.execute(query, args)
        self.conn.commit()

    def delete_item(self, user, item):
        query = 'DELETE FROM items WHERE user = (?) AND description = (?)'
        args = (user, item)
        self.conn.execute(query, args)
        self.conn.commit()

    def get_items(self, user):
        query = 'SELECT description FROM items WHERE user = (?)'
        args = (user, )
        items = self.conn.execute(query, args)
        return [item[0] for item in items]

    
