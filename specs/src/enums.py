from enum import Enum


class Command(Enum):
    """
    Enumuration of commands accepted by program.
    """
    CREATE_PARKING_LOT = 'Create_parking_lot'
    PARK = 'Park'
    LEAVE = 'Leave'
    SLOTS_BY_AGE = 'Slot_numbers_for_driver_of_age'
    REG_BY_AGE = 'Vehicle_registration_number_for_driver_of_age'
    SLOT_FOR_CAR_NUMBER = 'Slot_number_for_car_with_number'
    EXIT = 'exit'

    """ Checks whether command value exists or not"""
    @classmethod
    def has_command(cls, cmd):
        return cmd in cls._value2member_map_ 
