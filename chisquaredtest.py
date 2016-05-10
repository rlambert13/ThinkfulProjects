import matplotlib.pyplot as plt 
import pandas as pd 
import scipy.stats as stats
import collections

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

# Remove rows with null values
loansData.dropna(inplace=True)

# Gets counts of observations for each number of credit lines 
freq = collections.Counter(loansData['Open.CREDIT.Lines'])

# Plots a bar chart to show frequency of number of lines
# plt.figure()
# plt.bar(freq.keys(), freq.values(), width=1)
# plt.show()

chi, p = stats.chisquare(freq.values())

# print(chi, p)
