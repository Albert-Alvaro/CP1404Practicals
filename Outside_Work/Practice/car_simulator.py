from prac_06.car import Car
MENU = """Menu:
 d) drive
 r) refuel
 q) quit"""


def main():
    print("Let's drive!")
    name = input("Enter your car name: ")
    default_car = Car(name, 100)
    print(default_car)
    choice = get_choice()
    while choice != "q":
        if choice == "d":
            drive_car(default_car)
        elif choice == "r":
            fuel = get_fuel()
            default_car.add_fuel(fuel)
            print(f"Added {fuel} units of fuel")
        else:
            print("Invalid Choice")
        print(default_car)
        choice = get_choice()
    print(f"Goodbye {default_car.name}'s driver")


def drive_car(default_car):
    distance = get_distance()
    if default_car.fuel < distance:
        distance = default_car.fuel
        default_car.drive(distance)
        print(f"The car drove {distance}km and ran out of fuel")
    else:
        default_car.drive(distance)
        print(f"The car drove {distance}km")


def get_distance():
    distance = int(input("How many km do you wish to drive? "))
    while distance < 0:
        print("Distance must be >= 0")
        distance = int(input("How many km do you wish to drive? "))
    return distance


def get_fuel():
    fuel = int(input("How many units of fuel do you want to add to the car? "))
    while fuel < 0:
        print("Fuel must be >= 0")
        fuel = int(input("How many units of fuel do you want to add to the car? "))
    return fuel


def get_choice():
    print(MENU)
    choice = input("Enter your choice: ").lower()
    return choice


main()
