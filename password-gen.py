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
        try:
            lengthOfPassword = int(input('\nlength of password: '))
            correctDatatype = True
        except ValueError:
            print("\nInvalid input\n")
            correctDatatype = False

    correctDatatype = False
    while not correctDatatype:
        try:
            howManyPasswords = int(input('\nhow many passwords: '))
            correctDatatype = True
        except ValueError:
            print("\nInvalid input\n")
            correctDatatype = False

    print('\n')

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
        elif rerun == 'n':
            correctDatatype = True
            run = False
        else:
            print('\nInvalid input\n')
            correctDatatype = False
