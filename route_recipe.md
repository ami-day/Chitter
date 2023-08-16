1.  Design the route signature
    
    POST /posts
    message: string
    time: date
    user_id: int

    GET /posts
    Parameters: None

2.  Create Examples as Tests

# POST /posts

# body parameters:
# message = "Goodbye World"
# time = 2022/05/11
# user_id = 1

# Expected response (200 OK):

(No content)

# POST /posts

# body parameters:
# message = "This is my first post"
# time = 2022/06/01
# user_id = 2

# Expected response (200 OK):

(No content)

# GET /posts

Expected response (200 OK):
['Hello World: 2022/05/10, 1',
'Goodbye World: 2022/05/11, 1',
'This is my first post: 2022/06/01, 2']

3. Test-drive the Route

"""
POST /posts
Parameters:
message: Goodbye World
time: 2022/05/11
user_id: 1
"""
test_post_artist(web_client):
response = web_client.post('/posts?message=GoodbyewWorld&time=2022/05/11&user_id=1')
assert response.status_code == 200
(No content)

"""
POST /posts
Parameters:
message: This is my first post
time: 2022/05/10
user_id: 2
"""
test_post_artist(web_client):
response = web_client.post('/posts?message=Thisismyfirstpost&time=2022/06/01&user_id=2')
assert response.status_code == 200
(No content)

"""
GET /posts
Parameters:
None
"""
test_get_posts(web_client):
response = web_client.gett('/posts')
assert response.status_code == 200
assert response.data.decode('utf-8') == ['Hello World: 2022/05/10, 1',
'Goodbye World: 2022/05/11, 1',
'This is my first post: 2022/06/01, 2']