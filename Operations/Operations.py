from Mapping.Username import Username
from Cursor.Cursor import Cursor
from Mapping.Username import Username



class Operations:
    _TABLE = 'usernames'
    _QUERY_SELECT = f'SELECT Username_ID,Username_Name,Username_Nick,Username_Pass FROM {_TABLE}'
    _QUERY_INSERT = f'INSERT INTO {_TABLE} (Username_Name,Username_Nick,Username_Pass) VALUES (%s,%s,%s)'
    _QUERY_UPDATE = f'UPDATE {_TABLE} SET Username_Name = %s,Username_Nick=%s,Username_Pass=%s WHERE Username_ID = %s'
    _QUERY_DELETE = f'DELETE FROM {_TABLE} WHERE Username_ID = %s'
    _QUERY_FIND = f'SELECT Username_ID,Username_Name,Username_Nick,Username_Pass FROM {_TABLE} WHERE Username_ID=%s'

    @classmethod
    def select_all(cls):
        list_users = []
        with Cursor() as cursor:
            cursor.execute(cls._QUERY_SELECT)
            for user in cursor.fetchall():
                list_users.append(Username(
                    username_id = user[0],
                    username_name = user[1],
                    username_nick = user[2],
                    username_pass = user[3]
                ))
        return list_users

    @classmethod
    def insert_user(cls, user):
        rowAffected = 0
        with Cursor() as cursor:
            cursor.execute(cls._QUERY_INSERT,(user.username_name,user.username_nick,user.username_pass))
            rowAffected = cursor.rowcount
        return rowAffected

    @classmethod
    def update_user(cls,updates):
        rowAffected = 0
        with Cursor() as cursor:
            cursor.execute(cls._QUERY_FIND,(updates.username_id,))
            user_db = cursor.fetchone()

            new_username = Username(
                username_id=user_db[0],
                username_name=user_db[1],
                username_nick=user_db[2],
                username_pass=user_db[3]
            )

            new_username.username_name = new_username.username_name if updates.username_name  == None else updates.username_name
            new_username.username_nick = new_username.username_nick if updates.username_nick == None else updates.username_nick
            new_username.username_pass = new_username.username_pass if updates.username_pass == None else updates.username_pass

            cursor.execute(cls._QUERY_UPDATE,(new_username.username_name, new_username.username_nick, new_username.username_pass, new_username.username_id))
            rowAffected = cursor.rowcount
        return rowAffected

    @classmethod
    def delete_user(cls,user):
        rowAffected = 0
        with Cursor() as cursor:
            cursor.execute(cls._QUERY_DELETE,(user.username_id,))
            rowAffected = cursor.rowcount
        return rowAffected

