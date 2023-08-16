from lib.user import *

class User():
    user = User('Sam Morgan','sjmog','samm@makersacademy.com','password123')
    assert user.user_name == 'Sam Morgan'
    assert user.username == 'sjmog'
    assert user.user_email == 'samm@makersacademy.com'
    assert user.user_password == 'password123'
