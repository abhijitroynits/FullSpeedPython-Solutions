# Solutions for the book : http://joaoventura.net/static/files/python_exercises_book.pdf

# Exercise 3.1 Basic Datatypes

# 1. Try the following mathematical calculations and guess what is happening:(3/2),(3//2),(3%2),(3∗∗2)

print('3 / 2 =', 3 / 2)    # -> prints the quotient(float), ans: 1.5
print('3 // 2 = ', 3 // 2) # -> prints floored quotient(integer), ans : 1
print('3 % 2 =', 3 % 2)    # -> prints the remainder, ans : 1
print('3 ** 2 =', 3 ** 2)  # -> prints exponentiation result, ans : 9
print() # for spacing solved programs


# 2. Calculate the average of the following sequences of numbers: (2, 4), (4, 8, 9), (12, 14/6, 15)

seq1 = (2, 4)
seq2 = (4, 8, 9)
seq3 = (12, 14/6, 15)

print('Average of elements in (2, 4) ->', sum(seq1)/len(seq1))  # -> 3.0
print('Average of elements in (4, 8, 9) ->', sum(seq2)/len(seq2))  # -> 7.0
print('Average of elements in (12, 14/6, 15) ->', sum(seq3)/len(seq3)) # -> 9.777777777777779
print()

# 3. The volume of a sphere is given by (4/3)πr^3. Calculate the volume of a sphere of radius 5.
#   Suggestion: create a variable named "pi" with the value of 3.1415.

pi = 3.1415
radius = 5
volume = (4 * pi * (radius ** 3))/3
print('Volume of the sphere, (4 * pi * (radius ** 3))/3 -> ', volume)  # -> 523.5833333333334
print()

# 4. Use the module operator (%) to check which of the following numbers is even or odd: (1, 5, 20, 60/7).
#    Suggestion: the remainder of x/2 is always zero when x is even.

from fractions import Fraction

numbers = (1, 5, 20, 60/7)
fourth_element = Fraction(numbers[3]).limit_denominator()
fe_n = fourth_element.numerator
fe_d = fourth_element.denominator
print(f"{numbers[0]} is", 'even' if not numbers[0] % 2 else 'odd')  # -> odd
print(f"{numbers[1]} is", 'even' if not numbers[1] % 2 else 'odd')  # -> odd
print(f"{numbers[2]} is", 'even' if not numbers[2] % 2 else 'odd')  # -> even
print(f"{fe_n}/{fe_d} is", 'even' if not numbers[3] % 2 else 'odd') # -> odd
print()


# 5. Find some values for x and y such that x < 1/3 < y returns "True" on the Python REPL.
#    Suggestion: try 0 < 1/3 < 1 on the REPL.

# Consindering integers from -7 to 10.
import pprint

x_space = range(-7, 5)
y_space = range(-7, 5)
solution_set = []
for x in x_space:
    for y in y_space:
        if x < 1/3 < y:
            solution_set.append((x, y))

print("\nSolution set for x < 1/3 < y in the interval [-7, 5) ->")
pprint.pprint(solution_set)  #-> [(-7, 1),(-7, 2),(-7, 3),(-7, 4),...,]
print()

# Exercise 3.2 Exercises with strings
# 1. Initialize the string "abc" on a variable named "s":
# (a) Use a function to get the length of the string.
# (b) Write the necessary sequence of operations to transform the string "abc" to "aaabbbccc".
# Suggestion: Use string concatenation and string indexes.

s = "abc"
print("s =", s, ",Length of s =", len(s))  #-> abc, 3
t = s[0]*len(s) + s[1]*len(s) + s[2]*len(s)
print("\nTransformed string, t = s[0]*len(s) + s[1]*len(s) + s[2]*len(s) ->\n", t) #-> aaabbbccc
print()

# 2. Initialize the string "aaabbbccc" on a variable named "s":
# (a) Use a function that allows you to find the first occurence of "b" in the string,and the first occurence of "ccc".
# (b) Use a function that allows you to replace all occurences of "a" to "X", and
#     then use the same function to change only the first occurence of "a" to "X"

s = "aaabbbccc"
print("First occurence of 'b' in", s, "is at index:", s.find("b"))  #-> 3
print("First occurence of 'ccc' in", s, "is at index:", s.find("ccc")) #-> 6

s_X_rep_all_a = s.replace("a", "X")
print("\ns with all 'a' replaced by X ->", s_X_rep_all_a)    #-> XXXbbbccc

s_X_rep_one_a = s.replace("a", "X", 1)
print("s with first 'a' replaced by X ->", s_X_rep_one_a)  #-> XXXbbbccc
print()

# 3. Starting from the string "aaa bbb ccc", what sequences of operations do you need to arrive at the following strings?
#    You can find the "replace" function.
# (a) "AAA BBB CCC"
# (b) "AAA bbb CCC"

s = "aaa bbb ccc"
s_upper = s.upper()
print("\nFor the string, s =" , "\"" + s + "\"" , ", solution to question (a)->", s_upper)  #-> AAA BBB CCC

s_lower_b = s_upper.replace("B", "b")
print("For the string, s =" , "\"" + s + "\"" , ", solution to question (b)->", s_lower_b) #-> AAA bbb CCC


# Exercise 3.3 Exercises with lists
# Create a list named "l" with the following values ([1, 4, 9, 10, 23])
# 1. Using list slicing get the sublists [4, 9] and [10, 23].
l = [1, 4, 9, 10, 23]
slice1 = l[1:3]
slice2 = l[3:]
print("\nFor the given list l = {},".format(l), "\nl[1:3] =", slice1, ", and l[3:] =", slice2)  #-> [1, 4, 9, 10, 23], [4, 9], [10, 23]


# 2. Append the value 90 to the end of the list "l". Check the difference between list concatenation and the "append" method.
l.append(90)
print("\nUpdated list, l =", l)  #-> [1, 4, 9, 10, 23, 90] 


# 3. Calculate the average value of all values on the list. You can use the "sum" and "len" functions.
avg_of_l = sum(l)/len(l)
print("\nAverage of list elements =", avg_of_l)  #-> 22.833333333333332 


# 4. Remove the sublist [4, 9].
l[1:3] = []
print("\nAfter removing [4, 9], list l =", l)  #-> [1, 10, 23, 90]
print()

# Exercise 4.1 Exercises with the math module
# Use the python documentation about the math module to solve the following exercises:
# 1. Find the greatest common divisor of the following pairs of numbers: (15, 21), (152,200), (1988, 9765).

import math

pair1 = (15, 21)
pair2 = (152, 200)
pair3 = (1988, 9765)
print("\nGCD of (15, 21) =", math.gcd(*pair1))    #-> 3
print("GCD of (152, 200) =", math.gcd(*pair2))    #-> 8
print("GCD of (1988, 9765) =", math.gcd(*pair3))  #-> 7
print()

# 2. Compute the base-2 logarithm of the following numbers: 0, 1, 2, 6, 9, 15.
num_list = [0, 1, 2, 6, 9, 15]
try:
    print("\nlog2(0) =", math.log2(num_list[0]))  #-> ValueError : math domain error
except ValueError:
    print("Input proper values to log2(),", num_list[0], "isn't a plausible arg.")    

print("log2(1) =", math.log2(num_list[1]))    #-> 0.0
print("log2(2) =", math.log2(num_list[2]))  #-> 1.0
print("log2(6) =", math.log2(num_list[3]))  #-> 2.584962500721156
print("log2(9) =", math.log2(num_list[4]))  #-> 3.169925001442312
print("log2(15) =", math.log2(num_list[5]))  #-> 3.9068905956085187


# 3. Use the "input" function to ask the user for a number and show the result of the sine, cosine and tangent of the number.
#    Make sure that you convert the user input from string to a number (use the int() or the float() function).

try:
    angle = float(input("\nEnter a number for basic trig computation: "))
    print(f"Sine of {angle} =", math.sin(angle))
    print(f"Cosine of {angle} =", math.cos(angle))
    print(f"Tangent of {angle} =", math.tan(angle))
except Exception as e:
    print("Bad input; Exception =", e)

print()


# Exercise 4.2 Exercises with functions
# 1. Implement the "add2" function that receives two numbers as arguments and returns the sum of the numbers.
#    Then implement the "add3" function that receives and sums 3 parameters.

def add2(a, b):
    return a + b

def add3(a, b, c):
    return add2(add2(a,  b), c)

print("\nCalling add2(1, 2), Sum =", add2(1,2))       #->  3
print("Calling add3(3, 4, 5), Sum =", add3(3, 4, 5))  #->  12
print()

# 2.Implement a function that returns the greatest of two numbers given as parameters.
#   Use the "if" statement to compare both numbers.

def greater_of_two(a, b):
    try:
        if a > b:
            return a
        elif b > a:
            return b
        elif a == b:
            return 'Equal inputs'
    except Exception as _:   # Ignoring the exception msg for brevity!
        return 'Inputs cannot be compared'

print("\ngreater_of_two(3, -9) ->", greater_of_two(3, -9))    #-> 3
print("greater_of_two(37, 200) ->", greater_of_two(37, 200))  #-> 200
print("greater_of_two(89, 89) ->", greater_of_two(89, 89))    #-> Equal inputs
print("greater_of_two(67, \"river\") ->", greater_of_two(67, "river"))   #-> Inputs cannot be compared
print()

# 3. Implement a function named "is_divisible" that receives two parameters (named"a" and "b")
#    and returns true if "a" can be divided by "b" or false otherwise.
#    A number is divisible by another when the remainder of the division is zero. Use the modulo operator ("%").


def is_divisible(a, b):
    if a % b == 0:
        return True
    else:
        return False

print("\nis_divisible(4, 2) =", is_divisible(4, 2))     #-> True
print("is_divisible(47, 23) =", is_divisible(47, 23))   #-> False
print()

# 4. Create a function named "average" that computes the average value of a list passed as parameter to the function.
#    Use the "sum" and "len" functions.

def average(num_list):
    if len(num_list) > 0:
        return sum(num_list)/len(num_list)
    else:
        return 'Invalid denominator'

print("\naverage([2, 4, 6]) ->", average([2, 4, 6]))     #-> 4.0
print("average([-2, -4, 6]) ->", average([-2, -4, 6]))   #-> 0.0
print("average([]) ->", average([]))                     #-> Invalid denominator
print()


# Exercise 4.4 Exercises with recursive functions
# 1. Implement the factorial function and test it with several different values. Cross-check with a calculator.

def factorial(x):
    if x == 0:
        return 1
    elif x > 0:
        return x * factorial(x - 1)
    else:
        return 'Invalid arg.'

print("\nfactorial(4) =", factorial(4))    #-> 24
print("factorial(10) =", factorial(10))    #-> 3628800
print("factorial(-4) =", factorial(-4))    #-> Invalid arg.
print("factorial(0) =", factorial(0))      #-> 1
print()


# 2. Implement a recursive function to compute the sum of the n first integer numbers(where n is a function parameter).
#    Start by thinking about the base case (the sum of the first 0 integers is?) and then think about the recursive case.

def sum(n):
    if n == 0:
        return 0
    elif n > 0:
        return n + sum(n-1)
    else:
        return 'Invalid arg.'

print("\nsum(0) =", sum(0))     #-> 0
print("sum(1) =", sum(1))       #-> 1
print("sum(100) =", sum(100))   #-> 5050
print("sum(-54) =", sum(-54))   #-> Invalid arg.
print()

# 3. The Fibonnaci sequence is a sequence of numbers in which each number of the sequence matches
#    the sum of the previous two terms.
#    Given the following recursive definition implement fib(n).

#    fib(n) = 0, if x = 0
#    fib(n) = 1, if x = 1
#    fib(n) = fib(n-1) + fib(n-2), otherwise

# Check your results for the first numbers of the sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

print('\nGenerating 12 terms of fibonacci sequence ->')
def create_fib_term(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x > 1:
        return create_fib_term(x - 1) + create_fib_term(x - 2)


def create_fib_seq(n):
    term_indices = list(range(n))
    fib_seq = [create_fib_term(i) for i in term_indices]  # list comprehension
    return fib_seq
    
print(create_fib_seq(12))  #-> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print()


# Exercise 5.1 Exercises with the for loop
# For this section you may want to consult the python docs at > https://docs.python.org/3/tutorial/controlflow.html

# 1. Create a function "add" that receives a list as parameter and returns the sum of all elements in the list.
#   Use the "for" loop to iterate over the elements of the list.

def add(aList):
    sum = 0
    for i in range(len(aList)):
        sum += aList[i]
    return sum

print('\nSum of elements in [1, 2, 3] =', add([1, 2, 3]))      #-> 6
print('Sum of elements in [5, 6, 7, 8] =', add([5, 6, 7, 8]))  #-> 26
print()

# 2. Create a function that receives a list as parameter and returns the maximum value in the list.
#    As you iterate over the list you may want to keep the maximum value found
#    so far in order to keep comparing it with the next elements of the list.

def max_elem(aList):
    greatest = aList[0]
    for item in aList:
        if item > greatest:
            greatest = item
    return greatest

print('\nGreatest item in [-5, 3, 33, 87, 200] =', max_elem([-5, 3, 33, 87, 200]))          #-> 200
print('Greatest item in [-100, -85, -24, -2, -2] =', max_elem([-100, -85, -24, -2, -2]))    #-> -2


# 3. Modify the previous function such that it returns a list with the first element being the maximum value
#    and the second being the index of the maximum value in the list.
#    Besides keep the last maximum value found so far, you need to keep also the position where it occured.

def max_elem_with_index(aList):
    greatest = aList[0]
    g_index = 0
    for index, item in enumerate(aList):
        if item > greatest:
            greatest = item
            g_index = index
    return [greatest, g_index]

print('\nGreatest item and its index in [-5, 3, 33, 87, 200] =', max_elem_with_index([-5, 3, 33, 87, 200]))          #-> [200, 4]
print('Greatest item and its index in [-100, -85, 24, -2, 1] =', max_elem_with_index([-100, -85, 24, -2, -1]))       #-> [24, 2]
print()


# 4. Implement a function that returns the reverse of a list received as parameter.
#    You may create an empty list and keep adding the values in reversed order as they come from the original list.
#    Check what you can do with lists at > https://docs.python.org/3/tutorial/datastructures.html

def rev_list(aList):
    new_list = []
    for i in range(len(aList)):
        new_list.append(aList[-1 - i])
    return new_list


print("\nrev_list([4, 5, 6, 8, 9 , 24]) =", rev_list([4, 5, 6, 8, 9, 24]))        #-> [24, 9, 8, 6, 5, 4]
print("rev_list([-4, 20, 32, 98, 0 , 60]) =", rev_list([-4, 20, 32, 98, 0, 60]))  #-> [60, 0, 98, 32, 20, -4]
print()


# 5. Make the function "is_sorted" that receives a list as parameter and returns True
#    if the list is sorted by increasing order. For instance [1, 2, 2, 3] is ordered while [1, 2, 3, 2] is not.
#    Suggestion: you have to compare a number in the list with the next one, so you can use indexes
#    or you need to keep the previous number in a variable as you iterate over the list.
    
def is_sorted(aList):
    prev_num = aList[0]
    for item in aList:
        if item >= prev_num:
            prev_num = item
        else:
            return False
    return True

print("\nis_sorted([1, 2, 3, 4, 5, 99]) ->", is_sorted([1, 2, 3, 4, 5, 99]))          #-> True
print("is_sorted([-2, -1, 0, 4, 5, 3, 76]) ->", is_sorted([-2, -1, 0, 4, 5, 3, 76]))  #-> False
print("is_sorted([1, 2, 3, 3, 5, 5]) ->", is_sorted([1, 2, 3, 3, 5, 5]))              #-> True
print()


# 6. Implement the function "is_sorted_dec" which is similar to the previous one but
#    all items must be sorted by decreasing order.

# Let us use the previous functions with the key idea that if the reversed list is sorted in ascending order,
# we can conclude that the incoming list is sorted in descending order.
# For example, the list [3, 2, 1] when reversed is in asceding order, also the last element of the incoming list
# must be the minimum element.


def is_sorted_dec(aList):
    reversed_list = rev_list(aList)
    is_last_elem_min = (min(aList) == aList[-1])
    return (is_sorted(reversed_list) and is_last_elem_min)

print("\nis_sorted_dec([1, 2, 3, 4, 5, 99]) ->", is_sorted_dec([1, 2, 3, 4, 5, 99]))  #-> False
print("is_sorted_dec([6, 5, 4, 3, 2, 1]) ->", is_sorted_dec([6, 5, 4, 3, 2, 1]))      #-> True
print("is_sorted_dec([6, 5, 4, -3, 2, 1]) ->", is_sorted_dec([6, 5, 4, -3, 2, 1]))      #-> False
print()


# 7. Implement the "has_duplicates" function which verifies if a list has duplicate values.
#    You may have to use two "for" loops, where for each value you have to check for duplicates on the rest of the list.

def has_duplicates(aList):
    for index1, item1 in enumerate(aList):
        for index2, item2 in enumerate(aList):
            if item1 == item2 and index1 != index2:
                return True
    return False

print('\nhas_duplicates([6, 6, 7, 8, 9, 0]) ->', has_duplicates([6, 6, 7, 8, 9, 0]))              #-> True
print('has_duplicates(["a", "b", "c", "d", "e"]) ->', has_duplicates(["a", "b", "c", "d", "e"]))  #-> False
print()

# Exercise 5.2 Exercises with the while statement
# 1. Implement a function that receives a number as parameter and prints, in decreasing order,
#    which numbers are even and which are odd, until it reaches 0.

##>>> even_odd (10)
##Even number :  10
##Odd number :  9
##Even number :  8
##Odd number :  7
##Even number :  6
##Odd number :  5
##Even number :  4
##Odd number :  3
##Even number :  2
##Odd number :  1

def even_odd(num):
    while num > 0:
        if num % 2 == 0:
            print("Even number :", num)
        else:
            print("Odd number :", num)
        num -= 1


even_odd(10)  #->  prints as per shown in question
print()

# Exercise 6.1 Exercises with dictionaries
# Use the python documentation at > https://docs.python.org/3/tutorial/datastructures.html to solve the
# following exercises

# Take the following python dictionary:

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10
}

# 1. How many students are in the dictionary? Search for the "len" function.
print("\nNumber of students in ages = {} ->".format(ages), "\nlen(ages)= " + str(len(ages)))  #-> 8


# 2. Implement a function that receives the "ages" dictionary as parameter and return the average age of the students.
#    Traverse all items on the dictionary using the "items" method as above.

def avg_age(data):
    sum_ages = 0
    for _ , values in data.items(): # discarding the keys
        sum_ages += values
    return sum_ages/len(data)


print("\nAverage age of students =", avg_age(ages))  #-> 10.375


# 3. Implement a function that receives the "ages" dictionary as parameter and
#    returns the name of the oldest student.

def max_age(data):
    for k, v in data.items():
        if v == max(list(data.values())):
            return k

print("Student having max age ->", max_age(ages))  #-> Maria


# 4. Implement a function that receives the "ages" dictionary and a number "n" and returns a new dict where each student is n years older.
#    For instance, new_ages(ages,10) returns a copy of "ages" where each student is 10 years older.


def new_ages(data, n):
    new_ages_dict = {}
    for k, v in data.items():
        if v == n:
            new_ages_dict[k] = v
    return new_ages_dict

print("new_ages(ages, 10) ->", new_ages(ages, 10))   #-> {'Peter': 10, 'Thomas': 10, 'Bob': 10, 'Gabriel': 10}
print("new_ages(ages, 11) ->", new_ages(ages, 11))   #-> {'Isabel': 11, 'Joseph': 11}
print()        

# Exercise 6.2 Exercises with sub-dictionaries
# Take the following dictionary:
students = {
     "Peter": {"age": 10, "address": "Lisbon"},
     "Isabel": {"age": 11, "address": "Sesimbra"},
     "Anna": {"age": 9, "address": "Lisbon"}
}


# 1. How many students are in the "students" dict? Use the appropriate function.
print("\nNumber of students in the dictionary =", len(students))   #-> 3

# 2. Implement a function that receives the students dict and returns the average age.
def avg_student_age(data):
    sum_ages = 0
    counter = 0
    for info in data.values():
        for k, v in info.items():
            if k is "age":
                sum_ages += v
                counter += 1
    return sum_ages/counter


print("\navg_student_age(students) =", avg_student_age(students))  #-> 10.0


# 3. Implement a function that receives the students dict and an address, and returns a list with
#    the name of all students which address matches the address in the argument.
#    For instance, invoking "find_students(students, ’Lisbon’)" should return Peter and Anna.

def find_students(data, address):
    address_map = []
    for k, v in data.items():
        if v["address"] == address:
            address_map.append(k)
    return address_map


print("find_students(students, \"Sesimbra\") =", find_students(students, "Sesimbra"))   #-> ['Isabel']
print("find_students(students, \"Lisbon\") =", find_students(students, "Lisbon"))       #-> ['Peter', 'Anna']
print()



# Exercise 7.1 Exercises with classes
# Use the python documentation on classes > https://docs.python.org/3/tutorial/classes.html
# to solve the following exercises.

# 1. Implement a class named "Rectangle" to store the coordinates of a rectangle given by
#    the top-left corner (x1, y1) and the bottom-right corner (x2, y2).
# 2. Implement the class constructor with the parameters (x1, y1, x2, y2) and store them in the class instances using the "self" keyword.
# 3. Implement the "width()" and "height()" methods which return, respectively, the width and height of a rectangle.
#    Create two objects, instances of "Rectangle" to test the calculations.

# N. B: The question was corrected from the following URL :
#       https://github.com/joaoventura/full-speed-python/commit/bc4d68ebdd2cf7131e38b3626cb6ab667c32b1c7

# 4. Implement the method "area" to return the area of the rectangle (width*height).
# 5. Implement the method "circumference" to return the perimeter of the rectangle (2*width + 2*height).
# 6. Do a print of one of the objects created to test the class. Implement the "__str__"method such that when
#    you print one of the objects it print the coordinates as (x1,y1)(x2, y2).

class Rectangle():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return str((self.x1,self.y1)) + str((self.x2, self.y2))

    def width(self):
        self.width = math.fabs(self.x2 - self.x1)
        return self.width

    def height(self):
        self.height = math.fabs(self.y2- self.y1)
        return self.height

    def area(self):
        return self.width * self.height

    def circumference(self):
        return (2 * self.width + 2 * self.height)

rect1 = Rectangle(1, 2, 5, 0)
rect2 = Rectangle(2, 4, 5, 2)
print("\n Rectangle class in action...")
print("rect1.width() =", rect1.width(), ", rect1.height() =", rect1.height())   #-> 4.0, 2.0
print("rect2.width() =", rect2.width(), ", rect2.height() =", rect2.height())   #-> 3.0, 2.0
print("Area of rect1 =", rect1.area())   #-> 8.0
print("Area of rect2 =", rect2.area())   #-> 6.0
print("Perimeter of rect1 =", rect1.circumference())  #-> 12.0
print("Perimeter of rect2 =", rect2.circumference())  #-> 10.0
print("String representation of rect1 ->", rect1)   #-> (1, 2) (5, 0)
print("String representation of rect2 ->", rect2)   #-> (2, 4) (5, 2)
print()

# Exercise 7.3 Exercises with inheritance
# Use the "Rectangle" class as implemented above for the following exercises:

# 1. Create a "Square" class as subclass of "Rectangle".
# 2. Implement the "Square" constructor. The constructor should have only the x1, y1 coordinates and the size of the square.
#    Notice which arguments you’ll have to use when you invoke the "Rectangle" constructor when you use "super".
# 3. Instantiate two objects of "Square", invoke the area method and print the objects. Make sure that all calculations are returning
#    correct numbers and that the co-ordinates of the squares are consistent with the size of the square used as argument.


class Square(Rectangle):
    def __init__(self, x1, y1, size):
        super().__init__(x1, y1, x1 + size, y1 - size)
        self.size = size


square1 = Square(4, 2, 2)
square2 = Square(2, 2, 3)

print("\nString representation of square1 ->", square1)  #-> (4, 2)(6, 0)
print("String representation of square1 ->", square2)    #-> (2, 2)(5, -1) 
print("square1.width() =", square1.width(),", square1.height() =" ,square1.height())   #-> 2.0, 2.0
print("square2.width() =", square2.width(),", square2.height() =" ,square2.height())   #-> 3.0, 3.0
print("square1.area() =", square1.area())  #-> 4.0
print("square2.area() =", square2.area())  #-> 9.0
























