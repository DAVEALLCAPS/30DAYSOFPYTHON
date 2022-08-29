
## 💻 Exercises: Day 12

### Exercises: Level 1
import secrets
import string
# 1. Write a function which generates a six digit/character random_user_id.
def random_user_id():
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))

print(random_user_id())
# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters 
# but it takes two inputs using input(). One of the inputs is the number of characters and the second input 
# is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    N = int(input("Chars: "))
    C = int(input("IDs: "))
    for i in range(C):
        print(''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(N)))

user_id_gen_by_user()
# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = secrets.randbelow(256)
    g = secrets.randbelow(256)
    b = secrets.randbelow(256)
    return r,g,b
print(rgb_color_gen())

# # rgb(125,244,255) - the output should be in this form

# ### Exercises: Level 2

# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an 
# array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 
# 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(num):
    chars = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']
    hexa_list = []
    for i in range(num):
        hexa = '#' + ''.join(secrets.choice(chars) for _ in range(6))
        hexa_list.append(hexa)
    return hexa_list

print(list_of_hexa_colors(5))
# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num):
    rgb_list = []
    for i in range(num):
        r = secrets.randbelow(256)
        g = secrets.randbelow(256)
        b = secrets.randbelow(256)
        rgbs = f'rgb({r},{g},{b})'
        rgb_list.append(rgbs)
    return rgb_list

print(list_of_rgb_colors(5))
# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_type, number_colors):
    if color_type == 'hexa':
        print(list_of_hexa_colors(number_colors))
    elif color_type == 'rgb':
        print(list_of_rgb_colors(number_colors))

generate_colors('hexa', 3)
generate_colors('rgb', 8)
# ```py
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
#    ```

# ### Exercises: Level 3
import random
# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(a_list):
    return random.shuffle(a_list)

the_list = ['0','1','2','3','4']
shuffle_list(the_list)
print(the_list)
# 2. Write a function which returns an array of seven random numbers in a range of 0-9. 
# All the numbers must be unique.
def seven_randos():
    numbos = []
    for i in range(0,10):
        numbos.append(i)
    shuffle_list(numbos)
    return numbos[0:7]

print(seven_randos())
print(seven_randos())

# 🎉 CONGRATULATIONS ! 🎉
