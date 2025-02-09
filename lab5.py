# ECOR 1041 Lab 5

__author__ = "Joshua Kwan"
__student_number__ = "101332749"

#======================================================
# Exercise 1

def tip(price_of_meal: float, customer_satisfaction: int) -> float:
    """ Return the amount of the tip based on customer satisfaction

    Precondition:1<= customer_satisfaction <=3, price_of_meal >= 0

    >>> tip(50,1)
    10.0

    >>> tip(200,2)
    30.0

    >>> tip(130, 3)
    6.5
    """

    if customer_satisfaction == 1:
        customer_tip = price_of_meal * 0.20

    elif customer_satisfaction == 2:
        customer_tip = price_of_meal * 0.15

    elif customer_satisfaction == 3:
        customer_tip = price_of_meal * 0.05

    return round(customer_tip, 2)


#======================================================
# Exercise 2

def coupon(amount_spent: float) -> float:
    """ Return the value of the coupon based on amount spent
    Precondition: amount_spent > 0

    >>> coupon(25)
    2.0

    >>> coupon(165)
    19.8

    >>> coupon(300)
    42.0

    """

    if amount_spent > 210:
        value_of_coupon = amount_spent * 0.14

    elif 210 >= amount_spent > 150:
        value_of_coupon = amount_spent * 0.12

    elif 150 >= amount_spent > 60:
        value_of_coupon = amount_spent * 0.10

    elif 60 >= amount_spent >= 10:
        value_of_coupon = amount_spent * 0.08

    elif 10 > amount_spent:
        value_of_coupon = 0

    return value_of_coupon


#======================================================
# Exercise 3

def bakers_party(is_weekend: bool, amount_of_pastries: int) -> bool:
    """ Return if bakers party was successful based on amount of pastries

    Precondition: amount_of_pastries >= 0

    >>> bakers_party(True, 30)
    False
    >>> bakers_party(False, 30)
    False
    >>> bakers_party(False, 50)
    True

    """

    if is_weekend == False: #weekdasy
        if 60 >= amount_of_pastries >= 40:
            party_is_success = True
        elif amount_of_pastries > 60:
            party_is_success = False
        elif amount_of_pastries < 40:
            party_is_success = False

    if is_weekend == True: #weekend
        if amount_of_pastries >= 40:
            party_is_success = True
        elif amount_of_pastries < 40:
            party_is_success = False

    return party_is_success


#======================================================
# Exercise 4

def squirrel_play(summer: bool, temp: float) -> bool:
    """ Return if squirrels are playing based on temp in F
 
    >>> squirrel_play(True, 120)
    False

    >>> squirrel_play(True, 83)
    True

    >>> squirrel_play(True, 40)
    False

    """

    if summer == True: #summer
        if temp > 100:
            squirrels_are_playing = False
        if 100 >= temp >= 60:
            squirrels_are_playing = True
        if temp < 60:
            squirrels_are_playing = False

    if summer == False:
        if temp > 90:
            squirrels_are_playing = False
        if 90 >= temp >= 60:
            squirrels_are_playing = True
        if temp < 60:
            squirrels_are_playing = False

    return squirrels_are_playing


#======================================================
# Exercise 5

def great_42(a: float, b: float) -> bool:
    """ Return if great 42 is acheived based on two integers given

    >>> great_42(30, 12)
    True

    >>> great_42(-50,-8)
    True

    >>> great_42(500, 0)
    False

    """
    if a == 42 or b == 42 or a + b == 42 or abs(a - b) == 42:
        great_42 = True
    else:
        great_42 = False

    return great_42



#======================================================
# Exercise 6

def multiply_uniques(a: int, b: int, c: int) -> int:
    """ Return the product based on given int values

    >>> multiply_uniques(8,8,9)
    9

    >>> multiply_uniques(1,2,3)
    6

    >>> multiply_uniques(3,3,3)
    1
    """

    if a == b == c:
        product = 1

    product = 1
    
    if a != b and a!= c:
        product *= a

    if b != a and b!= c:
        product *= b
    
    if c != a and c!= b:
        product *= c
 
    return product

