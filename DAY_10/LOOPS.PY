# ## 💻 Exercises: Day 10

# ### Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(11):
    print(number,end=" ")

i = 0
print()

while i < 11:
    print(i,end=" ")
    i += 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
print()
for number in range(10,-1,-1):
    print(number,end=" ")

i = 10
print()
while i > -1:
    print(i,end=" ")
    i -= 1
# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

print()
symb = '#'
i = 1
while i < 8:
    print(symb * i)
    i += 1

# 4. Use nested loops to create the following:

print()
for x in range(8):
    for y in range(8):
        print(symb, end=" ")
    print()

#    ```sh
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    ```

# 5. Print the following pattern:

print()
for number in range(11):
    print("{} x {} = ".format(number, number), number * number)
#    ```sh
#    0 x 0 = 0
#    1 x 1 = 1
#    2 x 2 = 4
#    3 x 3 = 9
#    4 x 4 = 16
#    5 x 5 = 25
#    6 x 6 = 36
#    7 x 7 = 49
#    8 x 8 = 64
#    9 x 9 = 81
#    10 x 10 = 100
#    ```

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using 
# a for loop and print out the items.
my_list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for number in my_list:
    print(number)
# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for number in range(101):
    if number % 2 == 0:
        print(number)
# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for number in range(101):
    if number % 2 != 0:
        print(number)
# ### Exercises: Level 2
    
# 1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#    The sum of all numbers is 5050.
total_sum = 0
for number in range(101):
    total_sum += number
print(f'The sum of all numbers is {total_sum}.')

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
#     The sum of all evens is 2550. And the sum of all odds is 2500.

all_odds = 0
all_evens = 0
for number in range(101):
    if number % 2 != 0:
        all_odds += number
    elif number % 2 == 0:
        all_evens += number
print(f'The sum of all evens is {all_evens}. And the sum of all odds is {all_odds}.')

# ### Exercises: Level 3

# 1. Go to the data folder and use the [COUNTRIES.PY] file. 
# Loop through the countries and extract all the countries containing the word _land_.
import sys
sys.path.insert(1, r'C:\Users\david\30DAYSOFPYTHON\datafiles')
import countries as clist

our_word = 'land'
land_list = list()
for i in clist.countries:
    if our_word in i:
        land_list.append(i)
print(land_list)

# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_list = ['banana', 'orange', 'mango', 'lemon']
rev_list = list()
for i in reversed(fruit_list):
    rev_list.append(i)
print(rev_list)

print()

# 3. Go to the data folder and use the [countries_data.py]file.
import countries_data as cntrdata
langs = []
cntnames = []
cntpops = []

for i in cntrdata.c_d:
    langs.extend(i['languages'])
    cntnames.append(i['name'])
    cntpops.append(i['population'])

from collections import Counter
c = Counter(langs)

#    1. What are the total number of languages in the data
print(len(c))
#    2. Find the ten most spoken languages from the data
print(c.most_common(10))
#    3. Find the 10 most populated countries in the world
cntpops2 = sorted(cntpops)
cntpops2 = cntpops2[-10:]
for i in cntpops2:
    indy = cntpops.index(i)
    print(cntnames[indy], end=", ")

# 🎉 CONGRATULATIONS ! 🎉
