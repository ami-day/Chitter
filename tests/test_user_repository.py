from lib.user_repository import *
from lib.user import *

def test_get_all_records(db_connection):
    db_connection.seed("seeds/chitter_solo_project.sql")
    repository = UserRepository(db_connection)
    
    users = repository.all()
    
    assert users == [User('Sam Morgan','sjmog','samm@makersacademy.com','password123','https://cdn.vox-cdn.com/thumbor/MbYxeyxG82sFlibdnv9Br1aCLg8=/1400x1400/filters:format(png)/cdn.vox-cdn.com/uploads/chorus_asset/file/24395697/bkq6gtrpcnw43vsm5zm62q3z.png')]

def test_create_user(db_connection):
    db_connection.seed("seeds/chitter_solo_project.sql")
    repository = UserRepository(db_connection)
    
    repository.create(User('Ami Day','aday','aday@makersacademy.com','password1234','https://avatars.githubusercontent.com/u/25744951?v=4'))

    users = repository.all()

    assert users == [User('Sam Morgan','sjmog','samm@makersacademy.com','password123','https://cdn.vox-cdn.com/thumbor/MbYxeyxG82sFlibdnv9Br1aCLg8=/1400x1400/filters:format(png)/cdn.vox-cdn.com/uploads/chorus_asset/file/24395697/bkq6gtrpcnw43vsm5zm62q3z.png'),
                     User('Ami Day','aday','aday@makersacademy.com','password1234','https://avatars.githubusercontent.com/u/25744951?v=4')]
    
    





