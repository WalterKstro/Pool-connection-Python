from Connect.Connect import Connect
from Logger.Logs import log


class Cursor:

    def __init__(self):
        self._connection = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'In block with')
        self._connection = Connect.getOneConnection()
        self._cursor = self._connection.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('In block exit')
        if exc_val:
            self._connection.rollback()
            log.debug(f'Error in {exc_type} {exc_val} {exc_tb}')
        else:
            self._connection.commit()
            Connect.dropOneConnection(self._connection)
            log.debug('Transaction success')
