import numpy as np
import pandas as pd 
import statsmodels.api as sm
import matplotlib.pyplot as plt 
import math 

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData.to_csv('loansData_clean.csv', header=True, index=False)

## Use income (annual_inc) to model interest rates (int_rate).

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))

# This returns monthly income as ints instead of floats (needs to remove NaNs first)
loansData['Monthly.Income'] = loansData[['Monthly.Income']].fillna(0.0).astype(int)

loansData['Annual.Inc'] = loansData['Monthly.Income'].map(lambda x: x*12)

# loansData['Home.Ownership'] = loansData['Home.Ownership'].map(lambda x: 1 if x >= .12 else 0)

# # New Variables
# intrate = loansData['Interest.Rate']
# annual_inc = loansData['Annual.Inc']


# ## Scatterplot matrix to see how variables correlate with each other 
# # loansData_mod = loansData[['Interest.Rate', 'Annual.Inc']]
# # plt.figure()
# # a = pd.scatter_matrix(loansData_mod, alpha=0.05, figsize=(10,10), diagonal='hist')
# # plt.show()

# y = np.matrix(intrate).transpose()
# x = np.matrix(annual_inc).transpose()

# # Create linear model
# X = sm.add_constant(x)
# model = sm.OLS(y,X)
# f = model.fit()

# # There does not appear to be a correlation between these variables 
# print(f.summary())




## Add home ownership to the model - does this affect significance of coeff in the original model?


# loansData['Intercept'] = 1.0

# # Creates a list of all the column header names 
# ind_vars = ['Annual.Inc', 'Home.Ownership', 'Intercept']

# max_inc = max(loansData['Annual.Inc'])
# min_inc = min(loansData['Annual.Inc'])


# # Define the logistic regression model
# logit = sm.Logit(loansData['Interest.Rate'], loansData[ind_vars])
# result = logit.fit()
# coeff = result.params




# def log_function(coeff, annual_inc, home_own):
# 	p = 1/(1 + math.e**(coeff['Intercept'] + coeff['Annual.Inc']*annual_inc 
# 		+ coeff['Home.Ownership']*home_own))
# 	return p

# x = np.linspace(min_inc, max_inc, 1000)
# p = log_function(coeff, x, home_own)

# plt.figure()
# plt.plot(x, p)
# plt.show()

print(loansData['Home.Ownership'].unique())



# Try to add the interaction of home ownership and incomes as a term. How does this impact the new model?



