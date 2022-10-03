
# ## 💻 Exercises: Day 21

# ### Exercises: Level 1

# 1. Python has the module called _statistics_ and we can use this module to do all the statistical calculations. 
# However, to learn how to make function and reuse function let us try to develop a program, which calculates the 
# measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation).
# In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. 
# You can create a class called Statistics and create all the functions that do statistical calculations as 
# methods for the Statistics class. Check the output below.
from collections import Counter


class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)
        
    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return max(self.data) - min(self.data)
    
    def mean(self):
        return sum(self.data) / len(self.data)
    
    def median(self):
        data = sorted(self.data)
        n = len(data)
        if n == 0:
            pass
        if n % 2 == 1:
            return data[n // 2]
        else:
            i = n // 2
            return (data[i - 1] + data[i]) / 2
    
    def mode(self):
        pairs = Counter(iter(self.data)).most_common(1)
        try:
            return pairs[0][0]
        except IndexError:
            raise ValueError('no mode for empty data') from None


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
p = Statistics(ages)
print(p.data)
print('Count: ', p.count())
print('Sum: ',p.sum())
print('Min: ',p.min())
print('Max: ',p.max())
print('Range: ',p.range())
print('Mean: ',p.mean())
print('Median: ',p.median())
print('Mode: ',p.mode())
print('STD : ',)
print('Variance: ',)
print('Freq. Dist.: ',)

# print('Count:', data.count()) # 25
# print('Sum: ', data.sum()) # 744
# print('Min: ', data.min()) # 24
# print('Max: ', data.max()) # 38
# print('Range: ', data.range() # 14
# print('Mean: ', data.mean()) # 30
# print('Median: ', data.median()) # 29
# print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
# print('Standard Deviation: ', data.std()) # 4.2
# print('Variance: ', data.var()) # 17.5
# print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
# ```

# ```sh
# # you output should look like this
# print(data.describe())
# Count: 25
# Sum:  744
# Min:  24
# Max:  38
# Range:  14
# Mean:  30
# Median:  29
# Mode:  (26, 5)
# Variance:  17.5
# Standard Deviation:  4.2
# Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
# ```

# ### Exercises: Level 2

# 1. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it 
# has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. 
# Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname, lastname, income, expense):
        self.firstname = firstname
        self.lastname = lastname
        self.income = income
        self.expense = expense

    def total_income(self):
        return self.income

    def total_expense(self):
        return self.expense

    def account_info(self):
        return f'The name of the person is {self.firstname} {self.lastname}. Total expenses is {self.expense} and the total income is {self.income}. Account balance is {self.income - self.expense}.  '  

    def add_income(self):
        new_income = int(input("Enter the amount of income: "))
        self.income =  self.income + new_income
        return self.income 

    def add_expense(self):
        new_expense = int(input("Enter the amount of expense: "))
        self.expense = self.expense + new_expense
        return self.expense    

    def acc_bal(self):
        return self.income - self.expense

fname = input("Enter the first name: ")
lname = input("Enter the last name: ")
inc = int(input("Enter the income: "))
exp = int(input("Enter the expenses: "))

PA1 = PersonAccount(fname, lname, inc, exp)
print(PA1.firstname)        
print(PA1.lastname)        
print(PA1.income)        
print(PA1.expense) 
print((PA1.total_expense()))       
print((PA1.total_income()))       
print((PA1.acc_bal()))       
print((PA1.add_expense()))       
print((PA1.add_income()))       
print((PA1.account_info())) 
# ### Exercises: Level 3


# 🎉 CONGRATULATIONS ! 🎉
