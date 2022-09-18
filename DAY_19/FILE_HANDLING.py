
# ## 💻 Exercises: Day 19

# ### Exercises: Level 1

# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
def num_lines_words(file_name):
    f = open(file_name,"rt")
    data = f.read()
    words = data.split()
    linez = data.split('\n')
    return f'Lines: {len(linez)} and Words: {len(words)}'

#    a) Read obama_speech.txt file and count number of lines and words
print(num_lines_words('../datafiles/obama_speech.txt'))
#    b) Read michelle_obama_speech.txt file and count number of lines and words
print(num_lines_words('../datafiles/michelle_obama_speech.txt'))
#    c) Read donald_speech.txt file and count number of lines and words
print(num_lines_words('../datafiles/donald_speech.txt'))
#    d) Read melina_trump_speech.txt file and count number of lines and words
print(num_lines_words('../datafiles/melina_trump_speech.txt'))

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json
import collections

with open('../datafiles/countries_data.json', 'r', encoding='utf-8') as jz:
    jz_dict = json.loads(jz.read())

def most_spoken_languages(fi, num):
    all_langs = []
    for i in fi:
        all_langs.extend(i['languages'])
    c = collections.Counter(all_langs).most_common(num)
    return c

print(most_spoken_languages(jz_dict, 10))
print(most_spoken_languages(jz_dict, 3))

# 3. Read the countries_data.json data file in data directory, create a function that creates a 
# list of the ten most populated countries
from operator import itemgetter

def m_p_c(fi,num):
    newlist = sorted(fi, key=itemgetter('population'), reverse=True)
    newlist = newlist[:int(num)]
    return newlist

print(m_p_c(jz_dict,10))
print(m_p_c(jz_dict,3))

# ### Exercises: Level 2

# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re
# email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
# rgx = '[a-z0-9._%+-]+@[a-z0-9-]+\.[a-z0-9-]+'
def extract_emails(file_name):
    with open(file_name, 'r') as f:
        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", f.read())
    return set(emails), len(set(emails))

print(extract_emails('../datafiles/email_exchanges_big.txt'))
# 5. Find the most common words in the English language. Call the name of your function find_most_common_words, 
# it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your 
# function will return an array of tuples in descending order. Check the output

def find_most_common_words(fi,num):
    pass
# ```py
#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 10))
#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and'),
#     (4, 'a'),
#     (4, 'in'),
#     (3, 'that'),
#     (2, 'have'),
#     (2, 'I')]

#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 5))

#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and')]
# ```

# 6. Use the function, find_most_frequent_words to find:
#    a) The ten most frequent words used in [Obama's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)
#    b) The ten most frequent words used in [Michelle's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
#    c) The ten most frequent words used in [Trump's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)
#    d) The ten most frequent words used in [Melina's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)
# 7. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of [Michelle's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt) and [Melina's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt) speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of [stop words](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/stop_words.py) are in the data directory
# 8. Find the 10 most repeated words in the romeo_and_juliet.txt
# 9. Read the [hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) file and find out:
#    a) Count the number of lines containing python or Python
#    b) Count the number lines containing JavaScript, javascript or Javascript
#    c) Count the number lines containing Java and not JavaScript

# ### Exercises: Level 3

# 🎉 CONGRATULATIONS ! 🎉
