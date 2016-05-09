import pandas as pd 
import matplotlib.pyplot as plt 
import statsmodels.api as sm
import numpy as np 

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

## Here's how to get the first 5 rows of a column
	# first_five = loansData['Interest.Rate'][0:5]
## lambda is like a function but don't have to specify that it will return something (it always does)
	# g = lambda x: map(x)
## this is the template of what you should use to figure out mapping with lambda
	# r = map(function, sequence)
## other functions I don't know how to use yet -- reduce(), filter()

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))

loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))

loansData['FICO.Range'] = loansData['FICO.Range'].map(lambda x: x.split('-'))
## This is going to return a list showing start & end of ranges [start, end]
## To call on the first value in the first position of the list you ask loansData[0:5].values[0][0]

## Still need to convert FICO Range to ints. Everything within the [] is a list comprehension. 
## Need a list comprehension to get inside the list to conver to ints.
## Then grabs just the first column
loansData['FICO.Range'] = loansData['FICO.Range'].map(lambda x: [int(n) for n in x][0])

## Histogram 
# plt.figure()
# p = loansData['FICO.Range'].hist()
# plt.show()

# ## Scatterplot matrix to see how variables correlate with each other 
# plt.figure()
# a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
# plt.show()

## New variables
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Range']

## These variables will be a Series datatype. You want to reshape data. 
y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

## Create an input matrix with 2 columns together
x = np.column_stack([x1,x2])

## Create linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print(f.summary())




