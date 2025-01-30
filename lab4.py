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
    >>> area_of_disk(0)
    0.0
    >>> area_of_disk(10.0)
    314.16
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

    #litres_per_100km = (100 * LITRES_PER_GALLON) / (mpg * KMS_PER_MILE)
    #return round(litres_per_100km, 2)
    return round((100 * LITRES_PER_GALLON) / (mpg * KMS_PER_MILE), 2)

# =======================================================
# Exercise 3

def accumulated_amount(principal: float, rate: float, n: float, time: float) -> float:
    """ Return amount of money you'll have when money is deposited, based on the pricnipal, the annual rate of interest, the number of times interest is compunded per year and the amount of years since the principal is deposited.

    Precondition: principal >= 0, rate >= 0, n > 0, time >= 0
    
    >>> amount_of_money(1500, 0.043, 4, 6)
    1938.84
    >>> amount_of_money(100, 0.05, 1, 9)
    155.13
    >>> amount_of_money(10000, 0.1, 3, 4)
    14821.26
    """
    return round(principal * ((1 + rate / n) ** (n * time)), 2)


# =======================================================
# Exercise 4

def area_of_cone(height: float, radius: float) -> float:
    """ Return lateral surface area of cone based on height and radius
    
    Precondition: height >= 0, radius >= 0

    >>> area_of_cone(0.0, 0.0)
    0.0
    >>> area_of_cone(2.0, 2.0)
    25.13
    >>> area_of_cone(5.0, 5.0)
    392.70
    """

    return math.pi * radius * (radius ** 2 + height ** 2) ** 0.5
# =======================================================
# Exercise 5

def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """ Return distance based on two points and coordinates
    
    >>> distance(1, 2, 3, 4)
    2.83
    >>> distance(3, 1, 6, 9)
    8.54
    >>> distance(7, 7, 8, 8)
    1.41
    """
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


def area_of_circle(xc: int, yc: int, xp: int, yp: int) -> float:
    """ Return area of circle based on the coordinates of two points, the center of a cirlce and a point on the perimiter

    >>> area_of_circle(0, 0, 0, 0)
    0.0
    >>> area_of_circle(3, 6, 9, 1)
    191.64
    >>> area_of_circle(8, 9, 10, 15)
    125.66
    
    """
    return abs(area_of_disk(distance(xc, yc, xp, yp)))

