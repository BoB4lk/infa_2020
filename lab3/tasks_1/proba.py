ROWS = 5
COLS = 3

def main():

    numbers = []

    for i in range(ROWS):
        numbers.append([])
        for g in range(COLS):
            numbers[i].append(0)

    for nums in range(ROWS):
        for num in range(COLS):
            numbers[nums][num] = int(input("Введите случайное число - "))

    print(numbers)

if __name__ == '__main__':
    main()