from lib.post import *

class PostRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Post(row['message'],row['time'],row['user_id'])
        posts.append(item)
        return posts
    
    def find_by_id(self, id):
        rows = self._connection.execute('SELECT * FROM posts WHERE posts.id = %s', [id])
        row = rows[0]
        return Post(row['message'],row['time'],row['user_id'])
    
    def create(self,post):
        rows = self._connection.execute('INSERT INTO posts (message, time, user_id) VALUES(%s,%s,%s) RETURNING ID', [post.message, post.time, post.user_id])
        row = rows[0]
        post.id = row['id']
        return None