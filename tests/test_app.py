from lib.post import *
from lib.post_repository import PostRepository
from lib.user import *
from lib.user_repository import UserRepository

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

def test_post_message(db_connection, web_client):
    db_connection.seed("seeds/chitter_solo_project.sql")
    response = web_client.post("/posts", data={'title':'Voyage','release_year': 2022, 'artist_id': 2})

    assert response.status_code == 200

    response = web_client.get("/posts")

    assert response.status_code == 200
    assert response.data.decode('utf-8') == "1, Voyage, 2022, 2"

def test_get_posts(db_connection, web_client):
     db_connection.seed("seeds/chitter_solo_project.sql")
     response = web_client.get("/posts")
     assert response.status_code == 200
     assert response.data.decode('utf-8') == 'Pixies,ABBA,Taylor Swift,Nina Simone'

def test_create_user(db_connection, web_client):
    db_connection.seed("seeds/chitter_solo_project.sql")
    response = web_client.post("/users?name=MassiveAttack&genre=Pop")
    assert response.status_code == 200

    response = web_client.get("/users")

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies,ABBA,Taylor Swift,Nina Simone,Massive Attack'