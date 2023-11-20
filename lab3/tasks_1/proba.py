import Employee

def main():
    info = Employee.ProductionWorker

    name = input('1name: ')
    namber = int(input('2namber: '))
    namber_change = int(input('1 or 2: '))
    work_house = float(input('4work_house: '))

    intro = info(namber_change, work_house, name, namber)

    print(f'имя:',intro.get_name())
    print(f'номер сотрудника:', intro.get_namber())
    print(f'номер смены:',intro.get_shift())
    print(f'ставка труда:',intro.get_hourly())


if __name__ == '__main__':
    main()
