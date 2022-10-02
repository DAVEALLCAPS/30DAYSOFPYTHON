# Exercises: Day 25
import pandas as pd
import numpy as np
# Read the hacker_news.csv file from data directory
df = pd.read_csv('../datafiles/hacker_news.csv')
# Get the first five rows
print(df.head())
# Get the last five rows
print(df.tail())
# Get the title column as pandas series
titles = df['title']
print(titles)
# Count the number of rows and columns
print(df.shape)
# Filter the titles which contain python
print(df[df.title.str.contains('python')])
# Filter the titles which contain JavaScript
print(df[df.title.str.contains('JavaScript')])
# Explore the data and make sense of it
print(df.describe())
# 🎉 CONGRATULATIONS ! 🎉
