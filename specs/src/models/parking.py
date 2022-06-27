from specs.src import errors
from specs.src.enums import Command

__all__ = ['Parking']


class Parking(object):
    """
    Class used to manage the parking lot.
    Includes methods to add, remove, and enquire info about parking lot
    """

    def __init__(self):
        self.commands = Command
        self.parking_capacity = 0
        self.slot_status = dict()

    def initialise_parking(self, size):
        """
        Initialization of parking lot with size
        :param size: Space allocated to parking lot
        :return: None
        """
        if int(size) > 0:
            self.parking_capacity = int(size)
        else:
            self.parking_capacity = 0
            raise errors.SizeError('Invalid parking size, size cannot be negative or zero.')

        self.slot_status = {i + 1: None for i in range(self.parking_capacity)}

    @property
    def get_parking_size(self):
        """
        Total space allocated to parking lot
        :return: Total slots in parking lot
        """

        return self.parking_capacity

    def _avaiable_slot(self):
        """
        List of slot which are not assigned yet.
        :return: Empty slots
        """
        slot = [_slot for _slot in self.slot_status if self.slot_status[_slot] is None]
        if len(slot) != 0:
            return min(slot)
        return None

    def __parked_cars(self):
        """
        Provides info related status of slots whether occupied by car or empty
        :return:
        """
        return {i: self.slot_status[i] for i in self.slot_status if self.slot_status[i] is not None}

    def add_car(self, car_object):
        """
        Adds car object to parking slot
        :param car_object:  Car class instance
        :return: Status of car parked or not
        """

        if car_object.get_registration_number and car_object.get_driver_age:
            slot_avaible = self._avaiable_slot()
            if slot_avaible is not None:
                self.slot_status.update({slot_avaible: car_object})
                return "{}".format(slot_avaible)
            raise errors.SlotError('Inconvenience is regretted, Parking lot is full.')
        raise errors.CarError('Invalid car details')

    def remove_car(self, slot_number):
        """
        Empty the slot when car leaves occupied parking slot
        :param slot_number: Slot number allocated to parked car
        :return: Removed car object
        """

        if slot_number in self.slot_status.keys():
            if self.slot_status[slot_number] is not None:
                removed_car = self.slot_status[slot_number]
                self.slot_status[slot_number] = None
                return removed_car
            else:
                raise errors.SlotError('Slot is already empty')
        else:
            raise errors.SlotError('Invalid slot number')

    def get_status(self):
        """
        Provide status of available slots
        :return:
        """
        return self.slot_status

    def get_car_reg_by_age(self, age):
        """
        list of car registration numbers seperarated by comma
        :param color: age of driver
        :return: string of cars registration numbers matching the age of driver
        """
        cars = [car.get_registration_number for car in self.__parked_cars().values() if car.get_driver_age == age]
        if len(cars) > 0:
            return ', '.join(cars)
        else:
            raise errors.CarError('No car with Reg {} found '.format(age))

    def slot_num_by_age(self, age):

        """
        Provide slot number occupied with given age of driver
        :param color: 
        :return: List of slot numbers matching age of driver
        """
        slot_number = [_slot_number for _slot_number in self.__parked_cars().keys()
                       if self.__parked_cars()[_slot_number].get_driver_age == age]

        if len(slot_number) > 0:
            slot_numbers = list(map(str, slot_number))
            return ', '.join(slot_numbers)
        return 0

    def slot_num_with_registration_number(self, reg_num):
        """
        Provide slot number for given registration number
        :param reg_num: Registration number of car
        :return: Slot number of car for given registration number
        """
        slot_number = [str(_slot_number) for _slot_number in self.__parked_cars().keys()
                       if self.__parked_cars()[_slot_number].get_registration_number == reg_num]
        if len(slot_number) > 0:
            return ', '.join(slot_number)
        return 0
