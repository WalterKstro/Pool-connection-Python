import pymysql
from dbutils.pooled_db import PooledDB
from Logger.Logs import log
import sys


class Connect:
    _DATABASE = 'curso'
    _USERNAME = 'root'
    _PASSWORD = ''
    _HOST = 'localhost'
    _MAX_CONNECTIONS = 5
    _pool = None

    @classmethod
    def createPool(cls):
        if cls._pool is None:
            try:
                cls._pool = PooledDB(
                    creator=pymysql,
                    maxconnections=cls._MAX_CONNECTIONS,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    database=cls._DATABASE
                )
                log.debug(f'Pool created {cls._pool}')
            except Exception as e:
                log.debug(f'Error on create the pool {e}')
                sys.exit()

            return cls._pool
        else:
            return cls._pool

    @classmethod
    def getOneConnection(cls):
        connection = cls.createPool().connection()
        log.debug(f'Got one connection of pool {connection}')
        return connection

    @classmethod
    def dropOneConnection(cls,connection):
        connection.close()
        log.debug('Drop one connection')
