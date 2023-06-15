# k = 1/2*(m*v)**2
def main():
    weight = float(input("Введите массу тела в кг - "))
    speed = float(input("Введите скорость в м/с - "))
    kinetic = kinetic_energy(weight, speed)
    print(f"Кинетическая энергия состовляет - {kinetic:.2f} джоулей")

def kinetic_energy(weight, speed):
    kinetic = (weight * speed * speed ) / 2
    return kinetic


main()