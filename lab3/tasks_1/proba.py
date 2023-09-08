MIN = 1
MAX = 9
COLUMN = 3
LINE = 3
NUMS = 15

def main():
    magic_square = [[4, 9, 2],
                    [3, 5, 7],
                    [8, 1, 6]]

    number = number_comparison(magic_square)
    string = string_comparison(magic_square)
    column = column_comparison(magic_square)
    diagonal = diagonal_alignment(magic_square)

    if number == True and string == True and\
       column == True and diagonal == True:
        print('Ура.Квадрат являеться магическим')
    else:
        print('Квадрат не магический')

def number_comparison(magic):   # Проверяем все ли значения в диапазоне от 1 до 9
    status = True

    for column in range(COLUMN):
        for line in range(LINE):
            if magic[column][line] > MAX or magic[column][line] < 1:
                status = False

    return status

def string_comparison(magic):   # сумируем и сравниваем строки
    status = True

    line_1 = magic[0][0] + magic[0][1] + magic[0][2]
    line_2 = magic[1][0] + magic[1][1] + magic[1][2]
    line_3 = magic[2][0] + magic[2][1] + magic[2][2]

    if line_1 == NUMS and line_2 == NUMS and line_3 == NUMS:
        return status

def column_comparison(magic):   # сумируем и сравниваем столбцы
    status = True

    column_1 = magic[0][0] + magic[1][0] + magic[2][0]
    column_2 = magic[0][1] + magic[1][1] + magic[2][1]
    column_3 = magic[0][2] + magic[1][2] + magic[2][2]

    if column_1 == NUMS and column_2 == NUMS and column_3 == NUMS:
        return status

def diagonal_alignment(magic):   # сумируем и сравниваем диагонали
    status =True

    diagonal_1 = magic[0][0] + magic[1][1] + magic[2][2]
    diagonal_2 = magic[0][2] + magic[1][1] + magic[2][0]

    if diagonal_1 == NUMS and diagonal_2 == NUMS:
        return status

if __name__ == '__main__':
    main()