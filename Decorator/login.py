def printdebug(func):
    def d():
        print('enter the login')
        func()
        print('exit the login')
    return d


@printdebug
def login():
    print('in login')


login()
