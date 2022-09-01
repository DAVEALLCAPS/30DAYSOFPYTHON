
# ## 💻 Exercises: Day 14

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
        print(i)

print_list_1by1(countries)
# 5. Use for to print each name in the names list.
print_list_1by1(names)
# 6. Use for to print each number in the numbers list.
print_list_1by1(numbers)

# ### Exercises: Level 2

# 1. Use map to create a new list by changing each country to uppercase in the countries list
# 1. Use map to create a new list by changing each number to its square in the numbers list
# 1. Use map to change each name to uppercase in the names list
# 1. Use filter to filter out countries containing 'land'.
# 1. Use filter to filter out countries having exactly six characters.
# 1. Use filter to filter out countries containing six letters and more in the country list.
# 1. Use filter to filter out countries starting with an 'E'
# 1. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# 1. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# 1. Use reduce to sum all the numbers in the numbers list.
# 1. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# 1. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# 1. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# 2. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# 1. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

# ### Exercises: Level 3

# 1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#    - Sort countries by name, by capital, by population
#    - Sort out the ten most spoken languages by location.
#    - Sort out the ten most populated countries.

# 🎉 CONGRATULATIONS ! 🎉
