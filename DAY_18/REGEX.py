# ## 💻 Exercises: Day 18

# ### Exercises: Level 1
import collections
import re

#  1. What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
all_words_re = r'(\w+)'
all_words = re.findall(all_words_re, paragraph, re.IGNORECASE)
print(collections.Counter(all_words).most_common())

# 2. Extract these numbers from this whole text and find the distance between the two furthest particles.
whole_text = '''The position of some particles on the horizontal x-axis are -1, 2, -4, -3 and -1 in the negative direction, 
0 at origin, 4 and 8 in the positive direction.'''
all_digis_re = r'(-?\d)'
whole_digis = re.findall(all_digis_re, whole_text)
print('points =', whole_digis)
whole_digis_ints = [int(i) for i in whole_digis]
whole_digis_ints.sort()
print('sorted points =', whole_digis_ints)
distance_digis = whole_digis_ints[-1] - whole_digis_ints[0]
print(f'distance = {whole_digis_ints[-1]} - ({whole_digis_ints[0]}) = {distance_digis}')

# ### Exercises: Level 2

# 1. Write a pattern which identifies if a string is a valid python variable
regex_python_var = '^[A-Za-z_][A-Za-z0-9_]*'

def is_valid_variable(word):
    if re.search(regex_python_var,word):
        return True
    else:
        return False

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True


# ### Exercises: Level 3

# 1. Clean the following text. After cleaning, count three most frequent words in the string.

#     ```py
#     sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

#     print(clean_text(sentence));
#     I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
#     print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
#     ```

# 🎉 CONGRATULATIONS ! 🎉
