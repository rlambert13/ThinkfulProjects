import pandas as pd 
import matplotlib.pyplot as plt 
import statsmodels.api as sm
import numpy as np 
import math

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')


loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))

loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))

loansData['FICO.Range'] = loansData['FICO.Range'].map(lambda x: x.split('-'))
## This is going to return a list showing start & end of ranges [start, end]
## To call on the first value in the first position of the list you ask loansData[0:5].values[0][0]

## Still need to convert FICO Range to ints. Everything within the [] is a list comprehension. 
## Need a list comprehension to get inside the list to conver to ints.
## Then grabs just the first column
loansData['FICO.Range'] = loansData['FICO.Range'].map(lambda x: [int(n) for n in x][0])

## Create a new column and insert whether interest rate is less than 12% 
loansData['IR_TF'] = loansData['Interest.Rate'].map(lambda x: 1 if x >= .12 else 0)
loansData['Intercept'] = 1.0

loansData.to_csv('loansData_clean.csv', header=True, index=False)

## Creates a list of all the column header names 
ind_vars = ['FICO.Range', 'Amount.Requested', 'Intercept']

## define the logistic regression model
## loansData[ind_vars] means this will pull all the values of these column names in this list
logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])

## fit the model
result = logit.fit()

## get fitted coefficient from results
coeff = result.params

# Linear predictor: interest_rate = −60.125 + 0.087423(FicoScore) − 0.000174(LoanAmount)
# Logistic function: p(x) = 1/(1 + e^(intercept + 0.087423(FicoScore) − 0.000174(LoanAmount))

def logistic_function(coeff, ficoScore, loanAmount):
	# replace ^ with ** because this isn't how you do exponents in python 
	p = 1/(1 + math.e**(coeff['Intercept'] + coeff['FICO.Range']*ficoScore + coeff['Amount.Requested']*loanAmount))
	return p

# Define a FICO Score & Loan amount
# FicoScore = 720
# LoanAmount = 10000

# p = logistic_function(coeff, FicoScore, LoanAmount)
# print(p)

x = np.linspace(550, 950, 200)
p = logistic_function(coeff, x, loanAmount=10000)

plt.figure()
plt.plot(x, p)
plt.show()



