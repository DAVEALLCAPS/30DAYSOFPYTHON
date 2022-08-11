## 💻 Exercises: Day 5

### Exercises: Level 1

# 1. Declare an empty list
emp = []
# 2. Declare a list with more than 5 items
six = [0,1,2,3,4,5,6]
# 3. Find the length of your list
print(len(six))
# 4. Get the first item, the middle item and the last item of the list
print(six[0],six[len(six)//2],six[-1])
# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['DAVE', 10, 6.0, 'OK', 'STREET']
# 6. Declare a list variable named it_companies and assign initial values
# Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# 7. Print the list using _print()_
print(it_companies)
# 8. Print the number of companies in the list
print(len(it_companies))
# 9. Print the first, middle and last company
print(it_companies[0],it_companies[len(it_companies)//2],it_companies[-1])
# 10. Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)
# 11. Add an IT company to it_companies
it_companies.append('DAVEALLCAPS')
print(it_companies)
# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'MIDDLE')
print(it_companies)
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
a = it_companies.index('Apple')
it_companies[a] = it_companies[a].upper()
print(it_companies)
# 14. Join the it_companies with a string '#; '
'#; '.join(it_companies)
# 15. Check if a certain company exists in the it_companies list.
exist = 'DAVE' in it_companies
print(exist)
exist2 = 'DAVEALLCAPS' in it_companies
print(exist2)
# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)
# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
# 18. Slice out the first 3 companies from the list
print(it_companies[:3])
# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])
# 20. Slice out the middle IT company or companies from the list
middle = len(it_companies)//2
print(it_companies[middle])
# 21. Remove the first IT company from the list
it_companies.pop(0)
# 22. Remove the middle IT company or companies from the list
middle = len(it_companies)//2
it_companies.pop(middle)
# 23. Remove the last IT company from the list
it_companies.pop()
# 24. Remove all IT companies from the list
it_companies.clear()
# 25. Destroy the IT companies list
del it_companies
# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
# 27. After joining the lists in question 26. Copy the joined list and assign
# it to a variable full_stack. Then insert Python and SQL after Redux.
b = full_stack.index('Redux')
full_stack.insert(b + 1,'Python')
full_stack.insert(b + 2,'SQL')
print(full_stack)

### Exercises: Level 2

# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# - Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
# - Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
# - Find the median age (one middle item or two middle items divided by two)
middle = len(ages)//2
medianage = ages[middle + 1] + ages[middle + 2]
medianage /= 2
print('Median Age:', medianage)
# - Find the average age (sum of all items divided by their number)
total = 0
for i in ages:
    total = total + i
average = total/len(ages)
print('Average Age:', average)
# - Find the range of the ages (max minus min)
rnges = max_age - min_age
print('Age Range:', rnges)
# - Compare the value of (min - average) and (max - average), use _abs()_ method
a = abs(min_age - average)
b = abs(max_age - average)
print('Min-Average=', a, 'Max-Average=', b)

########################################
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
# 1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
middle = len(countries)//2
print(countries[middle])
# 2. Divide the countries list into two equal lists if 
# it is even if not one more country for the first half.
countries1 = countries[:middle]
countries2 = countries[middle:]
countries1.append('DAVEALLCAPS')
print(len(countries1), len(countries2))
# 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].
# Unpack the first three countries and the rest as scandic countries.
newlst = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_one, second_one, third_one, *scandic = newlst
print(first_one)
print(second_one)
print(third_one)
print(*scandic)
# 🎉 CONGRATULATIONS ! 🎉
