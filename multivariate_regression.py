import pandas as pd
import numpy as py 
import statsmodels.api as sm 
import statsmodels.formula.api as smf

## Advertising Budget Exercise 

df_adv = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)

X = df_adv[['TV', 'Radio']]
y = df_adv['Sales']

# Fit a OLS model with intercept on TV & Radio
X = sm.add_constant(X)
est = sm.OLS(y, X).fit()

# Printing this will show you OLS regression results 
est.summary()



## Chronic Heart Disease Exercise 

df = pd.read_csv('http://statweb.stanford.edu/~tibs/ElemStatLearn/datasets/SAheart.data', index_col=0)

# Copy data & separate predictors & response
X = df.copy()
y = X.pop('chd')

# compute percentage of chronic heart disease for famhist
print(y.groupby(X.famhist).mean())

# need to convert categorical variables to numeric before running regression
df['famhis_ord'] = pd.Categorical(df.famhist).labels

est = smf.ols(formula="chd - famhist_ord", data=df).fit()


## Relationship between doc visits & income and binary variable health status 

df = pd.read_csv('https://raw2.github.com/statsmodels/statsmodels/master/'
                 'statsmodels/datasets/randhie/src/randhie.csv')
df["logincome"] = np.log1p(df.income)

df[['mdvis', 'logincome', 'hlthp']].tail()