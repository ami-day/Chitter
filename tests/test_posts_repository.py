from lib.post import *
from lib.post_repository import *
from datetime import date

def test_get_all_posts(db_connection):
    db_connection.seed("seeds/chitter_solo_project.sql")
    repository = PostRepository(db_connection)
    
    posts = repository.all()
    print(posts)
    
    assert posts == [Post('Hello World',date(2022,3,10),1)]

def test_create_post(db_connection):
    db_connection.seed("seeds/chitter_solo_project.sql")
    repository = PostRepository(db_connection)

    repository.create(Post('This is my second post',date(2022,3,3),1))
    
    posts = repository.all()
    
    assert posts == [Post('Hello World',date(2022,3,10),1),Post('This is my second post',date(2022,3,3),1)]


