#from Logger.Logs import log
class Username:

    def __init__(self, username_id=None, username_name=None, username_nick=None, username_pass=None):
        self._username_id = username_id
        self._username_name = username_name
        self._username_nick = username_nick
        self._username_pass = username_pass


    @property
    def username_id(self) -> int:
        return self._username_id

    @property
    def username_name(self) -> str:
        return self._username_name
    @username_name.setter
    def username_name(self, username_name):
        self._username_name = username_name

    @property
    def username_nick(self) -> str:
        return self._username_nick
    @username_nick.setter
    def username_nick(self, username_nick):
        self._username_nick = username_nick

    @property
    def username_pass(self) -> str:
        return self._username_pass
    @username_pass.setter
    def username_pass(self, username_pass):
        self._username_pass = username_pass

    def __str__(self) -> str:
        return f'Username ID: {self._username_id}, Username Name: {self._username_name}, Username Nick: {self._username_nick}, Username Password: {self._username_pass}'


