## 💻 Exercises: Day 6

### Exercises: Level 1

# 1. Create an empty tuple
empty_tuple = ()
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers_tuple = ('FAKE1', 'NOTFAKE1')
sisters_tuple = ('FAKE2', 'NOTFAKE2')
# 3. Join brothers and sisters tuples and assign it to siblings
siblings_tuple = brothers_tuple + sisters_tuple
# 4. How many siblings do you have?
print('Siblings:', len(siblings_tuple))
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings_tuple + ('MOTHER', 'FATHER')
print('Family Members Tuple:', family_members)

### Exercises: Level 2

# 1. Unpack siblings and parents from family_members
siblings = family_members[0:3]
parents = family_members[4:]
print('Siblings: ', siblings)
print('Parents: ', parents)
# 2. Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple', 'Orange', 'Banana')
vegetables = ('Onion', 'Squash')
animalproducts = ('Beef', 'Chicken')
food_stuff_tp = fruits + vegetables + animalproducts
# 3. Change the about food_stuff_tp  tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid = len(food_stuff_lt) // 2
print(food_stuff_lt[mid])
# 5. Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])
# 6. Delete the food_staff_tp tuple completely
print(food_stuff_tp)
del food_stuff_tp
# 7. Check if an item exists in  tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# - Check if 'Estonia' is a nordic country
# - Check if 'Iceland' is a nordic country
est = 'Estonia' in nordic_countries
ice = 'Iceland' in nordic_countries
print('Estonia: ', est)
print('Iceland: ', ice)
