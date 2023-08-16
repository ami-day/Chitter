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
    
    def create(self,post):
        self._connection.execute('INSERT INTO posts (message, time, user_id) VALUES(%s,%s,%s)', [post.message, post.time, post.user_id])
        return None