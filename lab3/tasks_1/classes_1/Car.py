
SPEED_0 = 0
SPEED_5 = 5

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = SPEED_0

    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    def set_accelerate(self):
        self.__speed += SPEED_5

    def set_break(self):
        self.__speed -= SPEED_5

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed
