from lib.user import *

class User():
    user = User('Sam Morgan','sjmog','samm@makersacademy.com','password123','https://cdn.vox-cdn.com/thumbor/MbYxeyxG82sFlibdnv9Br1aCLg8=/1400x1400/filters:format(png)/cdn.vox-cdn.com/uploads/chorus_asset/file/24395697/bkq6gtrpcnw43vsm5zm62q3z.png')
    assert user.user_name == 'Sam Morgan'
    assert user.username == 'sjmog'
    assert user.user_email == 'samm@makersacademy.com'
    assert user.user_password == 'password123'
    assert user.user_picture == 'https://cdn.vox-cdn.com/thumbor/MbYxeyxG82sFlibdnv9Br1aCLg8=/1400x1400/filters:format(png)/cdn.vox-cdn.com/uploads/chorus_asset/file/24395697/bkq6gtrpcnw43vsm5zm62q3z.png'
