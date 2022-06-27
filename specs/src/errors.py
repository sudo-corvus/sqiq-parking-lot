__str__ = 'Errors specific to system'
__all__ = ['CarError', 'SizeError', 'FileError', 'SlotError' ]


class Error(Exception):
    pass

class CarError(Error):
    """ Car Registration number not found """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)

class SizeError(Error):
    """ Invalid size of Parking lot"""
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)

class FileError(Error):
    """
    Permission error or File not found
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)

class SlotError(Error):
    """
    Error when slot is already empty or Invalid slot size
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)



