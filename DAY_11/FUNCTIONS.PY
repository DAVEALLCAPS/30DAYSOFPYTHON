
# ## 💻 Exercises: Day 11

# ### Exercises: Level 1

# 1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
def add_two_numbers(x, y):
    total = x + y
    return total

print(add_two_numbers(10, 5))
# 2. Area of a circle is calculated as follows: area = π x r x r. 
# Write a function that calculates _area_of_circle_.
def area_of_circle(rad):
    area = 3.14 * rad * rad
    return area

print(area_of_circle(13))
# 3. Write a function called add_all_nums which takes arbitrary number 
# of arguments and sums all the arguments. Check if all the list items 
# are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add_all_nums(1,2,3,4,5))
# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
def convert_cels_to_fahren(cels):
    fahren = (cels * 9/5) + 32
    return fahren

print(convert_cels_to_fahren(100))
# 5. Write a function called check-season, it takes a month parameter and returns 
# the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ['January', 'February', 'March']:
        return 'Winter'
    elif month in ['April','May','June']:
        return 'Spring'
    elif month in ['July','August','September']:
        return 'Summer'
    elif month in ['October','November','December']:
        return 'Autumn'
    else:
        return 'Invalid month.'

print(check_season('July'))
# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(c):
    c = c.split()
    slp = c[2].rstrip('x')
    return slp

print(calculate_slope("y = 25x + 4"))
# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
import cmath
from keyword import iskeyword

def solve_quadratic(a,b,c):
    d = (b**2) - (4*a*c)  
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print('The solutions are {0} and {1}'.format(sol1,sol2))

solve_quadratic(5,10,4)
# 8. Declare a function named print_list. It takes a list as a parameter and 
# it prints out each element of the list.
def print_list(a_list):
    i = 0
    while i < len(a_list):
        print(i, end=',')
        i += 1
    else:
        print(i)

ccccccc = [1,2,3,4,5,6,7,8]
print_list(ccccccc)
# 9. Declare a function named reverse_list. It takes an array as a parameter and 
# it returns the reverse of the array (use loops).
def reverse_list(list_to_reverse):
    reversed_ = []
    i = len(list_to_reverse) - 1
    while i >= 0:
        reversed_.append(list_to_reverse[i])
        i -= 1
    return reversed_

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))
# 10. Declare a function named capitalize_list_items. It takes a list as a 
# parameter and it returns a capitalized list of items
def capitalize_list_items(a_list):
    a_list = [names.capitalize() for names in a_list]
    return a_list

print(capitalize_list_items(['john', 'jacob', 'jingleheimer']))
# 11. Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.
def add_item(a_list, a_item):
    a_list.append(a_item)
    return a_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
# 12. Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it.
def remove_item(a_list, a_item):
    a_list.remove(a_item)
    return a_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds 
# all the numbers in that range.
def sum_of_numbers(numb):
    total = 0
    for i in range(0,numb+1):
        total += i
    return total

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds 
# all the odd numbers in that range.
def sum_of_odds(numb):
    total = 0
    for i in range(0,numb+1):
        if i % 2 != 0:
            total += i
    return total

print(sum_of_odds(100))
# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(numb):
    total = 0
    for i in range(0,numb+1):
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(100))

# ### Exercises: Level 2

# 1.  Declare a function named evens_and_odds . It takes a positive integer as parameter 
# and it counts number of evens and odds in the number.
def evens_and_odds(num):
    evenstotal = 0
    oddstotal = 0
    for i in range(0,num+1):
        if i % 2 != 0:
            oddstotal += 1
        elif i % 2 == 0:
            evenstotal += 1
    smth = f"Evens: {evenstotal}\nOdds: {oddstotal}"
    return smth

print(evens_and_odds(100))
# 2. Call your function factorial, it takes a whole number as a parameter 
# and it return a factorial of the number
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact

print(factorial(23))
# 3. Call your function _is_empty_, it takes a parameter and it checks if 
# it is empty or not
def is_empty(chk):
    if chk:
        return False
    else:
        return True

print(is_empty(0))
print(is_empty(100))
print(is_empty(""))
print(is_empty("check"))
# 4. Write different functions which take lists. They should calculate_mean, 
# calculate_median, calculate_mode, calculate_range, calculate_variance, 
# calculate_std (standard deviation).
from collections import Counter
import math

def calculate_mean(a_list):
    total = sum(a_list) / len(a_list)
    return total
def calculate_median(a_list):
    n = len(a_list)
    indx = n // 2
    if n % 2:
        return sorted(a_list)[indx]
    return sum(sorted(a_list)[indx - 1:indx + 1]) / 2
def calculate_mode(a_list):
    c = Counter(a_list)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]
def calculate_range(a_list):
    rnge = max(a_list) - min(a_list)
    return rnge
def calculate_variance(a_list):
    m = calculate_mean(a_list)
    var_res = sum((xi - m) ** 2 for xi in a_list) / len(a_list)
    return var_res
def calculate_std(a_list):
    var = calculate_variance(a_list)
    std_dev = math.sqrt(var)
    return std_dev

our_list = [1,2,2,3,4,5,6,7,8,9,10]
print(calculate_mean(our_list))
print(calculate_median(our_list))
print(calculate_mode(our_list))
print(calculate_range(our_list))
print(calculate_variance(our_list))
print(calculate_std(our_list))
# ### Exercises: Level 3

# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    prm = True
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                prm = False
            else:
                prm = True
    return prm

print(is_prime(2), is_prime(4))
# 2. Write a functions which checks if all items are unique in the list.
def is_unique(a_list):
    flg = 0
    flg = len(set(a_list)) == len(a_list)
    return flg

print(is_unique([1,2,3,4]), is_unique([1,1,1,2,3,4]))
# 3. Write a function which checks if all the items of the list are of the same data type.
def all_type(a_list):
    types_list = []
    for i in a_list:
        types_list.append(type(i))
    if all(x == types_list[0] for x in types_list):
        return True
    else:
        return False

print(all_type(['a','b','c']))
print(all_type([1,2,False,'Cats']))
# 4. Write a function which check if provided variable is a valid python variable
from keyword import iskeyword
def is_valid_var(c):
    if c.isidentifier() and iskeyword(c) == False:
        return True
    else:
        return False

print(is_valid_var('_yes_or_no_'),is_valid_var('True'),is_valid_var('exampleVar'), is_valid_var('3fake'))
# 5. Go to the data folder and access the countries-data.py file.

# - Create a function called the most_spoken_languages in the world. It should 
# return 10 or 20 most spoken languages in the world in descending order

# - Create a function called the most_populated_countries. It should return 10 
# or 20 most populated countries in descending order.

# 🎉 CONGRATULATIONS ! 🎉
