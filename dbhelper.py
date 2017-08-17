import sqlite3

class DBHelper:
    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.connection = sqlite3.connect(dbname)

    def setup(self):
        print("creating database")
        statement = "CREATE TABLE IF NOT EXISTS items (description text, owner text)"
        itemindex = "CREATE INDEX IF NOT EXISTS itemIndex ON items (description ASC)"
        ownerindex = "CREATE INDEX IF NOT EXISTS onwerIndex ON items (owner ASC)"
        self.connection.execute(statement)
        self.connection.execute(itemindex)
        self.connection.execute(ownerindex)
        self.connection.commit()

    def add_item(self, item_text, owner):
        statement = "INSERT INTO items (description, owner) VALUES (?, ?)"
        args = (item_text, owner)
        self.connection.execute(statement, args)
        self.connection.commit()

    def delete_item(self, item_text, owner):
        statement = "DELETE FROM items WHERE description = (?) AND owner = (?)"
        args = (item_text, owner)
        self.connection.execute(statement, args)
        self.connection.commit()

    def get_items(self, owner):
        statement = "SELECT description FROM items WHERE owner = (?)"
        args = (owner, )
        return [x[0] for x in self.connection.execute(statement, args)]
