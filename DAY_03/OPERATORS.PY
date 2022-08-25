# 💻 Exercises - Day 3

age = 10 # 1. Declare your age as integer variable
height = 6.0 # 2. Declare your height as a float variable
c = (3 + 6j) # 3. Declare a variable that store a complex number

# 4. Write a script that prompts the user to enter base and height of the triangle and 
# calculate an area of this triangle (area = 0.5 x b x h).
base = input('Enter base:') # 20
height = input('Enter height:') # 10
area = 0.5 * int(base) * int(height)
print('The area of the triangle is', int(area)) # 100

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle.
# Calculate the perimeter of the triangle (perimeter = a + b + c).
a = input('Enter side a:') # 5
b = input('Enter side b:') # 4
c = input('Enter side c:') # 3
sides = int(a) + int(b) + int(c)
print('The perimeter of the triangle is', sides) # 12

# 6. Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = int(input('Enter length:'))
width = int(input('Enter width:'))
area = length * width
perimeter = 2 * (length + width)
print('Area:', area)
print('Perimeter:', perimeter)

# 7. Get radius of a circle using prompt. 
# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

myPI = 3.14
radius = int(input('Enter radius:'))
area = myPI * radius * radius
circ = 2 * myPI * radius
print('Area:', area)
print('Circumference:', circ)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# m1 = 2
# x1 = 0
# y2 = 0
# b=y1-m1*x1
# b2=y2-m1*x2
# print('Slope:', m1, 'Y-Intercept: (0,'+b+')', 'X-Intercept: ('+b2+',0)')

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance 
# between point (2, 2) and point (6,10) 

x1 = 2
x2 = 6
y1 = 2
y2 = 10
m2 = (y2-y1)/(x2-x1)
print('Slope:', m2)

# 10. Compare the slopes in tasks 8 and 9.

print('Slope 1: 2', 'Slope 2:', m2)

# 11. Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at what x value y is going to be 0.

x = -3
y = x**2+6*x+9
print(y)

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.

if len('python') != len('dragon'):
    print('Different.')
else:
    print('Same length.')

# 13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'

if 'on' in 'python' and 'on' in 'dragon':
    print('BOTH')
else:
    print('NOPE')

# 14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.

sentence = "I hope this course is not full of jargon"
if 'jargon' in sentence:
    print('Jargon found.')
else:
    print('No jargon here.')

# 15. There is no 'on' in both dragon and python

if 'on' not in 'dragon' and 'on' not in 'python':
    print('NOT IN')
else:
    print('IN')

# 16. Find the length of the text _python_ and convert the value to float and convert it to string

txt = 'python'
leng = len(txt)
leng = float(leng)
print(str(leng))

# 17. Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?

num = 44
if (num % 2) == 0:
    print('EVEN')
else:
    print('ODD')

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

k = int(2.7)
flo = 7 // 3
print(k == flo)

# 19. Check if type of '10' is equal to type of 10

print(type('10') == type(10))

# 20. Check if int('9.8') is equal to 10

print(int(9.8) == 10)

# 21. Write a script that prompts the user to enter hours and rate per hour. 
# Calculate pay of the person?

hours = float(input('Enter hours:'))
rate = float(input('Enter rate per hour:'))
pay = hours * rate
print('Your weekly earning is:', pay)

# 22. Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. 
# Assume a person can live hundred years

years = int(input('Enter number of years you have lived:'))
secYears = 31536000 * years
print('You have lived for', secYears, 'seconds.')

# 23. Write a Python script that displays the following table

for num in range(1,6):
    x = 1
    print(num, x, num**x, num**(x+1), num**(x+2))

"""
```py
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
```

🎉 CONGRATULATIONS ! 🎉"""