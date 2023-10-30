
SPEED_0 = 0
SPEED_5 = 5

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def set_year_model(self, year_model):
        '''Модель машины'''
        self.__year_model = year_model

    def set_make(self, make):
        '''Фирма изготовителя'''
        self.__make = make

    def set_accelerate(self):
        '''Прибавляет к скорости +5, при каждом вызове '''
        self.__speed += SPEED_5

    def set_break(self):
        '''Убавляет от скорости -5, при каждомвызове'''
        self.__speed -= SPEED_5

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed
