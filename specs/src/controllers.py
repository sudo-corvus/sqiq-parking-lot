import sys

from specs.src.models.car import Car
from specs.src.enums import Command


def command(line, parking_lot):
    """
    Accepts commands from each line and executes relevant behaviour
    :param line: command accepted by program
    :param parking_lot: parking_lot object
    :return: response relevant with command
    """

    data = line.split()
    cmd, args = Command(data[0]), data[1:]
    if Command.has_command(data[0]):
        if cmd is Command.CREATE_PARKING_LOT:
            try:
                parking_lot.initialise_parking(args[0])
                return f'Created parking of {args[0]} slots'
            except IndexError:
                return 'Please provide the size of parking lot'

        if cmd is Command.PARK:
            if len(data) == 4:
                try:
                    car = Car(args[0], args[2])
                    slot = parking_lot.add_car(car)
                    return f'Car with vehicle registration number "{args[0]}" has been parked at slot number {slot}'
                except:
                    return 'Inconvenience is regretted, Parking lot is full'
            else:
                return 'Invalid arguments'

        elif cmd is Command.LEAVE:
            if len(data) == 2:
                try:
                    slot = parking_lot.remove_car(int(args[0]))
                    if slot:
                        return f'Slot number {args[0]} vacated, the car with vehicle registration number "{slot.get_registration_number}" left the space, the driver of the car was of age {slot.get_driver_age}'
                except:
                    return 'Invalid slot number: Empty or Non-existant.'
            else:
                return 'Invaid arguments'

        elif cmd is Command.REG_BY_AGE:
            try:
                cars = parking_lot.get_car_reg_by_age(data[1])
                return cars
            except:
                return ''

        elif cmd is Command.SLOTS_BY_AGE:
            cars = parking_lot.slot_num_by_age(args[0])
            if cars == 0:
                return ''
            else:
                return cars

        elif cmd is Command.SLOT_FOR_CAR_NUMBER:
            cars = parking_lot.slot_num_with_registration_number(data[1])
            if cars != 0:
                return cars
            else:
                return ''

        elif cmd is Command.EXIT:
            print("Exiting...")
            sys.exit(0)

    else:
        return 'Invalid command'
