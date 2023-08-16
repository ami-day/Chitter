from lib.user import *

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
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (user_name, username, user_email, user_password) VALUES(%s,%s,%s,%s)', [user.user_name, user.username, user.user_email, user.user_password])
        return None

