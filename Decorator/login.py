def printdebug_level(level = 0):  #add wrapper to recevie decorator's parameter
    def printdebug(func):
        def __decorator(user):
            print('enter the login, and debug level is: ' + str(level)) #print debug level
            res = func(user)
            print('exit the login')
            return res
        return __decorator
    return printdebug    #return original decorator

@printdebug_level()   #decorator's parameter, debug level set to 5
def login(user):
    print 'in login:' + user
    msg = "success"
    return msg

print login('jatsz')