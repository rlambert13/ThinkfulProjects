import matplotlib.pyplot as plt 
import pandas as pd 
import scipy.stats as stats
import collections

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

# Remove rows with null values
loansData.dropna(inplace=True)

loansData['Open.CREDIT.Lines'] = loansData['Open.CREDIT.Lines'].astype(int)
# Gets counts of observations for each number of credit lines 
freq = collections.Counter(loansData['Open.CREDIT.Lines'])

# print(freq)
# print(type(loansData['Open.CREDIT.Lines']))


# Plots a bar chart to show frequency of number of lines
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

# chisquared function doesn't work on a dictionary object
# so you instead need to convert it to a list
chi, p = stats.chisquare(list(freq.values()))

print('Chi and p: {0}, {1}'.format(chi, p))
