from lib.user_repository import *
from lib.user import *

def test_get_all_records(db_connection):
    db_connection.seed("seeds/chitter_solo_project.sql")
    repository = UserRepository(db_connection)
    
    users = repository.all()
    
    assert users == [User('Sam Morgan','sjmog','samm@makersacademy.com','password123')]

def test_create_user(db_connection):
    db_connection.seed("seeds/chitter_solo_project.sql")
    repository = UserRepository(db_connection)
    
    repository.create(User('Ami Day','aday','aday@makersacademy.com','password1234'))

    users = repository.all()

    assert users == [User('Sam Morgan','sjmog','samm@makersacademy.com','password123'),
                     User('Ami Day','aday','aday@makersacademy.com','password1234')]
    
    





