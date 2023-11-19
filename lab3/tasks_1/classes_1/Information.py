class Info:
    def __init__(self,name, adress, age, phone_namber):
        self.__name = name
        self.__adress = adress
        self.__age = age
        self.__phone_namber = phone_namber

    def set_name(self, name):
        self.__name = name

    def set_adress(self, adress):
        self.__adress = adress

    def set_age(self, age):
        self.__age = age

    def set_phone_namber(self, phone_namber):
        self.__phone_namber = phone_namber

    def get_name(self):
        return self.__name

    def get_adress(self):
        return self.__adress

    def get_age(self):
        return self.__age

    def get_phone_namber(self):
        return self.__phone_namber
