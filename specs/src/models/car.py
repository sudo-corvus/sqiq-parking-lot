
__all__ = ['Car']


class Car(object):
    """
    Defines the properties of car
    Includes : car "registration number" and "driver age" of driver
    """

    def __init__(self, registration_number, driver_age):
        """
        Initialization of Car object
        :param registration_number: registation number of car
        :param driver_age: age of driver
        """
        self._reg_number = registration_number
        self._driver_age = driver_age

    @property
    def get_registration_number(self):
        """
        Return Registration number of the car
        """
        return self._reg_number

    @property
    def get_driver_age(self):
        """
        Return Age of driver
        """
        return self._driver_age
