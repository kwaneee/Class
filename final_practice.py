import random

string = " "
for x in range(13, 29, 3):
    string += str(x) + ", "
print(string) 


a_list = [1, 3, 7, 2]

for i in range (len(a_list)):
    print(a_list[i])

def find_smallest(a_list: list) -> list:

    smallest = 0

    for i in range (len(a_list)):
        if a_list[i] < a_list[smallest]:
            smallest = i
    return smallest

def doubled(a_list: list[float]) -> list[float]:
    double = [0, 0, 0, 0]

    for i in range (len(a_list)):
        double[i] = 2 * a_list[i]
    
    return double


import random

def doubled(a_list: list[float]) -> list[float]:
    double = [0] * len(a_list)
    a_list = [1, 2, 3, 4]
    for i in range (len(a_list)):
        double[i] = 2 * a_list[i]
    return double

x = 13
if x > 12 or x < 15 and x == 16:
    print("Hi")
else:
    print("Bye") 
"""
a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))
if a <= 0:
    b = b + 1
else:
    a = a + 1 
"""


for i in range (6):
    print(i)


def fuzzy(x):
    x = 73
    print(x)
def bunny():
    x = 29
    fuzzy(x)
    print(x) 


def increment(x):
    x = x + 1
    return x
z = 4
y = increment(z) #Line A
x = y 
print (z)
print (y)


3//25
1.2%4

10/6

5 * 2 / 6 % 4 - 5 // 2 * 3 % 2 

count_a = 0
count_b = 0
for number in range(2, 10):
    count_a = count_a + 1
    if count_a % 2 == 0:
        count_b = count_b + count_a
        count_b = count_b + 1
print("count_a:", count_a, "count_b:", count_b)

"""

-76 as a 2's component's binary nuber with bits

76/2 = 38 -- 0

38/2 = 19 0

19/2 = 9  1

9/2 = 4  1

4/2 = 2  0

2/2 = 1  0

1/2 = 0  1

00011001

01001100

  10110011
+        1
-----------
    10110100




27/2 = 13  1
13/2 = 6   1
6/2 = 3  0
3/2 = 1  1
1/2 = 0  1

.11011
"""


string = ""
for i in range(13, 29, 3):
    string += str(i) + ", "
print (string)


"""
line 1: missing :
line 15: should not be '''
line 17: remove ;
line 19: add range and len
20: not correct condition
16: add num_ten = 0
27: bad indentation
29: add ]
make % 2 the if and put % 10 into that if 


"""



def consonants_finder(s: str) -> int:
    consonants = 0
    
    for i in s:
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            consonants += 1
        
    return consonants


#OR

def consonants_finder(b: str) -> int:
    consonants = 0
    
    vowels = "aeiouAEIOU"

    for i in b:
        if i not in vowels:
            consonants += 1
        
    return consonants