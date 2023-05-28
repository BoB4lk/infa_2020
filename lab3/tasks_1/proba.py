DYE = 5
SQUARE_METERS = 10
JOB = 8
JOB_HOUR = 2000

def main():
    wall_area = float(input("Введите площадь окрашиваемой стены: "))
    price_dye = float(input("Введите стоимость 5 литвой краски: "))

    sum_dye = wall_area / SQUARE_METERS
    hours_spent = wall_area * JOB / SQUARE_METERS
    sum_price_dye = price_dye * sum_dye
    price_job = JOB_HOUR * hours_spent
    sum_job = sum_price_dye + price_job

    data_output(sum_dye, hours_spent, sum_price_dye, price_job, sum_job)
def data_output(sum_dye, hours_spent, sum_price_dye, price_job, sum_job):
    print(f"Кол-во требуемых емкостей краски - {sum_dye} шт")
    print(f"Кол-во затраченного времени - {hours_spent} часов")
    print(f"Стоимость краски - {sum_price_dye} руб.")
    print(f"Стоимость работ - {price_job} руб.")
    print(f"Общая стоимость всех затрат - {sum_job} руб.")

main()