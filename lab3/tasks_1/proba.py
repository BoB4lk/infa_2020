
import classes_1.Car  as automobile

def main():
    car = automobile.Car('2008', 'Honda Accord')

    for _ in range(5):
        car.set_accelerate()
        print(car.get_speed())

    for _ in range(5):
        car.set_break()
        print(car.get_speed())

if __name__ == '__main__':
    main()