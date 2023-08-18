from lib.user import *
import hashlib

class UserRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row['user_name'],row['username'],row['user_email'],row['user_password'])
            users.append(item)
        return users
    
    def find_by_id(self, id):
        rows = self._connection.execute('SELECT * FROM users WHERE users.id = %s', [id])
        row = rows[0]
        return User(row['user_name'],row['username'],row['user_email'],row['user_password'])
    
    def create(self, user):
        row = self._connection.execute('INSERT INTO users (user_name, username, user_email, user_password) VALUES(%s,%s,%s,%s) RETURNING id', [user.user_name, user.username, user.user_email, user.user_password])
        user.id = row[0]['id']
        return None

