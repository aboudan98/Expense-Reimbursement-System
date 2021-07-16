from json import JSONEncoder


class Manager:
    # constructor for initializing a user
    def __init__(self, manager_id, manager_username, manager_password):
        self._manager_id = manager_id
        self._manager_username = manager_username
        self._manager_password = manager_password

class ManagerEncoder(JSONEncoder):
    def default(self, manager):
        if isinstance(manager, Manager):
            return manager.__dict__
        else:
            # if something goes wrong just fall back to the parent implementation
            return super().default(self, manager)