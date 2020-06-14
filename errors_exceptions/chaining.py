#! usr/bin/python3
# UTF-8

import math
import traceback

class InclinationError(Exception):
    pass

def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        raise InclinationError("Slope cannot be vertical") from e

def main():
    try:
        inclination(0,5)
    except InclinationError as e:
        print(e.__traceback__)
        traceback.print_tb

if __name__ == '__main__':
    main()
    print("Finished")