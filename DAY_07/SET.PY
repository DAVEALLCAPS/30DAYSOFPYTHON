### 💻 Exercises: Day 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

### Exercises: Level 1

# 1. Find the length of the set it_companies
print(len(it_companies))
# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['FAKE', 'NOTFAKE', 'ITCOMPANY'])
# 4. Remove one of the companies from the set it_companies
it_companies.pop()
# 5. What is the difference between remove and discard
it_companies.remove('Twitter')
# Remove will throw a KeyError if the item doesn't exist in the set.
it_companies.discard('')
# Discard will not.

### Exercises: Level 2

# 1. Join A and B
print(A.union(B))
# 2. Find A intersection B
print(A.intersection(B))
# 3. Is A subset of B
print(A.issubset(B))
# 4. Are A and B disjoint sets
print(A.isdisjoint(B))
# 5. Join A with B and B with A
print(A.union(B))
print(B.union(A))
# 6. What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# 7. Delete the sets completely
del A
del B

### Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages = set(age)
print('List length:', len(age), 'Set length:', len(ages))
# 2. Explain the difference between the following data types: string, list, tuple and set
string_ = 'SEQUENCE OF UNICODE CHARACTERS'
list_ = ['ORDERED', 555, 1.90, 'MUTABLE']
tuple_ = ('MULTIPLE ITEMS', 'ORDERED', 'UNCHANGEABLE') 
set_ = {'UNORDERED', 'UNCHANGEABLE', 'NO DUPLICATES'}
# 3. _I am a teacher and I love to inspire and teach people._ How many unique words have been used
# in the sentence? Use the split methods and set to get the unique words.
our_string = 'I am a teacher and I love to inspire and teach people.'
our_string = our_string.strip('.').split()
setz = set(our_string)
print('Unique Words:', len(setz))

# 🎉 CONGRATULATIONS ! 🎉