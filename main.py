__author__ = 'Prince Kumar'
__email__ = 'neo11prince@gmail.com'

from specs.src.models.parking import Parking
from specs.src.controllers import command



def run():
    parking_lot = Parking()
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            result = command(line, parking_lot)
            print(result)


if __name__ == '__main__':
    run()
