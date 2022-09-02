import random

# loop as long as the user wants to run it
run = True
while run:
    # list of characters available
    characters = '''1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_\=+`~!@#$%^&*()[]{}|;:'",.<>/?'''

    # list of characters available but only the numbers
    pin = '1234567890'

    correctDatatype = False
    while not correctDatatype:
        # use alphanumeric characters or just numbers
        weatherPinOrNot = input('pin(y/n): ')

        if weatherPinOrNot == 'y':
            # override to just numbers
            characters = pin
            correctDatatype = True
        elif weatherPinOrNot == 'n':
            correctDatatype = True
        else:
            print('\nInvalid input\n')
            correctDatatype = False

    # get settings
    correctDatatype = False
    while not correctDatatype:
        lengthOfPassword = input('length of password: ')

        if type(lengthOfPassword) == int:
            correctDatatype = True
        else:
            print("\nInvalid input\n")
            correctDatatype = False

    correctDatatype = False
    while not correctDatatype:
        howManyPasswords = input('how many passwords: ')

        if type(correctDatatype) == int:
            correctDatatype = True
        else:
            print("\nInvalid input\n")
            correctDatatype = False

    # for every password
    for weatherPinOrNot in range(int(howManyPasswords)):
        # create password storage
        password = ''

        # for every character
        for i in range(int(lengthOfPassword)):
            character = random.choice(characters)

            password += character

        print(password)

    correctDatatype = False
    while not correctDatatype:
        rerun = input('\nredo(y/n): ')

        if rerun == 'y':
            correctDatatype = True
            run = True
        if rerun == 'n':
            correctDatatype = True
            run = False
        else:
            print('\nInvalid input\n')
            correctDatatype = False
