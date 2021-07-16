from json import JSONEncoder


class User:
    # constructor for initializing a user
    def __init__(self, user_id, user_username, user_password, reimbursements):
        self._user_id = user_id
        self._user_username = user_username
        self._user_password = user_password
        self.reimbursements = reimbursements

class UserEncoder(JSONEncoder):
    def default(self, user):
        if isinstance(user, User):
            return user.__dict__
        else:
            # if something goes wrong just fall back to the parent implementation
            return super().default(self, user)