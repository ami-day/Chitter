class Post():
    def __init__(self, message, time, user_id):
        self.message = message
        self.time = time
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__