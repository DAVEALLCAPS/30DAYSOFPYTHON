
# ## 💻 Exercises: Day 14

import collections
from functools import reduce


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ### Exercises: Level 1
'''
# 1. Explain the difference between map, filter, and reduce. 
- map takes a function and iterable
- filter takes function that returns a boolean and an iterable
- reduce takes a function and iterable and returns and single value

# 2. Explain the difference between higher order function, closure and decorator
# - high order functions return or use other functions as params
# - closure is a nested function that refers to a value in the enclosing func and
#       the enclosing func returns the nested func
# - decorators take in a function, add some functionality and return it 
'''
# 3. Define a call function before map, filter or reduce, see examples.
# 4. Use for loop to print each country in the countries list.
def print_list_1by1(lst):
    for i in lst:
        print(i, end=" ")

print_list_1by1(countries)
# 5. Use for to print each name in the names list.
print_list_1by1(names)
# 6. Use for to print each number in the numbers list.
print_list_1by1(numbers)

# ### Exercises: Level 2

# - Use map to create a new list by changing each country to uppercase in the countries list
map_upper = map(lambda c : c.upper(),countries)
print(list(map_upper))
# - Use map to create a new list by changing each number to its square in the numbers list
num_sq = map(lambda c : c ** 2,numbers)
print(list(num_sq))
# - Use map to change each name to uppercase in the names list
name_upper = map(lambda c : c.upper(),names)
print(list(name_upper))
# - Use filter to filter out countries containing 'land'.
land_filter = filter(lambda c : 'land' not in c, countries)
print(list(land_filter))
# - Use filter to filter out countries having exactly six characters.
six_filter = filter(lambda c : len(c) != 6, countries)
print(list(six_filter))
# - Use filter to filter out countries containing six letters and more in the country list.
sixmore_filter = filter(lambda c : len(c) < 6, countries)
print(list(sixmore_filter))
# - Use filter to filter out countries starting with an 'E'
startE_filter = filter(lambda c : c[0] != 'E', countries)
print(list(startE_filter))
# - Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
nums_zero_to_20 = [i for i in range(0,21)]
print(nums_zero_to_20)
chain_two = filter(lambda c : c % 2 == 0, filter(lambda x : x >= 10,nums_zero_to_20))
print(list(chain_two))
# - Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    if type(lst) == str:
        return lst
    else:
        pass

mix_list = [1,2,'one','two',True,'random','stringstringstring']
chk = filter(get_string_lists, mix_list)
print(list(chk))
# - Use reduce to sum all the numbers in the numbers list.
def add_two_nums(x,y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers)
print(total)
# - Use reduce to concatenate all the countries and to produce this sentence: 
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
concatstring = reduce(lambda x, y: x+', '+y, countries)
print(concatstring, 'are North European countries.')
# - Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the 
# [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) in this repository as countries.js
# (eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(lst):
    land_in,stan_in = [], []
    for i in lst:
        if 'land' in i:
            land_in.append(i)
        elif 'stan' in i:
            stan_in.append(i)
    return land_in, stan_in

import sys
sys.path.insert(1, r'C:\Users\david\30DAYSOFPYTHON\datafiles')
import countries as clist

print(categorize_countries(clist.countries))
# - Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number 
# of country names starting with that letter.
def country_dictionary(lst):
    dict = {}
    for i in lst:
        if i[0] in dict:
            dict[i[0]]+=1
        else:
            dict[i[0]]=1
    return dict

print(country_dictionary(clist.countries))
# - Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(lst):
    return lst[:10]

print(get_first_ten_countries(clist.countries))
# - Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(lst):
    return lst[-10:]

print(get_last_ten_countries(clist.countries))
# ### Exercises: Level 3

# 1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file 
# and follow the tasks below:
import countries_data as clist_data

#    - Sort countries by name, by capital, by population
by_name = sorted(clist_data.c_d,key=lambda dct:dct['name'])
by_caps = sorted(clist_data.c_d,key=lambda dct:dct['capital'])
by_pop = sorted(clist_data.c_d,reverse=True,key=lambda dct:dct['population'])

# TODO: Sort out the ten most spoken languages by location.
# TODO: Sort out the ten most populated countries.

# 🎉 CONGRATULATIONS ! 🎉
