import random

run = True
while run:
    characters = '''1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_\=+`~!@#$%^&*()[]{}|;:'",.<>/?'''

    pin = '1234567890'

    weatherPinOrNot = input('pin(y/n): ')

    if weatherPinOrNot == 'y':
        characters = pin

    lengthOfPassword = input('length of password: ')

    howManyPasswords = input('how many passwords: ')

    for weatherPinOrNot in range(int(howManyPasswords)):
        password = ''
        for i in range(int(lengthOfPassword)):
            character = random.choice(characters)
            password += character
        print(password)

    rerun = input('\n' + 'redo(y/n): ')

    if rerun == 'n':
        run = False
    else:
        run = True
