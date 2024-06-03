from math import pi
import random as rdm
import sys
from enum import Enum

import kansas

print(f"{pi:.25f}")
print(rdm.choice("123"))

for item in dir(rdm):
    print(item)

kansas.present()
print(kansas.capital)

print(__name__)  # __main__
print(kansas.__name__)  # kansas
