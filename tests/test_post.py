from lib.post import *
from datetime import date

def test_post_initialises():
    post = Post('Hello World',date(2022,3,10),1)
    assert post.message == 'Hello World'
    assert post.time == date(2022,3,10)
    assert post.user_id == 1