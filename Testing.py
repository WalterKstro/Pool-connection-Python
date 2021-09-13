from Mapping.Username import Username
from Operations.Operations import Operations
from Logger.Logs import log

isExit = True

def show():
    users = Operations.select_all()
    for user in users:
        print(user)

def add():
    name = input('Write the name: ')
    nick = input('Write the nick: ')
    password = input('Write the password: ')
    username = Username(username_name=name, username_nick=nick, username_pass=password)
    print(f'{Operations.insert_user(username)} username was registered')

def update():
    id = int(input('Write you id: '))
    name = input('Write the new name: ')
    nick = input('Write the new nick: ')
    password = input('Write the new password: ')

    username = Username(
        username_id= id if id != '' else None,
        username_name=name if name != '' else None,
        username_nick=nick if nick != '' else None,
        username_pass=password if password != '' else None
    )
    print(f'{Operations.update_user(username)} username was updated')

def delete():
    id = int(input('Write you id: '))
    username = Username(username_id=id)

    print(f'{Operations.delete_user(username)} username was deleted')



while isExit:
    print(' Main Menu '.center(50, '*'))

    print(' 1) --> Show users')
    print(' 2) --> Add user')
    print(' 3) --> Update user')
    print(' 4) --> Delete user')
    print(' 5) --> Exit')

    opt = int(input('Write one option (1-5): '))

    if opt == 1:
        show()
    elif opt == 2:
        add()
    elif opt == 3:
        update()
    elif opt == 4:
        delete()
    else:
        isExit=False
        log.info('Bye bye')
