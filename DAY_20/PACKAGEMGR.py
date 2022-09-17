
# ## Exercises: Day 20
import collections
import requests
# 1. Read this url and find the 10 most frequent words. 
romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
responses = requests.get(romeo_and_juliet)

def m_f_w(fi, num):
    wordz = fi.split()
    c = collections.Counter(wordz).most_common(num)
    return c

print(m_f_w(responses.text, 10))

# 2. Read the cats API and 
cats_api = 'https://api.thecatapi.com/v1/breeds'
responses = requests.get(cats_api)
#  and find :
#    1. the min, max, mean, median, standard deviation of cats' weight in metric units.
#    2. the min, max, mean, median, standard deviation of cats' lifespan in years.
#    3. Create a frequency table of country and breed of cats
# 3. Read the [countries API](https://restcountries.eu/rest/v2/all) and find
countries_api = 'https://restcountries.eu/rest/v2/all'
#    1. the 10 largest countries
#    2. the 10 most spoken languages
#    3. the total number of languages in the countries API
# 4. UCI is one of the most common places to get data sets for data science and machine learning. 
# Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php).
UCI = 'https://archive.ics.uci.edu/ml/datasets.php'
#  Without additional libraries
# it will be difficult, so you may try it with BeautifulSoup4

# 🎉 CONGRATULATIONS ! 🎉
