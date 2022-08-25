# Exercises: Level 1
# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# Write a python comment saying 'Day 2: 30 Days of python programming'

# Day 2: 30 Days of python programming

FIRST_NAME = "DAVE" # Declare a first name variable and assign a value to it
LAST_NAME = "ALLCAPS" # Declare a last name variable and assign a value to it
FULL_NAME = FIRST_NAME + LAST_NAME # Declare a full name variable and assign a value to it
COUNTRY = "USA" # Declare a country variable and assign a value to it
CITY = "NOTFAKE CITY" # Declare a city variable and assign a value to it
AGE = 1337 # Declare an age variable and assign a value to it
YEAR = 1999 # Declare a year variable and assign a value to it
IS_MARRIED = True # Declare a variable is_married and assign a value to it
IS_TRUE = True # Declare a variable is_true and assign a value to it
IS_LIGHT_ON = False # Declare a variable is_light_on and assign a value to it
VAR1, VAR2, VAR3 = 1337, "DAVE", True # Declare multiple variable on one line

# Exercises: Level 2
print(type(FIRST_NAME)) # Check the data type of all your variables using type() built-in function
print(type(LAST_NAME))
print(type(FULL_NAME))
print(type(COUNTRY))
print(type(CITY))
print(type(AGE))
print(type(YEAR))
print(type(IS_MARRIED))
print(type(IS_TRUE))
print(type(IS_LIGHT_ON))
print(type(VAR1))
print(type(VAR2))
print(type(VAR3))

print("FIRST NAME LENGTH:", len(FIRST_NAME)) # Using the len() built-in function, find the length of your first name
print("FIRST NAME LENGTH:", len(FIRST_NAME), "LAST NAME LENGTH:", len(LAST_NAME)) # Compare the length of your first name and your last name
NUM_ONE, NUM_TWO = 5, 4 # Declare 5 as num_one and 4 as num_two
TOTAL = NUM_ONE + NUM_TWO # Add num_one and num_two and assign the value to a variable total
DIFF = NUM_ONE - NUM_TWO # Subtract num_two from num_one and assign the value to a variable diff
PRODUCT = NUM_ONE * NUM_TWO # Multiply num_two and num_one and assign the value to a variable product
DIVISION = NUM_ONE / NUM_TWO # Divide num_one by num_two and assign the value to a variable division
REMAINDR = NUM_TWO % NUM_ONE # Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
EXP = NUM_ONE ** NUM_TWO # Calculate num_one to the power of num_two and assign the value to a variable exp
FLOOR_DIVISION = NUM_ONE // NUM_TWO # Find floor division of num_one by num_two and assign the value to a variable floor_division

PI = 3.14
RADIUS = 30 # The radius of a circle is 30 meters.
AREA_OF_CIRCLE = PI * RADIUS * RADIUS # Calculate the area of a circle and assign the value to a variable name of area_of_circle
CIRCUM_OF_CIRCLE = 2 * PI * RADIUS # Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

USER_RADIUS = input(int()) # Take radius as user input and calculate the area.
USER_AREA = PI * USER_RADIUS * USER_RADIUS

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
USER_FIRST = input()
USER_LAST = input()
USER_COUNTRY = input()
USER_AGE = input(int())

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
# 🎉 CONGRATULATIONS ! 🎉
