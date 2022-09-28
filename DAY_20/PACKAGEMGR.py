
# ## Exercises: Day 20
import collections
import requests
import statistics
import re
import pandas as pd
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
cats = responses.json()
all_cats_metric_weight = []
for a in cats:
    metric_weight = a['weight']['metric']
    minmax_weight = re.findall(r'\d', metric_weight)
    minmax_weight = list(map(int, minmax_weight))
    mean_weight = statistics.mean(minmax_weight)
    all_cats_metric_weight.append(mean_weight)
#  and find :
#    1. the min, max, mean, median, standard deviation of cats' weight in metric units.
print('MIN:', min(all_cats_metric_weight))
print('MAX:', max(all_cats_metric_weight))
print('MEAN:', statistics.mean(all_cats_metric_weight))
print('MEDIAN:', statistics.median(all_cats_metric_weight))
print('STDEV:', statistics.stdev(all_cats_metric_weight))
#    2. the min, max, mean, median, standard deviation of cats' lifespan in years.
all_cats_life_span = []
for a in cats:
    life_span = a['life_span']
    minmax_span = re.findall(r'\d', life_span)
    minmax_span = list(map(int, minmax_span))
    mean_span = statistics.mean(minmax_span)
    all_cats_life_span.append(mean_span)

print('MIN:', min(all_cats_life_span))
print('MAX:', max(all_cats_life_span))
print('MEAN:', statistics.mean(all_cats_life_span))
print('MEDIAN:', statistics.median(all_cats_life_span))
print('STDEV:', statistics.stdev(all_cats_life_span))
#    3. Create a frequency table of country and breed of cats
df = pd.DataFrame(cats, columns=['origin','name'])
print(df)
print(pd.crosstab(index=df['name'], columns=df['origin']))

# 3. Read the [countries API](https://restcountries.eu/rest/v2/all) and find
countries_api = 'https://restcountries.eu/rest/v2/all'
'''
# responses = requests.get(countries_api)
#    1. the 10 largest countries
#    2. the 10 most spoken languages
#    3. the total number of languages in the countries API

TODO: CANT GET THIS SITE TO RESPOND, MAY NEED NEW SOURCE
'''
# 4. UCI is one of the most common places to get data sets for data science and machine learning. 
# Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php).
UCI = 'https://archive.ics.uci.edu/ml/datasets.php'
#  Without additional libraries
# it will be difficult, so you may try it with BeautifulSoup4
from bs4 import BeautifulSoup
responses = requests.get(UCI)
soup = BeautifulSoup(responses.text,"html.parser")

lists = []
zz = soup.find('table',attrs={"border":"1","cellpadding":"5"})
for tag in zz.find_all('tr'):
    for td in tag.find_all('td'):
        lists.append(td.text)

# 🎉 CONGRATULATIONS ! 🎉
