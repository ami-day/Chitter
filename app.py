import os
from lib.user import *
from lib.user_repository import *
from lib.post_repository import *
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)
# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/users')
def get_users():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    users = repository.all()
    return render_template("users/all.html", users=users)

@app.route('/posts')
def get_posts():
    connection = get_flask_database_connection(app)
    p_repository = PostRepository(connection)
    posts = p_repository.all()
    return render_template("posts/all.html", posts=posts)

@app.route('/login')
def get_new_user():
    return render_template("users/login.html")

@app.route('/posts/new')
def get_new_post():
    return render_template("posts/new.html")

@app.route('/users/<id>')
def get_user_by_id(id):
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user = repository.find_by_id(id)
    return render_template('users/get_by_id.html',user=user)

@app.route('/posts/<id>')
def get_post_by_id(id):
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    post = repository.find_by_id(id)
    return render_template('posts/get_by_id.html',post=post)

@app.route('/users', methods=["POST"])
def create_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    name_name = request.form['user_name']
    username = request.form['username']
    user_email = request.form['user_email']
    user_password = request.form['user_password']
    user = User(name_name, username, user_email, user_password)
    repository.create(user)
    return redirect(f"/users/{user.id}")

@app.route('/posts', methods=["POST"])
def create_post():
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    message = request.form['message']
    posted = request.form['time']
    author = request.form['user_id']
    post = Post(message, posted, author)
    repository.create(post)
    return redirect(f"/posts/{post.id}")

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))