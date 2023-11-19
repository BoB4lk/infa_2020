
from Information import Info

def main():
    my_info = Info('Джон Доу', '111 Моя улица', 22, '555-555-1281')
    mom_info = Info('Мать', '222 Мамина улица', 52, '555-555-1234')
    sister_info = Info('Джейн Доу', '333 Ее улица', 20, '555-555-4444')

    print('Информация обо мне:')
    display_info(my_info)
    print()

    print("Информация о матери:")
    display_info(mom_info)
    print()

    print("Информация о сестре:")
    display_info(sister_info)


def display_info(info):
    print(' Имя:     ', info.get_name())
    print(' Адрес:   ', info.get_adress())
    print(' Возраст: ', info.get_age())
    print(' Телефон: ', info.get_phone_namber())


if __name__ == '__main__':
    main()