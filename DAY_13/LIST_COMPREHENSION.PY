
# ## 💻 Exercises: Day 13

# 1. Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers2 = [i for i in numbers if i <= 0]
print(numbers2)

# 2. Flatten the following list of lists of lists to a one dimensional list :

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for sub_list in list_of_lists for item in sub_list]
print(flattened_list)
#    output
#    [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Using list comprehension create the following list of tuples:
c = 1
numberz = [(i,c,i*c,i**2,i**3,i**4,i**5) for i in range(0,11)]
print(numberz)

#    [(0, 1, 0, 0, 0, 0, 0),
#    (1, 1, 1, 1, 1, 1, 1),
#    (2, 1, 2, 4, 8, 16, 32),
#    (3, 1, 3, 9, 27, 81, 243),
#    (4, 1, 4, 16, 64, 256, 1024),
#    (5, 1, 5, 25, 125, 625, 3125),
#    (6, 1, 6, 36, 216, 1296, 7776),
#    (7, 1, 7, 49, 343, 2401, 16807),
#    (8, 1, 8, 64, 512, 4096, 32768),
#    (9, 1, 9, 81, 729, 6561, 59049),
#    (10, 1, 10, 100, 1000, 10000, 100000)]

# 4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#    output:
#    [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
new_countries = [numbz for row in countries for numbz in row]
new_countries2 = [numbz.upper() for row in new_countries for numbz in row]
print(new_countries2)
# 5. Change the following list to a list of dictionaries:
new_countries3 = [numbz for row in new_countries for numbz in row]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
keys = ['country','city']
#    output:
#    [{'country': 'FINLAND', 'city': 'HELSINKI'},
#    {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#    {'country': 'NORWAY', 'city': 'OSLO'}]
n = len(new_countries3)
new_dict = [{keys[0]: new_countries3[idx], keys[1]: new_countries3[idx+1]} for idx in range(0,n,2)]
print(new_dict)
# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#    output
#    ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
concatnames = [" ".join(map(str,names2[i])) for i in range(0,len(names2))]
# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
calculate_slope = lambda c : c.split()[2].rstrip('x')

print(calculate_slope("y = 25x + 4"))

# 🎉 CONGRATULATIONS ! 🎉
