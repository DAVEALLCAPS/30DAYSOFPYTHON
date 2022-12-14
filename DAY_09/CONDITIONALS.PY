# ## 💻 Exercises: Day 9

# ### Exercises: Level 1

# 1.  Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback:
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
user_age = int(input("Enter your age: "))
legal_age = 18
if user_age >= legal_age:
    print('You are old enough to drive.')
else:
    age_diff = legal_age - user_age
    print(f"You need {age_diff} more years to learn to drive.")

# 2.  Compare the values of my_age and your_age using if … else. Who is older (me or you)?
# Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to
# print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom
# text if my_age = your_age. Output:

my_age = 10
if user_age == my_age:
    print('We are the same age!')
elif user_age > my_age:
    age_diff = user_age - my_age
    if age_diff == 1:
        print(f"You are {age_diff} year older than me!")
    else:
        print(f"You are {age_diff} years older than me!")
elif user_age < my_age:
    age_diff = my_age - user_age
    if age_diff == 1:
        print(f"I am {age_diff} year older than you!")
    else:
        print(f"I am {age_diff} years older than you!")

# 3.  Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
#  if a is less b return a is smaller than b, else a is equal to b. Output:

num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))

if num1 > num2:
    print(f"{num1} > {num2}")
elif num1 < num2:
    print(f"{num1} < {num2}")
else:
    print(f"{num1} = {num2}")

#     ### Exercises: Level 2

#    1. Write a code which gives grade to students according to theirs scores:

student = input("Enter student name: ")
grade = int(input("Enter student grade [0-100]: "))

if grade <= 59:
    print(f"{student} got an F.")
elif grade <= 69:
    print(f"{student} got a D.")
elif grade <= 79:
    print(f"{student} got a C.")
elif grade <= 89:
    print(f"{student} got a B.")
elif grade <= 100:
    print(f"{student} got an A.")

# 1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
#     September, October or November, the season is Autumn.
#     December, January or February, the season is Winter.
#     March, April or May, the season is Spring
#     June, July or August, the season is Summer

seasons = {
    'Autumn': ['September', 'October', 'November'],
    'Winter': ['December', 'January', 'February'],
    'Spring': ['March', 'April', 'May'],
    'Summer': ['June', 'July', 'August'],
}

month = input("What month is it: ")

if month in seasons['Autumn']:
    print('The season is Autumn.')
elif month in seasons['Spring']:
    print('The season is Spring.')
elif month in seasons['Winter']:
    print('The season is Winter.')
elif month in seasons['Summer']:
    print('The season is Summer.')

# 2.  The following list contains some fruits:
#     If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
#     If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_input = input("Enter a fruit: ")

if fruit_input in fruits:
    print('That fruit already exists in the list!')
    print(fruits)
else:
    fruits.append(fruit_input)
    print(fruits)

#     ### Exercises: Level 3

#    1. Here we have a person dictionary. Feel free to modify it!

    person = {
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_married': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }

# Check if the person dictionary has skills key,
# if so print out the middle skill in the skills list.
if 'skills' in person.keys():
    print(person['skills'][len(person['skills']) // 2])
# Check if the person dictionary has skills key,
# if so check if the person has 'Python' skill and print out the result.
if 'Python' in person.get('skills'):
    print("Python Skills: True")
else:
    print("Python Skills: False")
# If a person skills has only JavaScript and React,
# print('He is a front end developer'), if the person skills has
if person.get('skills') == ['JavaScript', 'React']:
    print('He is a front end developer')
elif person.get('skills') == ['Node', 'Python', 'MongoDB']:
    print('He is a backend developer')
# Node, Python, MongoDB, print('He is a backend developer'), if the person skills has
# React, Node and MongoDB, Print('He is a fullstack developer'),
elif person.get('skills') == ['React', 'Node', 'MongoDB']:
    print('He is a fullstack developer')
# else print('unknown title') - for more accurate results more conditions can be nested!
else:
    print('Unknown title')
# If the person is married and if he lives in Finland, print the
# information in the following format: Asabeneh Yetayeh lives in Finland. He is married.

if person['is_married'] == True and person['country'] == 'Finland':
    print('{} {} lives in {}. He is married.'.format(person.get('first_name'), person.get('last_name'), person.get('country')))

# 🎉 CONGRATULATIONS ! 🎉
