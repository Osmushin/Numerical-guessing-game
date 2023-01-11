from random import *

print('Добро пожаловать в игру Числовая Угадайка!!')

def is_valid(number):
    if number.isdigit() and 1 <= int(number) <= 100:
        return True
    else:
        return False

def game():
    hidden_num = randint(1, 100)
    score = 0
    while True:
        print('Введите число от 1 до 100')
        number = input()

        if is_valid(number) == True:
            number = int(number)
            if number < hidden_num:
                score += 1
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif number > hidden_num:
                score += 1
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                print('Количество попыток составило:', score)
                break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

    print('Если хотите сыграть еще раз - введите "да" ')
    print('Если не хотите продолжать игру введите "стоп"')
    answer = input()
    if answer == 'да':
        return True
    elif answer == 'стоп':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        return False

game()

while game() == True:
    game()