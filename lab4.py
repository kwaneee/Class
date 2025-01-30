# ECOR 1041 Lab 4

__author__ = "Joshua Kwan"
__student_number__ = "101332749"

import math

# =====================================================
# Exercise 1

def area_of_disk(radius: float) -> float:
    """Return the area of a disk with the specified radius.
    Precondition: radius >= 0.
    >>> area_of_disk(5)
    78.54
    """
    return math.pi * radius ** 2



# =======================================================
# Exercise 2

LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934
#mpg_imperial = 32 
#liters_per_100km = 282.48 / mpg_imperial
def convert_to_litres_per_100_km(mpg: float) -> float:
    """Return a conversion of miles per imperial gallon to liters per 100 km
    
    >>> convert_to_litres_per_100_km(32.0)
    8.83
    >>> convert_to_litres_per_100_km(12.0)
    23.54
    >>> convert_to_litres_per_100_km(1.1)
    256.8
    """

    litres_per_100km = (100 * LITRES_PER_GALLON) / (mpg * KMS_PER_MILE)
    return round(litres_per_100km, 2)
# =======================================================
# Exercise 3

def amount_of_money(principal: float, rate: float, n: float, time: float) -> float:

# =======================================================
# Exercise 4

# Type your function definition for Exercise 4 here.

# =======================================================
# Exercise 5

# Type your function definitions for Exercise 5 here.

