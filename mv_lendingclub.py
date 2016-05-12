import numpy as np
import pandas as pd 
import statsmodels.api as sm
import statsmodels.formula.api as smf 
import matplotlib.pyplot as plt 
import math 

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData.to_csv('loansData_clean.csv', header=True, index=False)

## Use income (annual_inc) to model interest rates (int_rate).

loansData['InterestRate'] = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
# This returns monthly income as ints instead of floats (needs to remove NaNs first)
loansData['Monthly.Income'] = loansData[['Monthly.Income']].fillna(0.0).astype(int)
loansData['Annual.Inc'] = loansData['Monthly.Income'].map(lambda x: x*12)

# New Variables
intrate = loansData['InterestRate']
annual_inc = loansData['Annual.Inc']


# # Scatterplot matrix to see how variables correlate with each other 
# loansData_mod = loansData[['InterestRate', 'Annual.Inc']]
# plt.figure()
# a = pd.scatter_matrix(loansData_mod, alpha=0.05, figsize=(10,10), diagonal='hist')
# plt.show()

# y = np.matrix(intrate).transpose()
# x = np.matrix(annual_inc).transpose()

# # Create linear model
# X = sm.add_constant(x)
# model = sm.OLS(y,X)
# f = model.fit()

# # There does not appear to be a correlation between these variables 
# print(f.summary())

## Add home ownership to the model - does this affect significance of coeff in the original model?

# Encode Home Ownership as a numeric variable, rename column
loansData['HomeOwnership'] = pd.Categorical(loansData['Home.Ownership']).codes
# home_own = loansData['HomeOwnership']

# X = loansData.copy()
# y = X.pop('InterestRate')
# check = y.groupby(X.HomeOwnership).mean() # --> allows you to see how interest rate varies on avg based on home ownership status


loansData['Intercept'] = 1.0

# Creates a list of all the column header names 
ind_vars = ['Annual.Inc', 'HomeOwnership', 'Intercept']

max_inc = max(loansData['Annual.Inc'])
min_inc = min(loansData['Annual.Inc'])


# fit OLS on categorical variables 
def short_summary(est):
    return est.summary().tables[1]

# fit OLS on categorical variables 
est = smf.ols(formula='InterestRate ~ C(HomeOwnership)', data=loansData).fit()
coeff = est.params
print(short_summary(est))

# def calc_interest_rate(coeff, annual_inc, home_own):
# 	return coeff['Intercept'] + coeff['Annual.Inc']*annual_inc + coeff['HomeOwnership']*home_own

# p = calc_interest_rate(coeff, 50000, home_own=0)
# print(p)

x = np.linspace(min_inc, max_inc, 10000)
# p0 = log_function(coeff, x, home_own=0)
# p1 = log_function(coeff, x, home_own=1)
# p2 = log_function(coeff, x, home_own=2)
# p3 = log_function(coeff, x, home_own=3)
# p4 = log_function(coeff, x, home_own=4)

print(est.params)

plt.figure()
plt.xlabel('Annual Income')
plt.ylabel('Interest Rate')
# plt.plot(x, est.params[0] + est.params[1] * x + est.params[2] * 0, 'r')
# plt.plot(x, est.params[0] + est.params[1] * x + est.params[2] * 1, 'g')
# plt.plot(x, est.params[0] + est.params[1] * x + est.params[2] * 2, 'b')
# plt.plot(x, est.params[0] + est.params[1] * x + est.params[2] * 3, 'k')
# plt.plot(x, est.params[0] + est.params[1] * x + est.params[2] * 4, 'm')
# plt.plot(x, p0, 'g', x, p1, 'b', x, p2, 'r', x, p3, 'k', x, p4, 'm')
plt.show()






# Try to add the interaction of home ownership and incomes as a term. How does this impact the new model?



