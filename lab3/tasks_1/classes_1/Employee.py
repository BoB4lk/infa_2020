
class Employee:

    def __init__(self, name_emp, namber_emp):
         self.__name_emp = name_emp
         self.__namber_emp = namber_emp

    def set_name(self, name_emp):
         self.__name_emp = name_emp

    def set_namber(self, namber_emp):
         self.__namber_emp = namber_emp

    def get_name(self):
        return self.__name_emp
    def get_namber(self):
        return self.__namber_emp

class ProductionWorker(Employee):
    def __init__(self, shift_number, hourly_rate, name_emp, namber_emp):
        Employee.__init__(self, name_emp, namber_emp)
        self.__shift_number = shift_number
        self.__hourly_rate = hourly_rate

    def set_shift(self, shift_number):
         self.__shift_number = shift_number

    def set_hourly(self, hourly_rate):
         self.__hourly_rate = hourly_rate

    def get_shift(self):
        return self.__shift_number
    def get_hourly(self):
        return self.__hourly_rate

class ShiftSupervisor(Employee):
    def __init__(self, name_emp, namber_emp, year_salary, year_bonus):
        Employee.__init__(self, name_emp, namber_emp)
        self.__year_salary = year_salary
        self.__year_bonus = year_bonus

    def set_salary(self, year_salary):
        self.__year_salary = year_salary

    def set_bonus(self, year_bonus):
        self.__year_bonus = year_bonus

    def get_salary(self):
        return self.__year_salary

    def get_bonus(self):
        return self.__year_bonus