# ECOR 1041 - Bonus

__author__ = "Joshua Kwan"
__student_number__ = "101332749"

# ======================================================
# Exercise 1

def replicate(word: str) -> str:
    """Return the parameter reapeated with the number of copies eaqual to the
    number of characters.
    
    >>> replicate('spring')
    'springspringspringspringspringspring'
    
    >>> replicate ('abc')
    'abcabcabc'
    
    >>> replicate ('hi')
    'hihi'

    """
    return word * len(word)

# ======================================================
# Exercise 2

def repeat_separator(word: str, sep: str, n: int) -> str:
    """return a string given a certain number of times specified seperated by a specific string
    
    >>> repeat_separator('cold' , X, 3)
    'coldXcoldXcold'
    
    >>> repeat_separator('cold' , 'X', 0)
    'cold'
    
    >>> repeat_separator('a', 'x', 1)
    'a'
    """
    longstring = (word + sep) * (n - 1)
    return longstring + word


# ======================================================
# Exercise 3

def has_pair(s: str, ch: str) -> bool:
    """return True if a character is repeated twice in sequence 
    
    >>> has_pair('screech', 'e')
    True
    >>> has_pair('treat', 't')
    True
    >>> has_pair('Aaron', 'a')
    False"""

    for i in range(len(s) - 1):
        if s[i] == ch and s[i + 1] == ch:
            return True
    return False


# ======================================================
# Exercise 4

def middle_way(first: list, second: list) -> list:
    """return a new list containing the middle int of both lists given
    Preconidition: Parameters must both be lists containing 3 ints each
    
    >>> middle_way([1,2,3], [3,4,5])
    [2,4]
    
    >>> middle_way([9,3,1], [9,0,8])
    [3,0]
    
    >>> middle_way([1,12,4], [6,7,8]])
    [12,7]
    """
    new_list = [first[1], second[1]]
    return new_list


# ======================================================
# Exercise 5

def make_ends(new_list: list) -> list:
    
    """return a new list that contains the first and last element of the original list
    
    Precondition: the original list must not be empty
    
    >>> make_ends([10])
    [10,10]
    
    >>> make_ends([10,2,4,9])
    [10,9]
    
    >>> make_ends([1, 3,7,0])
    [1,0]
    
    """

    return [new_list[0], new_list[len(new_list) - 1]]


# ======================================================
# Exercise 6

def common_end(first_list: list, second_list: list) -> bool:
    
    """return True if both the first or both the last elements of each list is the same or if the first and last element of each list is the same
    
    Precondition: The elements of the list must be ints, and the list must not be empty
    
    >>> common_end([6,2,5],[3,1,5])
    True
    
    >>> common_end([7,2,9,0],[3,1,5])
    False
    
    >>> common_end([6,2,3,4,5,6],[3,1,5,6,7,8,9,0,3])
    True
    """
    if first_list[0] == second_list[0] or first_list[len(first_list) - 1] == second_list[len(second_list) - 1] or (first_list[0] == first_list[len(first_list) - 1] and second_list[len(second_list) - 1] == second_list[0]):
        return True
    else:
        return False


# ======================================================
# Exercise 7

def count_evens(lst1: list) -> int:
    """return the number of even numbers in a list
    Preconditions: elements in list must be ints
    
    >>>count_evens([3,4,5,5,6,7,8,9])
    3
    
    >>>count_evens([1,3,5,7,9])
    0
    
    >>>count_evens([4,2])
    2
    """
    even_counter = 0
    for i in range(len(lst1)):
        if lst1[i] % 2 == 0:
            even_counter += 1

    return even_counter


# ======================================================
# Exercise 8

def big_diff(lst: list) -> int:
    """ Return the difference between the largest and smallest elements in the lsit
    
    """

    smallest = lst[0]
    largest - lst[0]

    for i in range(len(lst)):

        if smallest > lst[i]:
            smallest = lst[i]
            
        if largest < lst[i]:
            largest = lst[i]

    return largest - smallest

# ======================================================
# Exercise 9

def has22(lst: list) -> bool:
    counter = 0
    for i in range(1, len(lst)):
        if lst[i] == 2 and lst [i - 1] == 2:
            has22 = True
        else:
            has22 = False

    return has22


# ======================================================
# Exercise 10

def centered_average(lst: list) -> float:
    """
    Computes the centered average of a list of integers.

    The centered average is the mean of the list after removing exactly
    one smallest and one largest value.

    :param nums: List of integers (at least 3 elements)
    :return: The centered average as a float
    """
    min_val = min(lst)
    max_val = max(lst) 

    min_removed = False
    max_removed = False
    total = 0
    count = 0

    for i in lst:
        if i == min_val and not min_removed:
            min_removed = True
        elif i == max_val and not max_removed:
            max_removed = True
        else:
            total += i
            count += 1

    return total / count

# ======================================================
# Exercise 11

def bank_statement(lst: list) -> list:
    withdrawl = 0
    deposit = 0
    for i in range(len(lst)):
        if lst[i] >= 0:
            deposit += lst[i]
        else:
            withdrawl += lst[i]
    return [round(deposit, 2), round(withdrawl, 2), round(deposit + withdrawl, 2)]


# ======================================================
# Exercise 12

def reverse(lst: list) -> list:
    n = len(lst)
    reversed_list = [0] * n 
    for i in range(n):
        reversed_list[n - 1 - i] = lst[i]

    return reversed_list


