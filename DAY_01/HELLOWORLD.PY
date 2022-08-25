# Exercise: Level 1
# 1. Check the python version you are using

from platform import python_version

print("Python Version:", python_version())

# 2. Open the python interactive shell and do the following operations. The operands are 3 and 4.

print("3 + 4 =", 3 + 4) # addition(+)
print("3 - 4 =", 3 - 4) # subtraction(-)
print("3 * 4 =", 3 * 4) # multiplication(*)
print("3 % 4 =", 3 % 4) # modulus(%)
print("3 / 4 =", 3 / 4) # division(/)
print("3 ** 4 =", 3 ** 4) # exponential(**)
print("3 // 4 =", 3 // 4) # floor division operator(//)

# 3. Write strings on the python interactive shell. The strings are the following:

print("DAVE") # Your name
print("CAPS LOCK") # Your family name
print("USA") # Your country
print("I AM ENJOYING 30 DAYS OF PYTHON") # I am enjoying 30 days of python

# 4. Check the data types of the following data:

print(type(10)) # 10
print(type(9.8)) # 9.8
print(type(3.14)) # 3.14
print(type(4 - 4j)) # 4 - 4j
print(type(['Asabeneh', 'Python', 'Finland'])) # ['Asabeneh', 'Python', 'Finland']
print(type("DAVE")) # Your name
print(type("CAPS LOCK")) # Your family name
print(type("USA")) # Your country

# Exercise: Level 2

"""
Create a folder named day_1 inside 30DaysOfPython folder.
Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4.
Remember to use print() when you are working on a python file.
Navigate to the directory where you have saved your file, and run it.
"""

# Exercise: Level 3
# Write an example for different Python data types
# such as Number(Integer, Float, Complex), String, 
# Boolean, List, Tuple, Set and Dictionary.

print(type(1337)) # Integer
print(type(13.37)) # Float
print(type(13 - 37j)) # Complex
print(type('1337')) # String 
print(type(False)) # Boolean
print(type([1, 3, 3, 7])) # List
print(type(((1,3),(3,7)))) # Tuple
print(type({1, 3, 7})) # Set
print(type({'dict': 1337})) # Dictionary

# Find an Euclidian distance between (2, 3) and (10, 8)

from math import sqrt

x1 = 2
x2 = 10
y1 = 3
y2 = 8

print(sqrt((x2 - x1)**2 + (y2 - y1)**2))

# 🎉 CONGRATULATIONS ! 🎉
