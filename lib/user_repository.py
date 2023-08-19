from lib.user import *

class UserRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row['user_name'],row['username'],row['user_email'],row['user_password'],row['user_picture'])
            users.append(item)
        return users
    
    def find_by_id(self, id):
        rows = self._connection.execute('SELECT * FROM users WHERE users.id = %s', [id])
        row = rows[0]
        return User(row['user_name'],row['username'],row['user_email'],row['user_password'],row['user_picture'])
    
    def create(self, user):
        row = self._connection.execute('INSERT INTO users (user_name, username, user_email, user_password, user_picture) VALUES(%s,%s,%s,%s,%s) RETURNING id', [user.user_name, user.username, user.user_email, user.user_password, user.user_picture])
        user.id = row[0]['id']
        return None

    def check_password(self, username, password_attempt):

        # Check whether there is a user in the database with the given username
        # using a SELECT statement.
        rows = self._connection.execute(
            'SELECT * FROM users WHERE username = %s AND user_password = %s',
            [username, password_attempt])

        # If that SELECT finds any rows, the password is correct.
        return len(rows) > 0

