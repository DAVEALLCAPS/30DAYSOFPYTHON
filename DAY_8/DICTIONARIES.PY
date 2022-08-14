# 💻 Exercises: Day 8
# Create an empty dictionary called dog
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog.update(name=None,color=None,breed=None,legs=None,age=None)
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age,
# marital status, skills, country, city and address as keys for the dictionary
student = {
            'first_name':None,
            'last_name':None,
            'gender':None,
            'age':None,
            'marital':None,
            'skills':['THING','OTHER THING'],
            'country':None,
            'city':None,
            'address':None
}
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(student['skills'])
# Modify the skills values by adding one or two skills
student['skills'].append('NICE')
# Get the dictionary keys as a list
print(student.keys())
# Get the dictionary values as a list
print(list(student))
# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
student.pop('age')
print(student)
# Delete one of the dictionaries
del student
# 🎉 CONGRATULATIONS ! 🎉