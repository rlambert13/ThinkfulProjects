import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

# convert string to datetime object
df['issue_d_format'] = pd.to_datetime(df['issue_d'])
dfts = df.set_index('issue_d_format')
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

# trying to plot the series
ts = pd.Series(np.random.randn(1000), index=pd.issue_d_format('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

print(df.head())