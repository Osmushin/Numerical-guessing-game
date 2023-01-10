from random import *

Hidden_num = randint(1, 100)
print('Добро пожаловать в игру Числовая Угадайка!!')


def is_valid(number):
    if number.isdigit() and 1 <= int(number) <= 100:
        return True
    else:
        return False


while True:
    print('Введите число от 1 до 100')
    number = input()

    if is_valid(number) == True:
        number = int(number)
        print('OK')
        break
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')

print('Its test PySharm and GIT')
print('I like this progrdsdadam')