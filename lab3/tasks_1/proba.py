# формула расчета падения тела ( d = 1 / 2 * (9.8 ** 2) * t)
# d - расстояние в метрах
# t - время в секундах
# g - 9.8
def main():
    # time = float(input("Введите время падения тела в секундах - "))
    print("Время \t\t Расстоние")
    print('-' * 20)
    for time in range(1, 11):
        distance = falling_distance(time)
        print(time, "\t\t\t", f"{distance:.2f}")

def falling_distance(time):
    distance = (9.8 * time * time) / 2
    return distance

main()