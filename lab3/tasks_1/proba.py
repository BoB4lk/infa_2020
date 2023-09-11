

def main():
    try:
        numbers = []

        user_number = int(input('Введите целое число больше 1 - '))

        if user_number <= 1:
            print('Ошибка! Введите целое число больше 1.')
        else:
            for _ in range(2, user_number + 1):
                numbers.append(_)

        for _ in numbers:
            status = prime_numbers(_, user_number)

        if status:
            print('Простое число')
        else:
            print('Составное число')

    except:
        print('Ошибка!')

def prime_numbers(numbers, user):
    status = True

    for _ in range(2, numbers):
        if user % _ == 0:
            status = False
    return status




if __name__ == '__main__':
    main()