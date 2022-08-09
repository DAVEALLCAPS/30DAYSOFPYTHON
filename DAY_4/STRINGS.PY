# 💻 Exercises - Day 4

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
spc = ' '
w1 = 'Thirty'
w2 = 'Days'
w3 = 'Of'
w4 = 'Python'
singleString = w1 + spc + w2 + spc + w3 + spc + w4
print(singleString)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
cfa = 'Coding' + spc + 'For' + spc + 'All'
print(cfa)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

# 4. Print the variable company using _print()_.

print(company)

# 5. Print the length of the company string using _len()_ method and _print()_.

print(len(company))

# 6. Change all the characters to uppercase letters using _upper()_ method.

print(company.upper())

# 7. Change all the characters to lowercase letters using _lower()_ method.

print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.

print(company.capitalize(), company.title(), company.swapcase())

# 9. Cut(slice) out the first word of _Coding For All_ string.

print(company[0:6])

# 10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.

cut = company.split()
print(cut.index("Coding"))

# 11. Replace the word coding in the string 'Coding For All' to Python.

cut[0] = 'Python'
print(cut)

# 12. Change Python for Everyone to Python for All using the replace method or other methods.

company2 = company.replace("Coding", "Python")
company2 = company2.replace("Everyone", "All")
print(company2)

# 13. Split the string 'Coding For All' using space as the separator (split()) .

print(company.split())

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

k = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(k.split(','))

# 15. What is the character at index 0 in the string _Coding For All_.

print(company[0])

# 16. What is the last index of the string _Coding For All_.

print(company[-1])

# 17. What character is at index 10 in "Coding For All" string.

print(company[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.

pfe = 'Python For Everyone'
pfe = pfe.split()
for a in pfe:
    print(a[0], end='')

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.

print()
pfe2 = company.split()
for a in pfe2:
    print(a[0], end='')

# 20. Use index to determine the position of the first occurrence of C in Coding For All.

print()
print(company.index('C'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.

print(company.index('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
cfa2 = 'Coding For All People'
print(cfa2.rfind('l'))

# 23. Use index or find to find the position of the first occurrence of the word 'because'
# in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sntc = 'You cannot end a sentence with because because because is a conjunction'
print(sntc.index('because'))

#24. Use rindex to find the position of the last occurrence of the word because in the
# following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(sntc.rindex('because'))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end 
# a sentence with because because because is a conjunction'

sntc = 'You cannot end a sentence with because because because is a conjunction'
sntc2 = sntc[:31] + sntc[55:]
print(sntc2)

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'

print(sntc.index('because'))

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end 
# a sentence with because because because is a conjunction'

print(sntc.replace('because because because ', ''))

# 28. Does '\'Coding For All' start with a substring _Coding_?

print(company.startswith('Coding'))

# 29. Does 'Coding For All' end with a substring _coding_?

print(company.endswith('Coding'))

# 30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right 
# trailing spaces in the given string.

sntc = '    Coding For All      '
print(sntc.strip())

# 31. Which one of the following variables return True when we use the method isidentifier():

chal1, chal2 = '30DaysOfPython', 'thirty_days_of_python'
print(chal1.isidentifier())
print(chal2.isidentifier())

# 32. The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

lst = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
lst2 = '# '.join(lst)
print(lst2)

# 33. Use the new line escape sequence to separate the following sentences.

sntc = 'I am enjoying this challenge.\nI just wonder what is next.'
print(sntc)

# 34. Use a tab escape sequence to write the following lines.

sntc = '\tName\t\tAge\tCountry\t\tCity\n\tAsabeneh\t250\tFinland\t\tHelsinki'
print(sntc)

# 35. Use the string formatting method to display the following:

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')

# 36. Make the following using string formatting methods:

a = 8
b = 6
print(f'{a} + {b} = 14')
print(f'{a} - {b} = 2')
print(f'{a} * {b} = 48')
print(f'{a} / {b} = 1.33')
print(f'{a} % {b} = 2')
print(f'{a} // {b} = 1')
print(f'{a} ** {b} = 262144')

# 🎉 CONGRATULATIONS ! 🎉
