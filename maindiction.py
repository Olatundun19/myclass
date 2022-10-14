while 1:
    print('\nDictionary Homepage')
    opt = input('1. Search\t2. Add\n3. Delete \nPls enter your option: ')

    if opt == '1':
        import search
    elif opt == '2':
        import adddiction

    else:
        print('Wrong option...')

    opt = input('\nDo you want to run again (y/n): ')
    if opt == 'y':
        pass
    else:
        break

