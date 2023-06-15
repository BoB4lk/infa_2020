def main():
    num1 = int(input("ВВедите 1-ю оценку: "))
    num2 = int(input("ВВедите 2-ю оценку: "))
    num3 = int(input("ВВедите 3-ю оценку: "))
    num4 = int(input("ВВедите 4-ю оценку: "))
    num5 = int(input("ВВедите 5-ю оценку: "))

    sum_num = calc_average(num1, num2, num3, num4, num5)

    score = determine_grade(sum_num)

    print("-" * 20)
    print("Оценка\t\tБалл")
    print("-" * 20)

    print(f"\t{num1}\t\t", determine_grade(num1))
    print(f"\t{num2}\t\t", determine_grade(num2))
    print(f"\t{num3}\t\t", determine_grade(num3))
    print(f"\t{num4}\t\t", determine_grade(num4))
    print(f"\t{num5}\t\t", determine_grade(num5))

    print(f"Ваша средняя оценка - {score}, средний балл - {sum_num}")


def calc_average(num1, num2, num3, num4, num5):
    sum_num = num1 + num2 + num3 + num4 + num5
    return sum_num / 5


def determine_grade(sum_num):
    if sum_num >= 90:
        return "A"
    elif sum_num >= 80:
        return "B"
    elif sum_num >= 70:
        return "C"
    elif sum_num >= 60:
        return "D"
    else:
        return "F"


main()
