def verify():   
    while 1:
        pword = input('Enter your Password: ')
        x = len(pword)
        if x <= 7:
            print('Password should be more than 7 characters!!!')
        else: 
            return pword
    w