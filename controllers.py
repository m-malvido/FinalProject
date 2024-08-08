from models import User

class UserController:
    def login(self, username, password):
        user = User.authenticate(username, password)
        if user:
            return True
        return False

    def register(self, username, password):
        if not username or not password:
            return False
        user = User(username, password)
        user.save()
        return True
