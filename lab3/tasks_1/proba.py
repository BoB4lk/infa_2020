

YEAR_START = 1950
YEAR_FINISH = 1990

def main():
    try:
        # YEAR_START = 1950
        # YEAR_FINISH = 1990
        population_1 = []   # прочитанный из файла список с общим кол-вом проживающего
                            # населения ежегодно - в int формате

        people_year = []    # список с разницей кол-ва прибавляющегося населения ежегодно - в int формате

        population_file = open(r'data/USPopulation.txt', 'r')

        for years in population_file.readlines():   # добавление списка из файла в в пустой список
            population_1.append(int(years))

        population_file.close()

        for people in range(YEAR_FINISH - YEAR_START - 1):   # вычисляем кол-во населения прибавляющевося каждый год
            people_1 = population_1[people+1] - population_1[people]
            people_year.append(people_1)

        average = average_people_year(people_year)
        print(f'среднегодовое изменение численности населения - {average:,.0f} человек')

        max_people = max_people_year(people_year)
        print(f'{max_people} год с наибольшим увеличением численности населения с {YEAR_START}г по {YEAR_FINISH}г')

        min_people = min_people_year(people_year)
        print(f'{min_people} год с наименьшим увеличением численности населения с {YEAR_START}г по {YEAR_FINISH}г')

        print(people_year)

    except IOError:
        print('Файл не найден')
    except:
        print('Непонятная ошибка!!!')

def max_people_year(people):   # год с наибольшим увеличением численности населения
    max_people = max(people)

    index_max_people = people.index(max_people)

    return YEAR_START + index_max_people

def min_people_year(people):   # год с наименьшим увеличением численности населения
    min_people = min(people)

    index_min_people = people.index(min_people)

    return YEAR_START + index_min_people

def average_people_year(people):   # вычисляем среднегодовое изменение численности населения
    total = 0

    for average_number in people:
        total += average_number

    total /= len(people)

    return total


if __name__ == '__main__':
    main()