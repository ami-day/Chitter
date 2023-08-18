from lib.post import *
from lib.post_repository import PostRepository
from lib.user import *
from lib.user_repository import UserRepository
from playwright.sync_api import Page, expect

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

def test_get_users(page, test_web_address, db_connection):
    db_connection.seed('seeds/chitter_solo_project.sql')

    page.goto(f'http://{test_web_address}/users')

    h1_tags = page.locator("h1").all()

    expect(h1_tags[0]).to_have_text("Sam Morgan")

def test_get_posts(page, test_web_address, db_connection):
    db_connection.seed('seeds/chitter_solo_project.sql')

    page.goto(f'http://{test_web_address}/posts')

    h1_tags = page.locator("h1").all()

    #expect(h1_tags[0]).to_have_text("Post: Hello World")

    

